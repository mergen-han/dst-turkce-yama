# art/ — Görsel varlıklar

Bu klasör Faz 8'de doldurulur. SDXL üretimi + manuel Türkçe yazı dizgisi + Workshop banner'ları + in-game screenshot'lar burada toplanır.

## Klasör yapısı

```
art/
├── README.md                      # Bu dosya
├── modicon/
│   ├── modicon_source.png         # 256×256 RGBA — Faz 9'da autocompiler ile .tex'e çevrilecek
│   ├── modicon_source.psd         # Photoshop kaynağı (katmanlı, opsiyonel)
│   ├── sdxl_raw_01.png            # SDXL ham çıktıları (yedek)
│   ├── sdxl_raw_02.png
│   └── sdxl_raw_03.png
└── workshop/
    ├── banner_512.png             # 512×512 — Workshop kart önizleme
    ├── banner_1920x620.png        # 1920×620 — Workshop wide banner
    ├── banner_source.psd          # Photoshop kaynağı
    └── screenshots/
        ├── 01_main_menu.jpg       # Ana menü ("Oyna / Ayarlar / Süs Dolabı")
        ├── 02_world_setup.jpg     # Yeni dünya kurma (mevsim/biyom Türkçe)
        ├── 03_character_select.jpg # Karakter seçim (biyografi/unvan)
        ├── 04_hud_inventory.jpg   # HUD + envanter incele tooltip
        ├── 05_crafting.jpg        # Üretim menüsü filtreleri
        ├── 06_options.jpg         # Ayarlar tooltip'leri
        ├── 07_server_lobby.jpg    # Sunucu lobi
        ├── 08_loading_tip.jpg     # Yükleme ekranı lore tip
        ├── 09_pig_king.jpg        # Domuzların Kralı interaksiyon
        ├── 10_skill_tree.jpg      # (Faz 4 sonrası) yetenek ağacı
        ├── 11_scrapbook.jpg       # Karalama Defteri (Faz 4 ✅)
        └── 12_quagmire.jpg        # Boğaz etkinliği (yemek tarifleri)
```

## Üretim sırası

1. **`modicon/`** — Faz 8 ilk iş. SDXL → manuel yazı → 256×256 export.
2. **`workshop/banner_*`** — modicon onaylandıktan sonra aynı stil ile.
3. **`workshop/screenshots/`** — in-game playtest sırasında çekilir; tam yama PO'ya yüklendikten sonra.

## Faz 9'da

- `modicon/modicon_source.png` → `autocompiler.exe` ile mod kök dizinine `modicon.tex` + `modicon.xml` üret.
- `modinfo.lua` içindeki `-- icon_atlas` ve `-- icon` satırlarındaki yorumu kaldır.
- `workshop/` içindeki banner'lar Steam Workshop yükleme sırasında upload formuna eklenir.

## Stil notları

- Tim Burton / gotik / eskimiş parşömen — Klei DST resmi sanat referansı.
- Renk paleti: parşömen krem (#E8D9B0), mürekkep siyah (#1C1812), kanlı kırmızı vurgu (#8B0000).
- Türkçe yazı **manuel** dizgi (SDXL Türkçe diakritik üretmede güvenilmez): font seçimi `docs/comfyui_prompts.md`'de.
- "Türkçe Yama" yazısı net görünür olmalı — ana menü modicon'unda 256×256'da bile okunabilir kalsın.
