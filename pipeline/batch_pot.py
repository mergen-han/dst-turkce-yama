"""strings.pot'u kategorilere göre gruplanmış JSON batch dosyalarına böler.

Her batch:
  - Aynı üst-kategorideki (STRINGS.NAMES, STRINGS.UI, STRINGS.ACTIONS vb.) msgid'leri içerir
  - Maksimum BATCH_SIZE msgid (varsayılan 200)
  - JSON formatı: {"batch_id": "0001", "category": "STRINGS.NAMES", "items": [...]}

Çıktılar:
  pipeline/batches/pending/batch_NNNN.json  (boş msgstr)
  pipeline/batches/index.json                (toplam sayım, kategori dağılımı)

Kullanım:
  python pipeline/batch_pot.py [--batch-size 200]
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import polib

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
POT_PATH = REPO_ROOT / "pipeline" / "raw" / "strings.pot"
BATCHES_DIR = REPO_ROOT / "pipeline" / "batches"
PENDING_DIR = BATCHES_DIR / "pending"
INDEX_PATH = BATCHES_DIR / "index.json"

RESERVED_LEAD_BYTES = (b"\xee", b"\xef")


def category_of(msgctxt: str) -> str:
    """STRINGS.NAMES.SPIDER → STRINGS.NAMES; STRINGS.UI.MAINSCREEN.PLAY → STRINGS.UI"""
    parts = msgctxt.split(".")
    if len(parts) >= 2:
        return ".".join(parts[:2])
    return msgctxt


def is_reserved(msgid: str) -> bool:
    if not msgid:
        return True
    encoded = msgid.encode("utf-8", errors="replace")
    return encoded[:1] in RESERVED_LEAD_BYTES


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=200, help="msgid/batch (varsayılan 200)")
    args = parser.parse_args()

    if not POT_PATH.exists():
        print(f"HATA: {POT_PATH} bulunamadı. Önce extract_pot.py çalıştır.", file=sys.stderr)
        sys.exit(1)

    print(f"POT okunuyor: {POT_PATH}")
    pot = polib.pofile(str(POT_PATH), encoding="utf-8")
    print(f"  Toplam msgid: {len(pot)}")

    by_category: dict[str, list[polib.POEntry]] = defaultdict(list)
    skipped_reserved = 0
    skipped_empty = 0

    for entry in pot:
        ctxt = entry.msgctxt or ""
        if not ctxt:
            skipped_empty += 1
            continue
        if is_reserved(entry.msgid):
            skipped_reserved += 1
            continue
        by_category[category_of(ctxt)].append(entry)

    PENDING_DIR.mkdir(parents=True, exist_ok=True)
    for old in PENDING_DIR.glob("batch_*.json"):
        old.unlink()

    batch_id = 1
    total_in_batches = 0
    cat_stats: list[tuple[str, int, int]] = []

    for cat in sorted(by_category):
        entries = by_category[cat]
        first_id = batch_id
        for i in range(0, len(entries), args.batch_size):
            chunk = entries[i : i + args.batch_size]
            items = [
                {
                    "ctxt": e.msgctxt,
                    "msgid": e.msgid,
                    "msgstr": "",
                }
                for e in chunk
            ]
            payload = {
                "batch_id": f"{batch_id:04d}",
                "category": cat,
                "items": items,
            }
            target = PENDING_DIR / f"batch_{batch_id:04d}.json"
            target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            total_in_batches += len(chunk)
            batch_id += 1
        cat_stats.append((cat, len(entries), batch_id - first_id))

    index = {
        "total_msgid": len(pot),
        "total_in_batches": total_in_batches,
        "skipped_reserved": skipped_reserved,
        "skipped_empty_ctxt": skipped_empty,
        "total_batches": batch_id - 1,
        "batch_size": args.batch_size,
        "categories": [
            {"category": c, "msgid_count": cnt, "batch_count": bc} for c, cnt, bc in cat_stats
        ],
    }
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n  Kategori sayısı: {len(by_category)}")
    print(f"  Atlanan (reserved bytes): {skipped_reserved}")
    print(f"  Atlanan (boş ctxt): {skipped_empty}")
    print(f"  Toplam batch: {batch_id - 1}")
    print(f"  Batch dizini: {PENDING_DIR}/")
    print(f"  Index: {INDEX_PATH}")
    print("\n  En büyük 10 kategori:")
    for cat, cnt, bc in sorted(cat_stats, key=lambda x: -x[1])[:10]:
        print(f"    {cat:40s} {cnt:6d} msgid  ({bc} batch)")


if __name__ == "__main__":
    main()
