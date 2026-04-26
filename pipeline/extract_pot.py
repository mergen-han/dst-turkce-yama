"""DST'nin scripts.zip'inden strings.pot ve speech_*.lua dosyalarını çıkarır.

Çıktılar:
  pipeline/raw/strings.pot
  pipeline/raw/speech/speech_<karakter>.lua  (19 dosya)
  pipeline/raw/version.txt  (DST sürümü, diff için)

Kullanım:
  python pipeline/extract_pot.py [--dst-path PATH]
"""

from __future__ import annotations

import argparse
import shutil
import sys
import zipfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

DEFAULT_DST_PATH = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Don't Starve Together")
SCRIPTS_ZIP = "data/databundles/scripts.zip"
POT_IN_ZIP = "scripts/languages/strings.pot"
SPEECH_PREFIX = "scripts/speech_"

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = REPO_ROOT / "pipeline" / "raw"


def extract(dst_path: Path) -> None:
    scripts_zip = dst_path / SCRIPTS_ZIP.replace("/", "\\")
    if not scripts_zip.exists():
        print(f"HATA: scripts.zip bulunamadı: {scripts_zip}", file=sys.stderr)
        sys.exit(1)

    version_file = dst_path / "version.txt"
    version = version_file.read_text().strip() if version_file.exists() else "unknown"

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    speech_dir = RAW_DIR / "speech"
    speech_dir.mkdir(exist_ok=True)

    pot_count = 0
    speech_count = 0

    with zipfile.ZipFile(scripts_zip) as zf:
        for name in zf.namelist():
            normalized = name.replace("\\", "/")

            if normalized == POT_IN_ZIP:
                target = RAW_DIR / "strings.pot"
                with zf.open(name) as src, target.open("wb") as dst:
                    shutil.copyfileobj(src, dst)
                size_mb = target.stat().st_size / 1024 / 1024
                print(f"  ✓ strings.pot — {size_mb:.2f} MB")
                pot_count += 1

            elif (
                normalized.startswith(SPEECH_PREFIX)
                and normalized.endswith(".lua")
                and "/speech_" in normalized
            ):
                filename = Path(normalized).name
                target = speech_dir / filename
                with zf.open(name) as src, target.open("wb") as dst:
                    shutil.copyfileobj(src, dst)
                speech_count += 1

    if pot_count == 0:
        print(f"HATA: {POT_IN_ZIP} bulunamadı", file=sys.stderr)
        sys.exit(1)

    print(f"  ✓ {speech_count} speech_*.lua dosyası → {speech_dir}/")
    (RAW_DIR / "version.txt").write_text(f"{version}\n")
    print(f"  ✓ DST sürümü: {version}")
    print(f"\nÇıkarma tamam → {RAW_DIR}/")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dst-path",
        type=Path,
        default=DEFAULT_DST_PATH,
        help=f"DST kurulum yolu (varsayılan: {DEFAULT_DST_PATH})",
    )
    args = parser.parse_args()
    print(f"DST → {args.dst_path}")
    extract(args.dst_path)


if __name__ == "__main__":
    main()
