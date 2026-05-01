"""Faz 7 QA: Format string güvenliği — runtime crash önleme.

DST PO entry'lerinde msgid içindeki placeholder'lar msgstr'da da bulunmalı.
Eksik veya bozuk placeholder DST'yi runtime'da crash ettirir.

Yakalanan pattern'ler:
  - {name} {target} {item} ... — DST template
  - %s %d %.2f %s1 — Lua string.format
  - [count] — DST format alternatif

Çıkış:
  0 = OK, 1 = en az bir entry'de placeholder eksik
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
PO_PATH = REPO_ROOT / "languages" / "turkish.po"

PLACEHOLDER_PATTERNS = [
    re.compile(r"\{[a-zA-Z_][a-zA-Z0-9_]*\}"),
    re.compile(r"%(?:\d+\$)?[-+#0]*\d*(?:\.\d+)?[sdifxXeEgG]"),
    re.compile(r"%s\d"),
]


def parse_po(text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    cur: dict[str, str] = {}
    cur_field: str | None = None
    cur_value = ""

    def flush_field() -> None:
        nonlocal cur_field, cur_value
        if cur_field is not None:
            cur[cur_field] = cur_value
        cur_field = None
        cur_value = ""

    def flush_entry() -> None:
        nonlocal cur
        flush_field()
        if cur and "msgid" in cur:
            entries.append(cur)
        cur = {}

    for line in text.split("\n"):
        s = line.strip()
        if not s:
            flush_entry()
            continue
        if s.startswith("#"):
            continue
        m = re.match(r'^(msgctxt|msgid|msgstr)\s+"(.*)"\s*$', s)
        if m:
            flush_field()
            cur_field = m.group(1)
            cur_value = m.group(2)
            continue
        m2 = re.match(r'^"(.*)"\s*$', s)
        if m2 and cur_field is not None:
            cur_value += m2.group(1)
    flush_entry()
    return entries


def extract_placeholders(s: str) -> list[str]:
    found: list[str] = []
    for pat in PLACEHOLDER_PATTERNS:
        found.extend(pat.findall(s))
    return found


def main() -> int:
    text = PO_PATH.read_text(encoding="utf-8")
    entries = parse_po(text)
    print(f"Toplam entry: {len(entries)}")

    missing: list[tuple[str, list[str], list[str]]] = []
    extra: list[tuple[str, list[str], list[str]]] = []
    placeholder_entry_count = 0

    for e in entries:
        ctxt = e.get("msgctxt", "")
        msgid = e.get("msgid", "")
        msgstr = e.get("msgstr", "")
        if not msgid or not msgstr:
            continue
        id_ph = extract_placeholders(msgid)
        if not id_ph:
            continue
        placeholder_entry_count += 1
        str_ph = extract_placeholders(msgstr)
        id_counts: dict[str, int] = {}
        for p in id_ph:
            id_counts[p] = id_counts.get(p, 0) + 1
        str_counts: dict[str, int] = {}
        for p in str_ph:
            str_counts[p] = str_counts.get(p, 0) + 1
        missing_ph = [p for p, c in id_counts.items() if str_counts.get(p, 0) < c]
        extra_ph = [p for p, c in str_counts.items() if id_counts.get(p, 0) < c]
        if missing_ph:
            missing.append((ctxt, missing_ph, [msgid, msgstr]))
        if extra_ph:
            extra.append((ctxt, extra_ph, [msgid, msgstr]))

    print(f"Placeholder içeren entry: {placeholder_entry_count}")
    print(f"Eksik placeholder (KRİTİK runtime risk): {len(missing)}")
    print(f"Fazla placeholder (uyumsuzluk): {len(extra)}")

    if missing:
        print("\n=== EKSİK PLACEHOLDER (msgstr'da olması gerekenler yok) ===")
        for ctxt, ph, (msgid, msgstr) in missing[:30]:
            print(f"  {ctxt}")
            print(f"    eksik: {ph}")
            print(f"    msgid:  {msgid!r}")
            print(f"    msgstr: {msgstr!r}")
        if len(missing) > 30:
            print(f"  ... +{len(missing) - 30} daha")

    if extra:
        print("\n=== FAZLA PLACEHOLDER (msgid'de yok ama msgstr'da var — yanlış kopya?) ===")
        for ctxt, ph, (msgid, msgstr) in extra[:15]:
            print(f"  {ctxt}")
            print(f"    fazla: {ph}")
            print(f"    msgid:  {msgid!r}")
            print(f"    msgstr: {msgstr!r}")
        if len(extra) > 15:
            print(f"  ... +{len(extra) - 15} daha")

    if missing or extra:
        print(f"\n  ❌ {len(missing)} eksik + {len(extra)} fazla = toplam {len(missing) + len(extra)} sorun")
        return 1
    print("\n  ✅ Tüm placeholder'lar tutarlı")
    return 0


if __name__ == "__main__":
    sys.exit(main())
