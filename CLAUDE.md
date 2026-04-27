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

**`PROGRESS.md`** dosyasını oku — Faz 3 başlangıç batch'ini bul.

Kabaca özet (Oturum 6 sonu, 2026-04-28):
- ✅ Faz 0+1 tamam (mod iskeleti + pipeline + docs)
- ✅ **Faz 2 UI %100 tamam** — 4.439/4.439 string PO'da
- 🟡 **Faz 3 devam** — Oturum 5+6'da 770 string yapıldı (ACTIONS+ANTIADDICTION+ARCHIVE+ATRIUM+BALATRO+BEEFALONAMING+BOARLORD+BROKENITEM+BUNNYMANNAMES+CARNIVAL_CROWKID 1-5)
- Toplam: **5.209/85.706 (%6.08)**
- Sıradaki: batch_0036'dan devam — CARNIVAL_CROWKID kalan blokları + CARNIVAL_HOST/CARNIVAL_HOST_GUARDS_*

## Faz 2 ✅ tamam (2026-04-28) — In-game tam Türkçe ekranlar

### Önceki oturumlar (1-3): Ana menü tüm tooltip'ler, Yeni Dünya Kurma (tüm canavar/biyom/preset), AYARLAR tam, Sunucu lobi, Mod yönetim, Yükleme ekranları (lore tip'leri), Vefat ilanları, Demirhane/Boğaz ödülleri, HUD aksiyonları, 50+ NETWORKDISCONNECT, 35 emoji, yemek tipleri

### Oturum 4 yenilikleri (1.439 string, 8 batch):
- **Sandbox menüsü tam** — slider/qty/loop seçenekleri, 10 Yıl Etkinliği, Karganaval/Cadılar/Kış Şöleni
- **SaveLoad / Karalama Defteri / Server Admin** — yasak listesi, snapshot, restore
- **Server Creation tam** — 4 playstyle (Rekabetçi/İşbirlikçi/Çılgınlık/Sosyal), Cave/UseCave, Privacy, UGC kontrolü
- **Server Listing tam** — filtre, World Progression Tags (Kadim Arşivler/Atriyum/Semavi Küre/Çiçekli Çeşmecik/Constant)
- **Süs Dolabı (Skinsscreen)** + Snowman dekorasyon + Special Event Names + Splitscreen + Adventure modu (Maxwell kapısı)
- **Lunar/Shadow Rift'ler** — "Hırsın Bedeli" diyalogları
- **Teleportato (TELEPORT)** — yola devam diyalogları
- **Takas Hanı (Trade Inn) DERİNLİK** — Karganaval mini oyun, Yavrukoon (Kitcoon) evcilleştirme + Tasmana Vuruldum, Gölge Tüccar (Mortal/ölümlü), Redbird/Snow/Crowkid mini oyunları, köylü ağızlı SKIN_COLLECTOR (tüccar)
- **Gardırop (WARDROBESCREEN)** + Word prediction
- **WORLDGEN tam** — 45 NOUNS atmosferik+karakter parça + 22 VERBS yükleme cümleleri
- **WORLDRESETDIALOG** — herkes öldü/dirilmek için ele geçir (haunt)
- **WXPLOBBYPANEL tam** — Demirhane/Boğaz maç sonu + TP sistemi (XP→TP)
- **WXP_DETAILS** — Milestone başarımları (Yabansavaşçısı/Gergedankardeşler/Timsahkomutanlar/Horultaplumbağalar)
- **XB1_USER_DIALOG** — Xbox kontrolcü diyalogları

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
| 4 | 2026-04-27/28 | 0777-0784 | 1.439 | PAUSEMENU sonu + PRESENCE + PURCHASEPACK + RARITY + RECIPE_BOOK + SANDBOXMENU tam + SAVELOAD + SCRAPBOOK + SERVERADMIN + SERVERCREATION tam + SERVERLISTING tam + SETPOPUP + SKINSSCREEN tam + SNOWMAN + SPECIAL_EVENTS + SPLITSCREEN + STARTADVENTURE + LUNAR/SHADOW_RIFTS + STATSPANEL + TELEPORT + TRADESCREEN derinlik (CROW/KITCOON/MAGICSKIN/REDBIRD/SNOW/SKIN_COLLECTOR) + WARDROBE + WORDPREDICTION + WORLDGEN tam + WORLDRESET + WXPLOBBYPANEL tam + WXP_DETAILS + XB1 + XPUTILS — **UI %100 BİTTİ** |
| 5 | 2026-04-28 | 0001-0008 | 609 | Faz 3 başladı: STRINGS.ACTIONS tam (490) + ANTIADDICTION + ARCHIVE_RUNE_STATUE + ATRIUM_OVERGROWTH + BALATRO (Klei cross-promo) + BEEFALONAMING (Bızonsığır rastgele isim üreteci) |
| 6 | 2026-04-28 | 0009-0035 | 161 | STRINGS.BOARLORD tam (Forge patron Pugna 7 round dramatik yay) + BROKENITEM + BUNNYMANNAMES (72 Tavşanadam bilim/havuç/element ismi) + CARNIVAL_CROWKID 1-5 (Karganaval Karga Veleti gak-gak banter) |

### Sonraki oturumda devam protokolü
1. Bu dosyayı (CLAUDE.md) oku
2. PROGRESS.md son ✅ Oturum altındaki sıradaki ⬜ batch'i bul (şu an: `batch_0036` — CARNIVAL_CROWKID devamı)
3. docs/glossary.tsv + docs/style-guide.md tekrar yükle (her oturum başı)
4. `pipeline/batches/pending/batch_NNNN.json` Read → çevir → `pipeline/batches/done/batch_NNNN.json` Write
5. Hedef: oturum başına ~150-200 string (büyüklüğüne göre 6-30 batch)
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
