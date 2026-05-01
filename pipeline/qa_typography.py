"""Faz 7 QA: Tipografi/punctuation kontrolü.

Yakalanan sorunlar:
  - Çift boşluk (görsel dağılma)
  - Cümle sonu boşluk (gereksiz)
  - Cümle başı boşluk
  - Yanlış noktalama (. . / , , / !! !! / ?? ??)
  - Üç nokta yerine ellipsis (… vs ...) — DST orijinali ... kullanır
  - Eksik cümle sonu (msgid noktayla bitiyor, msgstr noktasız)
  - Dengesiz parantez/tırnak
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
PO_PATH = REPO_ROOT / "languages" / "turkish.po"


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


def check_typography(msgid: str, msgstr: str) -> list[str]:
    issues: list[str] = []
    if "  " in msgstr and "  " not in msgid:
        issues.append("çift boşluk")
    if msgstr.startswith(" "):
        issues.append("baş boşluk")
    if msgstr.endswith(" "):
        issues.append("son boşluk")
    if re.search(r"[.,!?;:]\s+[.,!?;:]", msgstr):
        issues.append("ardışık noktalama")
    if "…" in msgstr:
        issues.append("ellipsis (…) — DST '...' kullanır")
    if re.search(r"\(\)|\[\]|\{\}", msgstr):
        issues.append("boş parantez")
    if msgstr.count("(") != msgstr.count(")"):
        issues.append("dengesiz () parantez")
    if msgstr.count("[") != msgstr.count("]"):
        issues.append("dengesiz [] parantez")
    if msgid and msgid[-1] in ".!?" and msgstr and msgstr[-1] not in ".!?…\"":
        if not msgstr.endswith("\\n"):
            issues.append(f"msgid '{msgid[-1]}' ile biter, msgstr noktasız")
    if msgid and msgid[-1] not in ".!?" and msgstr and msgstr[-1] in ".!?":
        if not msgstr.endswith("..."):
            if msgid[-1] not in '"' and msgstr[-1] != msgid[-1]:
                issues.append(f"msgid noktasız, msgstr '{msgstr[-1]}' ile biter")
    return issues


def main() -> int:
    text = PO_PATH.read_text(encoding="utf-8")
    entries = parse_po(text)

    by_issue: dict[str, list[tuple[str, str, str]]] = {}
    total_problematic = 0

    for e in entries:
        ctxt = e.get("msgctxt", "")
        msgid = e.get("msgid", "")
        msgstr = e.get("msgstr", "")
        if not msgid or not msgstr:
            continue
        issues = check_typography(msgid, msgstr)
        if issues:
            total_problematic += 1
            for issue in issues:
                by_issue.setdefault(issue, []).append((ctxt, msgid, msgstr))

    print(f"Toplam entry: {len(entries)}")
    print(f"Sorunlu entry: {total_problematic}")
    print(f"Sorun kategorisi: {len(by_issue)}\n")

    for issue, items in sorted(by_issue.items(), key=lambda kv: -len(kv[1])):
        print(f"=== {issue}: {len(items)} entry ===")
        for ctxt, msgid, msgstr in items[:8]:
            ctxt_short = ctxt.replace("STRINGS.", "")
            print(f"  {ctxt_short}")
            print(f"    EN: {msgid!r}")
            print(f"    TR: {msgstr!r}")
        if len(items) > 8:
            print(f"  ... +{len(items) - 8} daha")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
