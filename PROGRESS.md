# DST Türkçe Yama — Çeviri İlerlemesi

> Bu dosya her çeviri oturumu sonu güncellenir. Aydın'ın "ne çevirildi, ne kaldı" görmesi + sonraki oturumdaki Claude için referans.

**Toplam hedef:** 85.706 msgid / 970 batch
**Son güncelleme:** 2026-04-26 (Oturum 2 TAMAM — 6 batch / 1.200 string + priority_mainscreen 39 string)

---

## 📊 Genel Durum

| Faz | Açıklama | Hedef | Tamam | % |
|---|---|---|---|---|
| 0 | Mod iskeleti + smoke test | — | ✅ | 100 |
| 1 | Pipeline + docs + smoke | — | ✅ | 100 |
| **2** | **STRINGS.UI** (UI/menü) | **4.439** | **🟡 1.839** | **41** |
| 3 | STRINGS.NAMES + RECIPE_DESC + INV_DESC + COOKBOOK + PLANTREGISTRY | ~5.000 | ⬜ | 0 |
| 4 | STRINGS.SCIENCE_TAB + CRAFTING_FILTER + SKILLTREE + STAGEPLAY | ~2.000 | ⬜ | 0 |
| 5 | STRINGS.CHARACTERS (17 karakter speech) | 62.645 | ⬜ | 0 |
| 6 | STRINGS.SKIN_NAMES + SKIN_DESCRIPTIONS + LORE | ~7.806 | ⬜ | 0 |
| 7 | QA + playtest | — | ⬜ | 0 |
| 8 | Logo + Workshop varlıkları | — | ⬜ | 0 |
| 9 | Yayın v1.0 | — | ⬜ | 0 |

**Şu ana kadar çevrilen toplam:** 1.839 / 85.706 msgid (%2.15)

---

## Faz 2 — STRINGS.UI (23 batch / 4.439 string)

### ✅ Oturum 1 — 2026-04-26 (4 batch / 639 string)

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `priority_mainscreen` | 39 | MAINSCREEN/LOBBY kritik override (Oyna/Ayarlar/Modlar/Çıkış/Külliyat/Oyun Listesi/Oyun Kur). 0772/0773 sıra geldiğinde override edilecek. | ✅ |
| `0762` | 200 | UI.ACCOUNT (login/şifre/kayıt) + ACHIEVEMENTS.LAVAARENA Forge başarımları (kelime oyunlu başlıklar Türkçe pun'a uyarlandı) | ✅ |
| `0763` | 200 | Forge kalan + Quagmire/Gorge başarımları + BARTERSCREEN (Süs Dokuma Tezgahı, Bobin/Doku/Söke) + BROADCASTING (Twitch yayın) + BUGREPORTSCREEN + BUILTINCOMMANDS başlangıcı | ✅ |
| `0764` | 200 | BUILTINCOMMANDS sonu (kick/ban/rollback/woby) + CHARACTERSELECT + CHATINPUTSCREEN + COLLECTIONSCREEN (Süs Dolabı 14 sekme) + 14 renk + COMPENDIUM (Külliyat sekmeleri) + CONTROLSSCREEN ilk 102 kontrol | ✅ |

### ✅ Oturum 2 — 2026-04-26 (6 batch / 1.200 string)

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0765` | 200 | CONTROLSSCREEN devamı (klavye tuşları A-Z/F1-15/Num/semboller — çoğu çevrilmedi, sadece açıklayıcı tuşlar Türkçe: Yukarı/Sağ/Boşluk/Yardım vb.) + Inv 11-15 + Toggle Target locking + Modifier 1 + Character Command Wheel + 14 controller tipi (Xbox/PS4/PS5/Switch/Steam Deck/DualSense/Joy-Con/Vita) | ✅ |
| `0766` | 200 | CONTROLSSCREEN sonu (PS4/Vita kontrol şemaları, Type 1-7) + COOKBOOK (yemek kitabı: pişirme süresi, bozulma, yan etkiler — Akıl/Açlık/Can sıralama) + **CRAFTING başlangıcı** (NEEDS_* mesajları: Bilim Makinesi/Simya Motoru/Gölge Manipülatörü/Tencere/Yemek Kitabı/Marangoz Tezgahı/Tapınaklar — Karnaval/Kış Şöleni/Cadılar Bayramı + Year of the X yıl etkinlikleri) | ✅ |
| `0767` | 200 | CRAFTING devamı (RECIPEACTION/TABACTION: Karıştır/Sahiplen/Sun/Takas Et/Yarat/Yerleştir/Dönüştür/Çiz/Öğüt/Satın Al) + CRAFTING_FILTERS (Zırh/Karakter Eşyaları/Kıyafet/Depolama/Pişirme/Süslemeler/Hepsi/Favoriler/Balıkçılık/Yemek ve Bahçıvanlık/Işık Kaynakları/Büyü/Mod Eşyaları/Yağmur Donanımı/İşlenmiş Malzemeler/İyileştirme/Bızonsığır Binme/Denizcilik/Yapılar/Aletler/Silahlar) + CRAFTING_MENU (Favorilere Ekle/Sabitle/Ara/Görünüm Seç/Üretilebilir/Alfabetik) + CRAFTING_STATION_FILTERS (Kadim Sözdebilim/Karganaval Yaratımı/Süs Sandığı/Marangozluk/Haritacılık/Semavi/Baharatlar/Şişe Takası/Çay Demleme/Aydındemirhane/Çılgın Bilim/Yaratıklar/Takas Kulübesi/Heykeller/Codex Umbra/Gölge Sanatı/İnci Sanatı/İmalat/Ticaret/Kış Şöleni Pişirmesi/Sunular) + CREDITS başlangıcı | ✅ |
| `0768` | 200 | CREDITS sonu (Klei geliştirici listesi NAMES.64-95 + ALTGAMES/BABEL/BLIT/HUWIZ/LOLLI/SKYMAP/SONY studio'ları + JENERİK/Teşekkürler metni — Klei'ye özel uzun teşekkür çevrildi) + CROSS_SAVE_DIALOG (PS4 import) + CUSTOMIZATIONSCREEN başlangıcı (Asit Yağmuru, Av Sürprizleri, Kadim Geçit, Sonbahar, Karganaval, Mevsim ayarları, Mob isimleri A-I) | ✅ |
| `0769` | 200 | CUSTOMIZATIONSCREEN devamı J-S (mob/biyom/preset adları: Krampuslar/Likenler/Ağaçmuhafızlar/Şimşek Keçileri/Adamotları/Köstebekler/Splumaymunlar/Havufareler/Salatamender/Düşmanavarlar/Pengullar/Yutkunlar/Domuz Evleri/Ay Quay Korsanları + **PRESETLEVELDESC + PRESETLEVELS** preset açıklamaları "Standart Don't Starve deneyimi"/"Daha sert bir dünya"/"Demirhane'de kendini kanıtla"/"Boğaz'ın sıcağına dayanabilir misin?"/"Vahşi Doğa" — Çılgın Ahmet, Adan Sana Balta gibi yerelleştirmeler) | ✅ |
| `0770` | 200 | CUSTOMIZATIONSCREEN sonu (Sahne Oyunları/Mevsim/Birlikte/Demirhane/Boğaz biyom + Mantarkurbağa/Diriliş Taşları/Kayadallar/Yuvarlanan Otlar/Wobsterler/Yüce Solucan + 10 Yıl Etkinliği: Bızonsığır/Tavşanadam/Havufare/Kedikoon/Yusufçuk/Yutkun/Mekanik Şövalye/Domuzların Kralı/Derinlik Solucanı/Varg) + DATACOLLECTION (Veri Toplama, Çevrimdışı Mod) + DATE.MONTH_ABBR (Oca-Ara) + DAYS_FORMAT + DEMOOVERDIALOG + DRESSUP_AVATAR + DRONE_ZAP + EMAILSCREEN (kayıt formu) + EMOTES (35 ifade: Kızgın/Tezahürat/Tavuk Dansı/Mutlu/Kahkaha/Robot Dansı/Step Dansı/Şapka Selamı vb.) + EULADIALOG + EVENT_QUICKJOINSCREEN + FESTIVALEVENTSCREEN (Demirhane/Boğaz etkinlikleri) + FOOD_TYPES.BERRY (başlangıç) | ✅ |

### ⬜ Oturum 3 — sıradaki (hedef ~6 batch, başlangıç batch_0771)

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0771` | 200 | FOOD_TYPES sonu + LAVAARENA + LOADING_SCREEN_LORE_TIPS | ⬜ |
| `0772` | 200 | LOADING_SCREEN_LORE_TIPS sonu + LOBBYSCREEN + LOBBY_WAITING + **MAINSCREEN ilk yarısı** (priority_mainscreen override edilir) | ⬜ |
| `0773` | 200 | **MAINSCREEN ikinci yarısı** + MODSSCREEN | ⬜ |
| `0774` | 200 | MODSSCREEN devamı + NETWORKDISCONNECT | ⬜ |
| `0775` | 200 | NETWORKDISCONNECT sonu + **OPTIONS başlangıcı (yüksek görünür: ses/grafik/genel)** | ⬜ |
| `0776` | 200 | **OPTIONS devamı** (parlaklık/ekran/dil) + PAUSEMENU | ⬜ |

### ⬜ Oturum 4 — (hedef ~7 batch + 39)

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0777` | 200 | PAUSEMENU sonu + PRESENCE | ⬜ |
| `0778` | 200 | PRESENCE sonu + SANDBOXMENU | ⬜ |
| `0779` | 200 | SANDBOX sonu + SERVERCREATIONSCREEN (yeni sunucu) | ⬜ |
| `0780` | 200 | **SERVERCREATIONSCREEN devamı + SERVERLISTING** | ⬜ |
| `0781` | 200 | **SERVERLISTING devamı (sunucu tarayıcısı)** + TRADESCREEN başlangıcı | ⬜ |
| `0782` | 200 | TRADESCREEN devamı | ⬜ |
| `0783` | 200 | TRADESCREEN sonu + WXP_DETAILS | ⬜ |
| `0784` | 39 | WXP_DETAILS sonu + XPUTILS (UI son batch) | ⬜ |

---

## Faz 3+ — sonraki büyük bloklar (özet)

| Bölüm | msgid | Önemi | Strateji |
|---|---|---|---|
| `STRINGS.NAMES` (item isimleri) | ~2.802 | ⭐⭐⭐ Çok yüksek görünür | Faz 3 öncelikli — glossary'yi item-bazlı genişlet |
| `STRINGS.RECIPE_DESC` | ~956 | ⭐⭐ Yüksek | Faz 3 |
| `STRINGS.INV_DESC` (envanter açıklamaları) | ~? | ⭐⭐ Yüksek | Faz 3 |
| `STRINGS.SCRAPBOOK` | ~690 | ⭐⭐ | Faz 4 |
| `STRINGS.SKILLTREE` | ~718 | ⭐⭐ | Faz 4 |
| `STRINGS.STAGEACTOR` | ~622 | ⭐ | Faz 4 |
| `STRINGS.SCIENCE_TAB` | ~? | ⭐⭐ | Faz 4 |
| `STRINGS.SKIN_NAMES` | ~3.903 | ⭐ | Faz 6 |
| `STRINGS.SKIN_DESCRIPTIONS` | ~3.903 | ⭐ | Faz 6 |
| **`STRINGS.CHARACTERS`** (17 karakter speech) | **~62.645** | ⭐⭐⭐ Persona kritik | **Faz 5** — Wilson referans, sonra her karakter ayrı persona prompt |

---

## 📌 Kararlar & Notlar

- **Glossary uyarıları (false-positive):** Validator "Friends/Save/Cancel/Dusk/Log" gibi terimler için katı eşleşme arıyor; "dost / kayıt / iptal / akşam / günlük" gibi bağlamsal varyantlar uyarı çıkarıyor ama **hata değil**, geçer.
- **priority_mainscreen geçici batch:** 0772/0773 sıra geldiğinde tam bağlamlı versiyonla override edilecek (merge_translations.py duplicate ctxt'lerde son tanım kazanır). Sonra silinecek.
- **Üç farklı kelime oyunlu başlık** (Forge başarımları): "Down But Not Snout" → "Bitap Düştük, Burnumuz Sapasağlam" gibi Türkçe pun yaratıldı. Aydın redakte ederse buradan başlasın.
- **Lavaarena = Demirhane, Quagmire = Boğaz/Gorge** olarak sabitlendi.
- **Curio Cabinet → Süs Dolabı**, **Curio Loom → Süs Dokuma Tezgahı**, **Spool → Bobin**, **Weave → Doku**, **Unravel → Söke** kalıcı.

---

## Sonraki oturum başlatma rehberi (Claude'a not)

> Compact sonrası yeni oturumda Aydın "devam" derse:

### 1. Bağlam yükle (paralel Read)
- `CLAUDE.md` — proje özeti + çalışma yöntemi (zaten oku)
- `PROGRESS.md` — bu dosya, sıradaki ⬜ batch hangisi gör
- `docs/glossary.tsv` — 121 zorunlu terim
- `docs/style-guide.md` — disiplin kuralları
- `docs/character-voices.md` — 17 karakter persona (Faz 5 için)

### 2. Sıradaki batch'i çevir
```bash
# Read
pipeline/batches/pending/batch_0771.json     # ← şu an buradan başlıyoruz (Oturum 3)

# Write (çevirisi yapılmış halde)
pipeline/batches/done/batch_0771.json
```

### 3. Oturum sonu prosedürü
```bash
cd "C:\Users\colak\Desktop\dst-turkce-yama"
python pipeline/merge_translations.py
python pipeline/validate_po.py
cp languages/turkish.po "C:\Program Files (x86)\Steam\steamapps\common\Don't Starve Together\mods\dst-turkce-yama\languages\turkish.po"

# PROGRESS.md güncelle (bu dosya):
# - Genel Durum tablosunda Faz 2 sayısını artır
# - "Şu ana kadar çevrilen toplam" güncelle
# - "Oturum N" başlığında ⬜ → ✅, batch satırına gerçek kapsamı yaz

git add .
git commit -m "feat(faz-2): oturum N — batch XXXX-YYYY (NN string)"
git push
```

### 4. Aydın'a bildirilecek
- Hangi yeni Türkçe ekranlar görülebilir (in-game test rehberi)
- Toplam ilerleme % (UI bazlı + genel)
- Sonraki oturum hedef batch'ler

### 5. Aydın "compact" derse
- CLAUDE.md ve PROGRESS.md zaten güncel olmalı
- Tüm değişiklikler commit + push edilmiş olmalı
- Pending iş bırakma — done/ klasörüne yazıp merge'le
