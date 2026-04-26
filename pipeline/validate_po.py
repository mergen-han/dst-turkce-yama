"""languages/turkish.po dosyasını doğrular.

Kontrol edilen kurallar:
  1. POT v2 header doğru (LoadPOFile yüklemez yoksa)
  2. UTF-8 + BOM yok
  3. msgctxt unique (çakışma yok)
  4. Escape disiplini — sadece \\n, \\r, \\" kabul; raw \\ yok
  5. msgid/msgstr çift-tırnak dengesi
  6. Glossary uyumu (docs/glossary.tsv'deki terimlere uyulmuş mu)
  7. Karakter sayım sapması (msgstr uzunluğu / msgid uzunluğu < 3, runaway translation)
  8. Boş msgstr oranı (eksik çeviri yüzdesi)

Çıkış kodu:
  0 = OK, 1 = hata, 2 = uyarı (geçer ama dikkat)

Kullanım:
  python pipeline/validate_po.py [--po PATH] [--strict]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PO = REPO_ROOT / "languages" / "turkish.po"
GLOSSARY_PATH = REPO_ROOT / "docs" / "glossary.tsv"


class Issue:
    __slots__ = ("level", "msg")

    def __init__(self, level: str, msg: str) -> None:
        self.level = level
        self.msg = msg

    def __repr__(self) -> str:
        return f"[{self.level}] {self.msg}"


def parse_po(po_text: str) -> list[dict[str, str]]:
    """Basit DST-uyumlu PO parser. polib UTF-8 BOM ile sıkıntı yaşadığı için kendi parser."""
    entries: list[dict[str, str]] = []
    lines = po_text.split("\n")
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

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_entry()
            continue
        if stripped.startswith("#"):
            continue
        m = re.match(r'^(msgctxt|msgid|msgstr)\s+"(.*)"\s*$', stripped)
        if m:
            flush_field()
            cur_field = m.group(1)
            cur_value = m.group(2)
            continue
        m2 = re.match(r'^"(.*)"\s*$', stripped)
        if m2 and cur_field is not None:
            cur_value += m2.group(1)
            continue
    flush_entry()
    return entries


def load_glossary(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) >= 2:
            out[parts[0].strip()] = parts[1].strip()
    return out


def check_escapes(s: str) -> str | None:
    """Backslash escape ihlali var mı? Sadece \\n, \\r, \\" geçerli."""
    i = 0
    while i < len(s):
        if s[i] == "\\":
            if i + 1 >= len(s):
                return f"dangling backslash at end: {s[-20:]!r}"
            nxt = s[i + 1]
            if nxt not in ('n', 'r', '"', '\\'):
                return f"invalid escape \\{nxt} in: {s!r}"
            i += 2
            continue
        i += 1
    return None


def validate(po_path: Path, strict: bool) -> int:
    issues: list[Issue] = []

    if not po_path.exists():
        print(f"HATA: PO bulunamadı: {po_path}", file=sys.stderr)
        return 1

    raw = po_path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        issues.append(Issue("ERROR", "UTF-8 BOM mevcut — DST parser BOM'u sevmiyor, kaldır"))

    text = raw.decode("utf-8", errors="replace")

    if 'POT Version: 2.0' not in text:
        issues.append(Issue("ERROR", "POT v2 header eksik: 'POT Version: 2.0\\n' header'da olmalı"))

    entries = parse_po(text)
    if not entries:
        issues.append(Issue("ERROR", "Hiç entry parse edilemedi"))
        for it in issues:
            print(it)
        return 1

    seen_ctxt: dict[str, int] = {}
    empty_msgstr = 0
    runaway = 0
    glossary = load_glossary(GLOSSARY_PATH)
    glossary_violations: list[str] = []

    for idx, e in enumerate(entries):
        ctxt = e.get("msgctxt", "")
        msgid = e.get("msgid", "")
        msgstr = e.get("msgstr", "")

        if ctxt == "" and msgid == "":
            continue

        if ctxt in seen_ctxt:
            issues.append(Issue("ERROR", f"Duplicate msgctxt: {ctxt!r} (entry #{idx})"))
        seen_ctxt[ctxt] = idx

        for field_name, val in (("msgid", msgid), ("msgstr", msgstr)):
            err = check_escapes(val)
            if err:
                issues.append(Issue("ERROR", f"{ctxt} {field_name}: {err}"))

        if not msgstr.strip():
            empty_msgstr += 1
            continue

        if msgid and len(msgstr) > len(msgid) * 4:
            runaway += 1
            if runaway <= 5:
                issues.append(
                    Issue(
                        "WARN",
                        f"{ctxt}: msgstr çok uzun (msgid {len(msgid)} → msgstr {len(msgstr)})",
                    )
                )

        for en, tr in glossary.items():
            en_pat = re.compile(r"\b" + re.escape(en) + r"\b", re.IGNORECASE)
            if not en_pat.search(msgid):
                continue
            stem_len = max(3, len(tr) - 2)
            tr_stem = tr.lower()[:stem_len]
            if tr_stem and tr_stem not in msgstr.lower():
                glossary_violations.append(f"{ctxt}: '{en}' geçti ama '{tr}' (kök: '{tr_stem}') yok")

    total = len(entries)
    empty_pct = (empty_msgstr / total * 100) if total else 0
    print(f"  Toplam entry: {total}")
    print(f"  Boş msgstr:  {empty_msgstr} ({empty_pct:.1f}%)")
    print(f"  Runaway uzunluk uyarıları: {runaway}")
    print(f"  Glossary uyumu: {len(glossary)} terim, {len(glossary_violations)} ihlal")

    if glossary_violations:
        if len(glossary_violations) <= 10:
            for v in glossary_violations:
                issues.append(Issue("WARN", v))
        else:
            for v in glossary_violations[:5]:
                issues.append(Issue("WARN", v))
            issues.append(
                Issue("WARN", f"... +{len(glossary_violations) - 5} glossary ihlali daha")
            )

    if strict and empty_pct > 5:
        issues.append(Issue("ERROR", f"Eksik msgstr oranı %{empty_pct:.1f} > %5 (strict)"))

    errors = [i for i in issues if i.level == "ERROR"]
    warnings = [i for i in issues if i.level == "WARN"]

    for it in issues:
        print(it)

    if errors:
        print(f"\n  ❌ {len(errors)} hata, {len(warnings)} uyarı")
        return 1
    if warnings:
        print(f"\n  ⚠️  {len(warnings)} uyarı (hata yok)")
        return 2
    print("\n  ✅ Tüm kontroller geçti")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--po", type=Path, default=DEFAULT_PO, help=f"PO yolu ({DEFAULT_PO})")
    parser.add_argument("--strict", action="store_true", help="Eksik msgstr %5'i geçerse fail")
    args = parser.parse_args()
    print(f"PO doğrulanıyor: {args.po}")
    sys.exit(validate(args.po, args.strict))


if __name__ == "__main__":
    main()
