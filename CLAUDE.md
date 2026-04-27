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

**`PROGRESS.md`** dosyasını oku — "⬜ Oturum 4" bölümü altında ⬜ işaretli ilk batch'ten başla.

Kabaca özet (oturum 3 sonu, 2026-04-27):
- ✅ Faz 0+1 tamam (mod iskeleti + pipeline + docs)
- ✅ Faz 2 oturum 1+2+3 tamam: 0762-0776 + priority_mainscreen = **3.000 string** PO'da (%3.50 / %68 UI)
- ⬜ Sıradaki: `batch_0777.json` (PAUSEMENU sonu + PRESENCE — Oturum 4 başlangıcı)

## Compact öncesi tam durum (2026-04-27)

### Çevrilen ana ekranlar (in-game görünür):
- **Ana menü** (Oyna/Ayarlar/Modlar/Çıkış/Külliyat/Oyun Listesi/Oyun Kur/Süs Dolabı/Hazine/Jenerik) — tooltip'ler dahil
- **Yeni Dünya Kurma menüsü** — tüm canavar/biyom adları + 10 Yıl Etkinliği + preset açıklamaları
- **AYARLAR menüsü tam** — ses/grafik/HUD/dokunsal/ipuçları + tüm tooltip açıklamaları
- **Sunucu lobi ekranı** — karakter seç/skin/loadout
- **Mod yönetim ekranı** — yapılandırma/uyumluluk/atölye filtreleri
- **Yükleme ekranları** — Wilson notebook alıntıları + 14 karakter lore tip'i
- **Vefat ilanları (Morgue)** — geçmiş/karşılaşmalar
- **Demirhane/Boğaz etkinlikleri** — istatistik ödülleri (Suikastçı/Şifacı/Şef/Oduncu)
- **HUD** — Saldır/İncele/Kuşan/Bayat/Bozuk/Erimiş + ölüm anonsları
- **Tüm hata/bağlantı mesajları** — 50+ NETWORKDISCONNECT + EULA + DATACOLLECTION
- **Emoji menüsü** — 35 ifade
- **Yemek tipleri** — Et/Sebze/Meyve/Korkunç/Lifli vb.

### Kalıcı yerelleştirme kararları (glossary'den):
- Health/Sanity/Hunger = **Can/Akıl/Açlık** (asla "sağlık" değil)
- Spider Den = **Örümcek İni**, Pig King = **Domuzların Kralı**
- Eyebrella = **Gözlemsiye**, Touch Stone = **Diriliş Taşı**
- The Forge = **Demirhane**, The Gorge = **Boğaz**
- Curio Cabinet = **Süs Dolabı**, Spool = **Bobin**, Weave = **Doku**
- Florid Postern = **Çiçekli Çeşmecik**, Meat Effigy = **Et Heykel**
- Year of the X = **X Yılı** (10 yıl etkinliği)
- Cawnival = **Karganaval** (karga + karnaval pun)
- Gnarwail = **Hırlbalina** (gnar + narwhal)
- Catcoon = **Kedikoon**, Beefalo = **Bızonsığır**
- Crazy Eddie preset = **Çılgın Ahmet** (yerelleştirme)

### Stil disiplini:
- "Sen" = karakter→oyuncu, item açıklamaları, replikler
- "Siz" = sistem/lobby/menu yönergeleri (sadece gerektiğinde)
- Klei pun'ları → Türkçe pun (motamot YASAK)
- Karakter özel isimleri çevrilmez (Wilson/Maxwell/Krampus/Klaus)
- Kelime oyunu olan unvanlar uyarlanır (All's Well That Maxwell → Sonu İyi Olan Maxwell)

### Oturum geçmişi
| Oturum | Tarih | Batch | String | Kapsam özeti |
|---|---|---|---|---|
| 1 | 2026-04-26 | priority_mainscreen + 0762-0764 | 639 | MAINSCREEN override + ACCOUNT + ACHIEVEMENTS + BARTERSCREEN + BUILTINCOMMANDS + COLLECTIONSCREEN + COMPENDIUM + CONTROLSSCREEN ilk |
| 2 | 2026-04-26 | 0765-0770 | 1.200 | CONTROLSSCREEN sonu + COOKBOOK + CRAFTING + CREDITS + CUSTOMIZATIONSCREEN tam (10 yıl etkinliği dahil) + DATACOLLECTION + DATE + EMOTES + EULA + FESTIVAL + FOOD_TYPES başlangıcı |
| 3 | 2026-04-27 | 0771-0776 | 1.200 | FOOD_TYPES sonu + GAMEMODES + GENDERSTRINGS + HELP + HUD + LAVAARENA + LOADING_SCREEN ipuçları + LOBBYSCREEN + MAINSCREEN tam + MODSSCREEN + MORGUESCREEN + MVP_LOADING + NETWORKDISCONNECT (50+ hata) + NOTIFICATION + OPTIONS tam (tooltip'ler) + PAUSEMENU başlangıcı |

### Sonraki oturumda devam protokolü
1. Bu dosyayı (CLAUDE.md) oku
2. PROGRESS.md "⬜ Oturum 4" altındaki ⬜ ilk batch'i bul (şu an: `batch_0777`)
3. docs/glossary.tsv + docs/style-guide.md tekrar yükle (her oturum başı)
4. `pipeline/batches/pending/batch_NNNN.json` Read → çevir → `pipeline/batches/done/batch_NNNN.json` Write
5. 6 batch hedef (oturum başı bilgi yükleme + 6 × ~5-10 dk çeviri)
6. Oturum sonu: merge + validate + DST sync + PROGRESS.md güncelle + commit + push

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

- Mevcut topluluk Türkçe yamaları base alma — **sıfırdan AI-destekli kaliteli çeviri** mantığı zorunlu.
- Karakter ses tonu (Wilson akademik, Wendy melankolik, WX-78 BÜYÜK HARF, Wormwood yarım Türkçe, Wortox kafiyeli) Faz 5'te zorunlu.
- DST mods klasörüne kopyalarken DAİMA `cp` veya `Write` — link/symlink kurma (Windows izinleri).
