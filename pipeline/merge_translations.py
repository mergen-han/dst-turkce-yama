"""Tamamlanmış batch JSON dosyalarını birleştirip languages/turkish.po üretir.

Akış:
  pipeline/batches/done/batch_*.json  →  languages/turkish.po

Kurallar:
  - POT v2 header zorunlu (Translator:LoadPOFile bu olmadan yüklemez)
  - Sadece \\n, \\r, \\" escape edilir (DST'nin gettext-lite parser'ı backslash escape etmez)
  - UTF-8, BOM yok, LF line ending
  - Boş msgstr varsa ilgili msgctxt'i atla (mod İngilizce'ye düşer, yani fallback)

Kullanım:
  python pipeline/merge_translations.py
  python pipeline/merge_translations.py --include-pending  # boş batch'leri de dahil et (test için)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
DONE_DIR = REPO_ROOT / "pipeline" / "batches" / "done"
PENDING_DIR = REPO_ROOT / "pipeline" / "batches" / "pending"
PO_OUT = REPO_ROOT / "languages" / "turkish.po"

POT_HEADER = (
    'msgid ""\n'
    'msgstr ""\n'
    '"Application: Don\'t Starve\\n"\n'
    '"POT Version: 2.0\\n"\n'
    "\n"
)


def escape_dst(s: str) -> str:
    """DST gettext-lite escape: sadece \\n, \\r, \\" kaçışlanır."""
    return s.replace("\r", "\\r").replace("\n", "\\n").replace('"', '\\"')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--include-pending",
        action="store_true",
        help="Pending batch'lerdeki dolu msgstr'ları da dahil et (geçici çeviriler)",
    )
    parser.add_argument(
        "--allow-empty-output",
        action="store_true",
        help="Hiç batch yoksa boş PO yaz (ilk kurulumda kullanışlı)",
    )
    args = parser.parse_args()

    sources: list[Path] = []
    if DONE_DIR.exists():
        sources.extend(sorted(DONE_DIR.glob("batch_*.json")))
    if args.include_pending and PENDING_DIR.exists():
        sources.extend(sorted(PENDING_DIR.glob("batch_*.json")))

    if not sources and not args.allow_empty_output:
        print("HATA: çevrilmiş batch yok (pipeline/batches/done/ boş).", file=sys.stderr)
        print("       --include-pending veya --allow-empty-output dene.", file=sys.stderr)
        sys.exit(1)

    by_ctxt: dict[str, tuple[str, str]] = {}
    duplicates = 0
    empty_skipped = 0

    for src in sources:
        try:
            data = json.loads(src.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"HATA: {src} JSON parse: {e}", file=sys.stderr)
            sys.exit(1)
        for item in data.get("items", []):
            ctxt = item["ctxt"]
            msgid = item["msgid"]
            msgstr = item.get("msgstr", "")
            if not msgstr.strip():
                empty_skipped += 1
                continue
            if ctxt in by_ctxt and by_ctxt[ctxt] != (msgid, msgstr):
                duplicates += 1
            by_ctxt[ctxt] = (msgid, msgstr)

    PO_OUT.parent.mkdir(parents=True, exist_ok=True)
    with PO_OUT.open("w", encoding="utf-8", newline="\n") as f:
        f.write(POT_HEADER)
        for ctxt in sorted(by_ctxt):
            msgid, msgstr = by_ctxt[ctxt]
            f.write(f"#. {ctxt}\n")
            f.write(f'msgctxt "{escape_dst(ctxt)}"\n')
            f.write(f'msgid "{escape_dst(msgid)}"\n')
            f.write(f'msgstr "{escape_dst(msgstr)}"\n\n')

    print(f"  ✓ {len(by_ctxt)} msgctxt yazıldı → {PO_OUT}")
    print(f"  Atlanan (boş msgstr): {empty_skipped}")
    if duplicates:
        print(f"  UYARI: {duplicates} duplicate ctxt çakışması, son tanım kazandı")


if __name__ == "__main__":
    main()
