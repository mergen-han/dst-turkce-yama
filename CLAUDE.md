# Claude Code — Bu Repo İçin Bağlam

> Bu dosya yeni Claude oturumlarına proje durumunu hızlıca aktarır. **Önce bunu, sonra `PROGRESS.md`'yi oku.**

---

## Proje Özeti

**Don't Starve Together (DST) için Türkçe yama modu.**

- Sahip: Aydın Çolak — `mergen-han` (GitHub).
- Repo: `github.com/mergen-han/dst-turkce-yama` (public, MIT + CC-BY-SA)
- Çalışma dizini: `C:\Users\colak\Desktop\dst-turkce-yama\`
- DST yerel test klasörü: `C:\Program Files (x86)\Steam\steamapps\common\Don't Starve Together\mods\dst-turkce-yama\`
- Hedef yayın: Steam Workshop + GitHub açık kaynak (Faz 9'da)
- Plan dosyası: `C:\Users\colak\.claude\plans\dont-starve-together-i-in-proud-wombat.md`

## Çalışma Yöntemi (kritik)

**Çeviri kanalı = Claude Code üyeliği.** API key yok. Ben (Claude) batch JSON dosyalarını **Read** ile okur, çeviririm, **Write** ile yazarım. Pipeline scriptleri sadece batch hazırlama/birleştirme/doğrulama yapar.

### Akış (her oturumda)

```
pipeline/batches/pending/batch_NNNN.json   ←  Read
                                                ↓
                                            (Claude çevirir)
                                                ↓
pipeline/batches/done/batch_NNNN.json      ←  Write
```

Sonra:
```bash
python pipeline/merge_translations.py    # done/ → languages/turkish.po
python pipeline/validate_po.py           # syntax + glossary kontrolü
cp languages/turkish.po "/c/Program Files (x86)/Steam/steamapps/common/Don't Starve Together/mods/dst-turkce-yama/languages/turkish.po"
git add . && git commit -m "..." && git push
```

## Çeviri Disiplini — ZORUNLU okumalar

Her oturum başında bu üç dosyayı oku (Aydın'ın "devam" demesi yetiyor):

1. **`docs/glossary.tsv`** — 121+ zorunlu terim. Spider Den = Örümcek İni, Pig King = Domuzların Kralı, Health/Sanity/Hunger = Can/Akıl/Açlık vb. ASLA sapma.
2. **`docs/style-guide.md`** — sen/siz, sayı+isim tekil, kelime oyunu stratejisi, escape kuralları.
3. **`docs/character-voices.md`** — 17 karakter ses tonu (Faz 5'te kullanılacak).

## Sıradaki Adım

**`PROGRESS.md`** dosyasını oku — "🟡 Oturum 2 — devam ediyor" bölümü altında ⬜ işaretli ilk batch'ten başla.

Kabaca özet (compact zamanı, 2026-04-26):
- ✅ Faz 0+1 tamam (mod iskeleti + pipeline + docs)
- 🟡 Faz 2 oturum 2 yarıda: 0762-0766 ✅ + priority_mainscreen ✅ = **1.039 string** PO'da
- ⬜ Sıradaki: `batch_0767.json` (CRAFTING devamı + CREDITS başlangıcı)

## Kritik Teknik Noktalar

- **POT v2 header zorunlu** PO'da (yoksa DST yüklemez): `"Application: Don't Starve\n"` + `"POT Version: 2.0\n"` — `pipeline/merge_translations.py` otomatik ekler.
- **DST mod sandbox strict mode** — `pcall`, `print`, `pairs`, `ipairs`, `type`, `tostring` global'lerine `GLOBAL.<func>` prefix gerek (modmain.lua başında `local pcall = GLOBAL.pcall` vb.).
- **Forest/Cave shard ayrımı** — `modmain.lua`'da `AddSimPostInit` + `AddPlayerPostInit` ile her shard load'da Translator + speech merge yeniden uygulanır (rakip yamaların ana yarası).
- **Escape**: sadece `\n`, `\r`, `\"`. Backslash escape **etme**.
- **UTF-8** — Türkçe ş ç ğ İ ö ü doğal yaz, fallback font destekliyor (Faz 0 smoke test doğruladı).

## Pipeline Komutları

```bash
# POT'u yeniden çıkar (DST güncellendiğinde)
python pipeline/extract_pot.py

# POT'u 200-msgid batch'lere böl (970 batch)
python pipeline/batch_pot.py

# done/ batch'lerini turkish.po'ya birleştir
python pipeline/merge_translations.py

# PO doğrulaması
python pipeline/validate_po.py

# DST sürüm diff'i (gelecekte güncelleme zamanı)
python pipeline/diff_pot.py
```

## Aydın'ın Kullanım Talimatları

- "devam" → `PROGRESS.md`'deki sonraki ⬜ batch'ten başla.
- "X commit + push yap" → tüm değişiklikleri repo'ya gönder.
- "test edeyim" → DST'yi açıp Aydın test eder; ben yeni Türkçeleşen ekranları listelerim.
- "compact" → `CLAUDE.md` + `PROGRESS.md` + `docs/` ile yeni oturumda kalan iş tamlanabilir; tüm batch'ler `pipeline/batches/done/` altında kalıcı.

## Önemli URL'ler

- Repo: https://github.com/mergen-han/dst-turkce-yama
- DST API docs (referans): https://vietnd69.github.io/dst-api-webdocs/
- Klei forum modding: https://forums.kleientertainment.com/forums/forum/79-dont-starve-together-mods-and-tools/

## Yapılmaması Gereken (Aydın'ın notu)

- Mevcut Türkçe yamalar (peter_a_klei koleksiyonu, officialvolkan vb.) Google Translate kalitesinde — onları base alma. **Sıfırdan AI-destekli kaliteli çeviri**.
- Karakter ses tonu (Wilson akademik, Wendy melankolik, WX-78 BÜYÜK HARF, Wormwood yarım Türkçe, Wortox kafiyeli) Faz 5'te zorunlu.
- DST mods klasörüne kopyalarken DAİMA `cp` veya `Write` — link/symlink kurma (Windows izinleri).
