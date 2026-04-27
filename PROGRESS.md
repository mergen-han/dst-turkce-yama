# DST Türkçe Yama — Çeviri İlerlemesi

> Bu dosya her çeviri oturumu sonu güncellenir. Aydın'ın "ne çevirildi, ne kaldı" görmesi + sonraki oturumdaki Claude için referans.

**Toplam hedef:** 85.706 msgid / 970 batch
**Son güncelleme:** 2026-04-27 (Oturum 3 TAMAM — 6 batch / 1.200 string)

---

## 📊 Genel Durum

| Faz | Açıklama | Hedef | Tamam | % |
|---|---|---|---|---|
| 0 | Mod iskeleti + smoke test | — | ✅ | 100 |
| 1 | Pipeline + docs + smoke | — | ✅ | 100 |
| **2** | **STRINGS.UI** (UI/menü) | **4.439** | **🟡 3.000** | **68** |
| 3 | STRINGS.NAMES + RECIPE_DESC + INV_DESC + COOKBOOK + PLANTREGISTRY | ~5.000 | ⬜ | 0 |
| 4 | STRINGS.SCIENCE_TAB + CRAFTING_FILTER + SKILLTREE + STAGEPLAY | ~2.000 | ⬜ | 0 |
| 5 | STRINGS.CHARACTERS (17 karakter speech) | 62.645 | ⬜ | 0 |
| 6 | STRINGS.SKIN_NAMES + SKIN_DESCRIPTIONS + LORE | ~7.806 | ⬜ | 0 |
| 7 | QA + playtest | — | ⬜ | 0 |
| 8 | Logo + Workshop varlıkları | — | ⬜ | 0 |
| 9 | Yayın v1.0 | — | ⬜ | 0 |

**Şu ana kadar çevrilen toplam:** 3.000 / 85.706 msgid (%3.50)

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

### ✅ Oturum 3 — 2026-04-27 (6 batch / 1.200 string)

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0771` | 200 | FOOD_TYPES sonu (Yanık/Element/Et/Çiğ/Sebze) + GAMEMODES tam (Endless/Forge/Gorge/Survival/Wilderness açıklamalı) + GENDERSTRINGS (TR cinsiyet yok → hep "o/onun") + HELP (kontrol yardım butonları) + HUD (oyun arayüzü temel: Saldır/İncele/Kuşan/Bayat/Bozuk/Erimiş + ölüm anonsları + Quagmire bildirimleri + Trophyscale Merm sahipleri) + INTENTION + ITEM_SCREEN (eşya alma) + ITEM_SERVER + LAVAARENA_COMMUNITY_UNLOCKS başlangıcı | ✅ |
| `0772` | 200 | LAVAARENA_COMMUNITY_UNLOCKS sonu (görev tipleri/zırh tanımları/silah açılışları) + LAVAARENA_QUESTS_HISTORY/SUMMARY + **LOADING_SCREEN_CONTROL_TIPS** (klavye+kontrolcü ipuçları) + **LOADING_SCREEN_LORE_TIPS** (Charlie/Maxwell/Wendy/Webber/Wilson/Winona/Woodie karakterleri kısa anlatım) + **LOADING_SCREEN_SURVIVAL_TIPS** (Wilson notebook alıntıları — uzun atmosferik metinler) + LOBBYSCREEN tam (karakter seç/skin/loadout) + LOBBY_WAITING_FOR_PLAYERS + **MAINSCREEN ilk yarısı** (Hesap/Görüntü Alanı/Macera/Yine de Oyna/Beta/Yayında/Oyun Listesi/Oyun Kur/Konsol/Külliyat/Devam/Kontroller/Kontrolcü/Jenerik/Sil/Demirhane Betası/Yayın/Anahtar) | ✅ |
| `0773` | 200 | **MAINSCREEN ikinci yarısı** (Aile Paylaşımı/Demirhane'ye Gir/Sanal Kum/Oyun Sihirbazı/Hediye/Merhaba/IP ile Katıl/Giriş Yap/Yetenek Vurgusu/Mod Forumları/Klei Mağaza/Hazine/Oyna!/Çevrimiçi Oyna/Bölünmüş Ekran/Süs Dolabı/Hileler/Yeniden Başlat/Oyundan Çık/Hata Ayıklama/Tooltip'ler) + MODSSCREEN ilk kısmı (Tümü/Uygula/Bağımlılıklar/Mod Uyarısı/Yapılandır/Devre Dışı/İstemci Modları/Uyumluluk) | ✅ |
| `0774` | 200 | MODSSCREEN devamı (Yerel/Mod Sayfası/Hepsini Güncelle/Atölye/Çöktü/Yapılandırma) + MORGUESCREEN (Vefat İlanları/Karşılaşmalar/Geçmiş) + MORTALITYSTRINGS (ölümlü/şeytan-Wortox) + MVP_LOADING_WIDGET (Forge: Suikastçı/Şifacı/Diriltici + Quagmire: Şef/Hasatçı/Tarımcı/Mutfak Felaketi) + MYSTERYBOXSCREEN + NETWORKDISCONNECT.BODY ilk kısmı (E_BANNED/E_DELETED/Bağlantı sorunları) | ✅ |
| `0775` | 200 | NETWORKDISCONNECT.BODY sonu + NETWORKDISCONNECT.TITLE tam (Bağlantı Kesildi/Sürüm Uyumsuzluğu/Sunucu Dolu/Yasaklı/Atıldı vb. 50+ başlık) + NEW_CONTROLSCHEME_POPUP + NOTIFICATION (Bağlanılıyor/Yükleniyor/Dünya Üretiliyor/Oyuna Katıldı/Atıldı) + OBJECTOWNERSHIP + OPTIONS başlangıcı (A-D: Onayla/Çevre Sesi/Otomatik Giriş/Yapı Hizalaması/Geri/Sırt Çantası/Parlama/Tekne/Üretim/Veri Toplama/Loş) | ✅ |
| `0776` | 200 | **OPTIONS devamı E-Y** (En Loş/Bozulma/Tam Ekran/Ses Efekt/Grafikler/Boss Efektleri/HUD Boyutu/Giriş Cihazı/Bütünleşik/Diller/Yükleme İpuçları/Mini Harita/Müzik/Çevrimiçi/Oyun Ayarları + **TÜM TOOLTIP'LER** — kontrol açıklamaları/sosyal menü/grafik kalitesi/dokunsal efektler/yıldırım/Wigfrid Umlaut) + PAUSEMENU başlangıcı (Mola Ver/Otomatik Duraklatıldı) | ✅ |

### ⬜ Oturum 4 — sıradaki (hedef ~7 batch + 39, başlangıç batch_0777)

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

### Validator notları
- **Glossary uyarıları (false-positive):** Validator "Friends/Save/Cancel/Dusk/Log" gibi terimler için katı eşleşme arıyor; "dost / kayıt / iptal / akşam / günlük" gibi bağlamsal varyantlar uyarı çıkarıyor ama **hata değil**, geçer.
- **priority_mainscreen geçici batch:** 0772/0773 işlendi → MAINSCREEN tam bağlamlı versiyonla override edildi (merge_translations.py son tanım kazanır). priority_mainscreen.json silinmedi ama artık önceliği yok.

### Kalıcı yerelleştirme sözlüğü (oturum 1-3'te kabul edilenler)

**Mekânlar/Yapılar:**
- The Forge → **Demirhane**
- The Gorge → **Boğaz**
- Curio Cabinet → **Süs Dolabı**
- Curio Loom → **Süs Dokuma Tezgahı**
- Florid Postern → **Çiçekli Çeşmecik**
- Touch Stone → **Diriliş Taşı**
- Meat Effigy → **Et Heykel**
- Atrium → **Atriyum**
- Ancient Gateway → **Kadim Geçit**
- Hot Springs → **Kaplıcalar**
- Junk Yard → **Hurdalık**

**Karakterler/Mob'lar (özel isim → çeviri):**
- Beefalo → **Bızonsığır**
- Catcoon → **Kedikoon** (kedi + raccoon)
- Bunnyman → **Tavşanadam**
- Werepig → **Kurtdomuz**
- Deerclops → **Geyikgöz**
- Bearger → **Ayıger**
- Toadstool → **Mantarkurbağa**
- Crab King → **Yengeçlerin Kralı**
- Tallbird → **Uzunkuş**
- Treeguard → **Ağaçmuhafız**
- Carrat (carrot+rat) → **Havufare**
- Saladmander → **Salatamender**
- Gnarwail → **Hırlbalina** (gnar + narwhal)
- Anenemy (anemone+enemy) → **Düşmanavar**
- Spilagmite (spider+stalagmite) → **Örümşit**
- Pengull → **Pengul**
- Splumonkey → **Splumaymun**
- Marotter (marine+otter) → **Denisamur**

**Sistem/Stat:**
- Health/Sanity/Hunger → **Can/Akıl/Açlık** (ASLA "sağlık")
- Spool → **Bobin**, Weave → **Doku**, Unravel → **Söke**
- XP → **TP** (tecrübe puanı)

**Etkinlikler/Pun'lar:**
- Cawnival (crow+carnival) → **Karganaval**
- Year of the X → **X Yılı** (10 yıl etkinliği: Bızonsığır/Tavşanadam/Havufare/Kedikoon/Yusufçuk/Yutkun/Mekanik Şövalye/Domuzların Kralı/Derinlik Solucanı/Varg)
- Hallowed Nights → **Cadılar Bayramı Geceleri**
- Winter's Feast → **Kış Şöleni**
- All's Well That Maxwell → **Sonu İyi Olan Maxwell** (Klei pun)
- Where There's a Wilson... → **Wilson Olan Yerde...**

**Preset oyun adları (yerelleştirme):**
- Crazy Eddie → **Çılgın Ahmet**
- Soggy → **Sırılsıklam**
- Together Forever → **Sonsuza Dek Birlikte**
- Lights Out → **Işıklar Sönsün**
- Wilderness → **Vahşi Doğa**
- Endless → **Sonsuz**

**Forge başarım pun'ları (oturum 1):**
- "Down But Not Snout" → "Bitap Düştük, Burnumuz Sapasağlam"
- (Aydın redakte ederse Forge başarımlarından başlasın)

**Yiyecek tipleri:**
- Burnt → Yanık, Edible → Yenilebilir, Goodies → Atıştırmalıklar
- Horrible → Korkunç, Insect → Böcek, Monstrous → Canavarsı
- Roughage → Lifli, Seed → Tohum, Veggie → Sebze, Wood → Odun

**UI temel:**
- Play → Oyna, Quit → Çıkış, Cancel → İptal, Apply → Uygula
- Browse Games → Oyun Listesi, Host Game → Oyun Kur
- Compendium → Külliyat, Workshop → Atölye
- Curio Cabinet → Süs Dolabı, Treasury → Hazine
- Save/Load → Kaydet/Yükle, Resume → Devam Et

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
pipeline/batches/pending/batch_0777.json     # ← şu an buradan başlıyoruz (Oturum 4)

# Write (çevirisi yapılmış halde)
pipeline/batches/done/batch_0777.json
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
- CLAUDE.md ve PROGRESS.md zaten güncel olmalı (her oturum sonu güncellenir)
- Tüm değişiklikler commit + push edilmiş olmalı
- Pending iş bırakma — done/ klasörüne yazıp merge'le
- **`pipeline/batches/done/` git'te değil (`.gitignore`'da)** — ama lokal disk'te kalıcı, reproducible
- Yeni oturum protokolü (compact sonrası):
  1. CLAUDE.md oku (ana bağlam + oturum geçmişi + kalıcı kararlar)
  2. PROGRESS.md oku (sıradaki ⬜ batch + glossary kararları)
  3. docs/glossary.tsv + docs/style-guide.md tekrar yükle
  4. Sıradaki batch'ten devam (kaldığı yerden)

---

## 🗂️ Compact öncesi durum kayıt (2026-04-27)

**Yapılan iş özeti:**
- 4 commit: `ec0eb59` (faz 0+1), `2d45792` (compact prep oturum 1), `5e900b0` (oturum 2), `2310dba` (oturum 3)
- 3.000 string PO'da, 18 batch JSON done/ altında
- Mod DST'de çalışıyor (sandbox sorunu çözüldü, mağarada da çalışır)
- README.md güncel (rakip yama atfı kaldırıldı, pozitif tona alındı)

**Ana ekran kapsamı (in-game test için):**
- Ana menü tam Türkçe + tooltip'ler
- Yeni Dünya Kurma menüsü (preset/biyom/canavar/yıl etkinliği)
- AYARLAR menüsü tam (ses/grafik/HUD/dokunsal + tooltip'ler)
- Sunucu lobi (karakter seç/skin/loadout)
- Mod yönetim ekranı
- Yükleme ekranları (Wilson/Maxwell/Wendy/Webber lore tip'leri)
- Vefat ilanları (Morgue)
- Demirhane/Boğaz etkinlik istatistikleri
- HUD aksiyonları (Saldır/İncele/Kuşan/Bayat...)
- Tüm bağlantı/hata mesajları (50+)
- 35 emoji ifadesi
- Yemek tipleri

**Sıradaki adımlar (Faz 2 oturum 4):**
- batch_0777: PAUSEMENU sonu + PRESENCE
- batch_0778: PRESENCE sonu + SANDBOXMENU
- batch_0779: SANDBOX sonu + SERVERCREATIONSCREEN
- batch_0780: SERVERCREATION devamı + SERVERLISTING
- batch_0781: SERVERLISTING devamı + TRADESCREEN başlangıcı
- batch_0782: TRADESCREEN devamı
- batch_0783: TRADESCREEN sonu + WXP_DETAILS
- batch_0784: WXP sonu + XPUTILS (UI **son** batch — 39 öğe)
- → Oturum 4 sonu: Faz 2 UI %100 tamam (4.439/4.439)
- → Faz 3 başlar: STRINGS.NAMES + RECIPE_DESC + INV_DESC (item çevirisi)
