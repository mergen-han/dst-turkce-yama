# DST Türkçe Yama

Don't Starve Together için açık kaynak, kapsamlı, **bağlamsal** Türkçe çeviri modu.

> 🚧 **Geliştirme aşamasında — Faz 0 (smoke test).** Şu an yalnızca birkaç ana menü stringi çevrilmiş. Tam yama (UI + itemler + 19 karakter konuşmaları) v1.0 ile gelecek.

## Neden başka bir Türkçe yama?

Mevcut yamalar (peter_a_klei, officialvolkan, vb.) Google Translate ile çevrilmiş, **mağarada çalışmıyor** (Forest/Cave shard ayrımı), 6000+ satır boş, item isimleri tutarsız. Bu mod:

- 🤖 **AI-destekli + insan redakte:** Claude ile bağlamsal çeviri, glossary/style-guide disipliniyle tutarlı.
- 🕳️ **Mağarada çalışır:** `AddSimPostInit` + `AddPlayerPostInit` ile shard transition'larında çeviri yeniden yüklenir.
- 🎭 **Karakter ses tonu korunur:** 19 karakterin her biri için ayrı persona (Wilson akademik, Wendy melankolik, WX-78 büyük harf mekanik, Wormwood yarım Türkçe...).
- 📜 **Açık kaynak:** Topluluk PR'larıyla canlı kalır, DST güncellemelerinde otomatik diff.
- 📦 **Tek mod:** Forest + Cave için tek mod, ayrı "server versiyonu" gerekmez.

## Kurulum

> **Workshop link Faz 9'da eklenecek.** Şu an yerel test için:

1. Bu repo'yu klonla veya ZIP indir.
2. İçeriği şuraya kopyala: `Steam/steamapps/common/Don't Starve Together/mods/dst-turkce-yama/`
3. DST'yi başlat → **Mods → Client Mods → Türkçe Yama → Enable → Apply**.

## Lisans

- **Kod** (Lua mod, Python pipeline): [MIT](LICENSE)
- **Çeviri metinleri** (`languages/*.po`, `scripts/speech_overrides/*.lua`): CC-BY-SA 4.0

## Katkı

Bkz. `CONTRIBUTING.md` (yakında). Yanlış çeviri / eksik metin / bug için **Issues** sekmesi.

---

**Sahip:** [@mergen-han](https://github.com/mergen-han) · **Build:** DST `722900` · **Sürüm:** `0.1.0-faz0`
