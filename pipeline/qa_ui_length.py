"""Faz 7 QA: UI uzunluk kontrolü — HUD slot taşması raporu.

Türkçe çeviri İngilizceden %15-30 uzun olur. UI/HUD bağlamında sabit slotlar
(buton, tab, status etiket) varsa taşma riski. Bu script şüpheli adayları
listeler — Aydın'ın in-game test sırasında inceleyebileceği shortlist.

Kapsam: STRINGS.UI.* hiyerarşisi (menü/buton/tab/seçim ekranları).
Eşik: msgstr / msgid > 1.6 ve msgid >= 4 karakter.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
PO_PATH = REPO_ROOT / "languages" / "turkish.po"

UI_PREFIXES = (
    "STRINGS.UI.",
    "STRINGS.NAMES.",
    "STRINGS.ACTIONS.",
    "STRINGS.RECIPE_DESC.",
    "STRINGS.CRAFTING_FILTERS.",
    "STRINGS.SCRAPBOOK.SUBCATS.",
    "STRINGS.SCRAPBOOK.CATS.",
)

RATIO_THRESHOLD = 1.6
MIN_MSGID_LEN = 4


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


def main() -> int:
    text = PO_PATH.read_text(encoding="utf-8")
    entries = parse_po(text)

    candidates: list[tuple[float, str, str, str]] = []
    for e in entries:
        ctxt = e.get("msgctxt", "")
        msgid = e.get("msgid", "")
        msgstr = e.get("msgstr", "")
        if not ctxt.startswith(UI_PREFIXES):
            continue
        if not msgid or not msgstr:
            continue
        if "\\n" in msgid or "\\n" in msgstr:
            continue
        if len(msgid) < MIN_MSGID_LEN:
            continue
        if len(msgid) > 60:
            continue
        ratio = len(msgstr) / len(msgid)
        if ratio >= RATIO_THRESHOLD:
            candidates.append((ratio, ctxt, msgid, msgstr))

    candidates.sort(reverse=True)
    print(f"Toplam UI/short entry: incelenen {len(entries)}")
    print(f"Şüpheli (ratio >= {RATIO_THRESHOLD}, msgid {MIN_MSGID_LEN}-60 char): {len(candidates)}")
    print()
    print("Top 50 (manuel inceleme adayı — buton/tab/etiket taşma riski):")
    print(f"{'oran':<5}  {'msgid len':<3}  {'msgstr len':<3}  ctxt")
    print("-" * 100)
    for ratio, ctxt, msgid, msgstr in candidates[:50]:
        ctxt_short = ctxt.replace("STRINGS.", "")
        print(f"{ratio:<5.2f}  {len(msgid):<10}  {len(msgstr):<10}  {ctxt_short}")
        print(f"        EN: {msgid!r}")
        print(f"        TR: {msgstr!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
