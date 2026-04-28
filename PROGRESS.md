# DST Türkçe Yama — Çeviri İlerlemesi

> Bu dosya her çeviri oturumu sonu güncellenir. Aydın'ın "ne çevirildi, ne kaldı" görmesi + sonraki oturumdaki Claude için referans.

**Toplam hedef:** 85.706 msgid / 970 batch
**Son güncelleme:** 2026-04-28 (Oturum 8 ✅ — Faz 3 Seçenek B: CHARACTER_* karakter kartları + STRINGS.NAMES başlangıcı)

---

## 📊 Genel Durum

| Faz | Açıklama | Hedef | Tamam | % |
|---|---|---|---|---|
| 0 | Mod iskeleti + smoke test | — | ✅ | 100 |
| 1 | Pipeline + docs + smoke | — | ✅ | 100 |
| **2** | **STRINGS.UI** (UI/menü) | **4.439** | **✅ 4.439** | **100** |
| 3 | STRINGS.NAMES + RECIPE_DESC + INV_DESC + COOKBOOK + PLANTREGISTRY | ~5.000 | ⬜ | 0 |
| 4 | STRINGS.SCIENCE_TAB + CRAFTING_FILTER + SKILLTREE + STAGEPLAY | ~2.000 | ⬜ | 0 |
| 5 | STRINGS.CHARACTERS (17 karakter speech) | 62.645 | ⬜ | 0 |
| 6 | STRINGS.SKIN_NAMES + SKIN_DESCRIPTIONS + LORE | ~7.806 | ⬜ | 0 |
| 7 | QA + playtest | — | ⬜ | 0 |
| 8 | Logo + Workshop varlıkları | — | ⬜ | 0 |
| 9 | Yayın v1.0 | — | ⬜ | 0 |

**Şu ana kadar çevrilen toplam:** 5.756 / 85.706 msgid (%6.72)

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

### ✅ Oturum 4 — 2026-04-27/28 (8 batch / 1.439 string — UI BİTTİ!)

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0777` | 200 | PAUSEMENU + PLANTREGISTRY (Wickerbottom -W açıklamaları, pun'lar) + PLAYERSTATUSSCREEN (admin/ban/kick/oylama) + PLAYERSUMMARYSCREEN + POPUPDIALOG + PORTRAIT + PRESENCE başlangıcı | ✅ |
| `0778` | 200 | PRESENCE sonu + PUMPKIN_CARVING + PURCHASEPACKSCREEN tam (Klei mağaza) + QUICKJOINSCREEN + RARITY (10 nadirlik) + RECIPE_BOOK (Warly arzu sistemi) + REDEEMDIALOG + SANDBOXMENU başlangıcı (Adventure presetleri) | ✅ |
| `0779` | 200 | SANDBOXMENU devamı (slider/qty/loop + Special Events: Karganaval/Cadılar/Kış Şöleni/10 Yıl Etkinliği) + SAVELOAD (bozuk veri/yedek) + SCRAPBOOK + SERVERADMINSCREEN tam (yasak listesi/snapshot/restore) + SERVERCREATIONSCREEN başlangıcı (intention 4 playstyle) | ✅ |
| `0780` | 200 | SERVERCREATIONSCREEN devamı (NEWGAME/NEWHOST/OFFLINE/PRIVACY/PVP/PRESETS/USECAVES/WORLDGEN_FAILED) + SERVERLISTING başlangıcı (filtre/clan/dedicated/intention) | ✅ |
| `0781` | 200 | SERVERLISTING devamı (Phases/Ping/Players/Refresh/Report/Seasons/Sort/WORLDPROGRESSION_TAGS — Kadim Arşivler/Atriyum Anahtarı/Semavi Küre/Çiçekli Çeşmecik/Constant) + SETPOPUP + SKINSSCREEN (Süs Dolabı tam) + SNOWMAN_DECORATING + SPECIAL_EVENT_NAMES + SPLITSCREEN + STARTADVENTURE + START_LUNAR/SHADOW_RIFTS + STATSPANEL + TELEPORT + TIME_FORMAT + TRADESCREEN/CROWKID_GAME başlangıcı | ✅ |
| `0782` | 200 | TRADESCREEN derinlik: CROW_GAME (Karganaval mini oyun, ambalaj toplama) + KITCOON_GAME (Yavrukoon evcilleştirme: Tasmana Vuruldum) + MAGICSKIN_COLLECTOR_SPEECH (Gölge Tüccar - "ölümlü") + REDBIRD_GAME (yumurta toplama) + SKIN_COLLECTOR_SPEECH (köylü ağızlı tüccar tam: Start/Result/Lucky/Trade/Warning) + SKIN_COLLECTOR_SPEECH_CROW/CROWKID/REDBIRD/SNOW (mini oyun replikleri) + SNOWBIRD | ✅ |
| `0783` | 200 | SNOW_GAME sonu + TRADESCREEN sonu (Sold Out/Specials/Warning) + UNLOCKMAXWELL (Maxwell tahtı) + UPGRADEMODULEDISPLAY (WX-78 modüller) + USERCOMMANDS (komut hata mesajları) + VOTEDIALOG + WARDROBESCREEN tam (Gardırop) + WORDPREDICTIONWIDGET + **WORLDGEN tam** (45 NOUNS atmosferik+karakter parça + 22 VERBS yükleme cümleleri) + WORLDRESETDIALOG (herkes öldü/dirilmek için ele geçir) + WXPLOBBYPANEL tam (Demirhane/Boğaz maç sonu paneli) + WXP_DETAILS başlangıcı | ✅ |
| `0784` | 39 | WXP_DETAILS sonu (LAB_MILESTONE: Timsahkomutanlar/Horultaplumbağalar/Yabansavaşçısı/Gergedankardeşler) + Quagmire milestones + XB1_USER_DIALOG (Xbox kontrolcü) + **XPUTILS** = **UI SON BATCH — FAZ 2 %100 TAMAM** ✅ | ✅ |

---

## Faz 3 — STRINGS.ACTIONS + küçük lore blokları (devam ediyor)

### ✅ Oturum 5 — 2026-04-28 (8 batch / 609 string)

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0001` | 200 | STRINGS.ACTIONS başlangıcı (A-G): Saldır/İncele/Kuşan/İnşa Et/Hücum Et/Ele Geçir + tüm CASTAOE büyüleri (Lava Arena/Maxwell/Wathgrithr) + DEPLOY/DROP/EAT/EQUIP + GIVE.QUAGMIRE_ALTAR pun (Snackrifice → Atıştırmalık Adak) | ✅ |
| `0002` | 200 | STRINGS.ACTIONS devamı (G-T): GIVE/HAMMER/HARVEST/HAUNT/HEAL/INVESTIGATE/JUMPIN/LIFT/LOOKAT/Examine→İncele + OCEAN_FISHING tam + OPEN_CRAFTING (Şurada Döv/Sun/Heykel Yap) + Quagmire/Boat/Slaughter ironik kibar öldürme (Politely Butcher → Nazikçe Doğra) | ✅ |
| `0003` | 90 | STRINGS.ACTIONS sonu (T-Y): TAPTREE/TEACH/TELEPORT/TILL/UNLOCK/USEDOOR/USEITEMON tam + USESPELLBOOK + WEREFORM (Kunduz/Kaz) + WHISTLE Woby + WRAPBUNDLE/WRITE/YOTB | ✅ |
| `0004` | 7 | STRINGS.ANTIADDICTION (Çin bölgesi anti-bağımlılık uyarıları, saat sayacı) | ✅ |
| `0005` | 5 | STRINGS.ARCHIVE_RUNE_STATUE (Kadim Arşivler rün heykelleri Alter ilahileri) | ✅ |
| `0006` | 5 | STRINGS.ATRIUM_OVERGROWTH (Atriyum bitki örtüsü Shrouden ilahileri) | ✅ |
| `0007` | 80 | STRINGS.BALATRO (Klei cross-promo kart oyunu — Jimbo joker karakteri, 18 karakter joker özel etkisi, poker el türleri: Floş/Kare/Streyt) | ✅ |
| `0008` | 22 | STRINGS.BEEFALONAMING (Bızonsığır rastgele isim üreteci — Beef→Bızon portmanto: Annabızon/Toynakfrey/Sinderbızonella/Danavera) | ✅ |

**Faz 3 ilk dilim:** ACTIONS tam tamam (490 string), küçük lore blokları (124 string) → 609 string yeni.

### ✅ Oturum 6 — 2026-04-28 (27 batch / 161 string)

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0009-0028` | 75 | **STRINGS.BOARLORD** tam (Forge patron Pugna diyalogları): PLAYERDEATH_BANTER + PLAYERS_DEFEATED_BATTLECRY + ROUND1-7 START/FIGHT_BANTER/PLAYER_VICTORY/TRAILS_INTRO/BOARRIOR_INTRO. **Boarrior=Yabansavaşçı, Boarilla=Yabongoril, Battlemaster Pugna=Savaş Ustası Pugna, Gatekeepers=Geçit Bekçileri, Throne=Taht, Swineclops=Domuzgöz**. Pugna'nın 1. round kibirinden 7. round teslimiyetine dramatik yay korundu | ✅ |
| `0029` | 1 | STRINGS.BROKENITEM (Bozuk) | ✅ |
| `0030` | 72 | STRINGS.BUNNYMANNAMES (Tavşanadam rastgele isimleri — bilim/havuç/element temalı). Latin bilim isimleri olduğu gibi (Brassica/Bunium/Sium/Tragopogon/Ipomoea/Manihot/Mirabilis/Psoralea/Canna/Typha/Zingiber/Oxalis/Solanum/Ullucus/Cuperus/Apios/Lepidium/Microseris); günlük TR adlar çevrildi (Burdock=Dulavratotu, Carrot=Havuç, Celeriac=Kereviz, Parsnip=Yaban Havucu, Radish=Turp, Yam Daisy=Yam Papatyası); havuç çeşit özel adları olduğu gibi (Altrincham/Barwon/Nantes/Imperator vb.); lantanit element adları Türkçeye (Skandiyum/İtriyum/Lantan/Seryum/Praseodimyum/Neodimyum/Prometyum/Samaryum/Evropyum/Gadolinyum/Terbiyum/Disprozyum/Holmiyum/Erbiyum/Tulyum/İterbiyum/Lutesyum) | ✅ |
| `0031` | 3 | STRINGS.CARNIVAL_CROWKID_ACCEPTGIFT (Karganaval Karga Veleti hediye kabul) | ✅ |
| `0032` | 6 | STRINGS.CARNIVAL_CROWKID_CAMPFIRE (kamp ateşi diyalogları — "Cah-cah-cah" → "Gak-gak-gak", featherfree → tüysüz) | ✅ |
| `0033` | 5 | STRINGS.CARNIVAL_CROWKID_DECOR_AMBIENT_LOTS (dekorasyon dolu ambiyans) | ✅ |
| `0034` | 3 | STRINGS.CARNIVAL_CROWKID_DECOR_AMBIENT_LOTS_SNACK (atıştırmalık + Corvus karga ismi) | ✅ |
| `0035` | 6 | STRINGS.CARNIVAL_CROWKID_DECOR_AMBIENT_NONE (dekorsuz alaycı banter — "Caw-no-val" → "Karga-yok-val" pun) | ✅ |

**Faz 3 toplam:** Oturum 5 (609) + Oturum 6 (161) = 770 string. UI sonrası küçük blok temizliği devam ediyor.

### ✅ Oturum 7 — 2026-04-28 (24 batch / 103 string)

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0036-0049` | 52 | **CARNIVAL_CROWKID kalan tam** — DECOR_AMBIENT_NONE_SNACK/SOME/SOME_SNACK + DECOR_PLAYER_LOTS/LOTS_SNACK/NONE/NONE_SNACK/SOME/SOME_SNACK + GAME_GOTO + HASGIFT + OTHERGAME_GOTO + REFUSEGIFT + SCARED. Mini oyun adları: **Egg Scramble=Yumurta Telaşı, Hubbub for Grub=Yem için Yaygara**. "Featherfree creature=tüysüz mahluk" (Oturum 6 standart). "Squawck about creepy" → "Gak desem az gelir, ne ürpertici!" (karga sesi pun korundu). Karga veletlerinin meraklı/tembel/açgözlü kişiliği yansıdı | ✅ |
| `0050-0058` | 35 | **CARNIVAL_HOST tam** — Karganaval host'u **Corvus Goodfeather=Corvus İyitüy** (Latince Corvus karga cinsi korundu, Goodfeather=İyitüy yerelleştirildi). Showman tarzı abartılı sıfatlar (great/wondrous/spectacular → ulu/harikulade/muhteşem). "Last year was so profitable- er, FUN" Klei açgözlü tüccar kaçışı korundu. "Early bird gets the worm" → "Erken kalkan kuş solucanı kapar" (atasözü uyarlaması). Sistem-tarzı "siz" kullanımı (Hoş geldiniz, Jetonlarınızı alın) | ✅ |
| `0059` | 16 | **STRINGS.CAST** — Atriyum sahne oyunu rolleri: Zanaatkâr/Demirci/Oyuncak Bebek/Kırık Bebek/Paramparça Bebek/Elytra/Joker/Akılsız/Kral/Ayna/Prenses/Kraliçe/Bilge/Yağcı/Ağaç/Görücü. Klei kasıtlı ironi: DOLL_REPAIRED key=Shattered (yenilenmiş ama paramparça — Charlie lore). Elytra Latin böcek terimi olduğu gibi korundu | ✅ |

**Faz 3 toplam:** Oturum 5 (609) + Oturum 6 (161) + Oturum 7 (103) = 873 string.

### ✅ Oturum 8 — 2026-04-28 (10 batch / 444 string) — SEÇENEK B YOLA ÇIKILDI

**Aydın'ın kararı:** Seçenek B (item öncelikli) — CHARACTERS uzun bloğu (0060-0373) atlandı, item-related bloklara geçildi.

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0374` | 19 | **STRINGS.CHARACTER_ABOUTME** — 19 karakter hakkında 1 cümle özet (3. tekil anlatıcı; "Wilson hakikaten bir bilim insanı..."). Karakter persona'sı GEREKMEZ — narator anlatımı | ✅ |
| `0375` | 112 | **STRINGS.CHARACTER_BIOS** — Doğum günü tarihleri (TR formata: "31 Mart"), En sevdiği yemek, uzun lore paragrafları (Walter Constant'a düşüşü, Wanda zaman çatlağı, Warly Maman, Wigfrid Valkyrie rolü, Maxwell Codex Umbra, Webber giriş hikayesi, Wendy Abigail, Wes mim trajikomedi, Wickerbottom librarian-spy, Willow Bernie+ateş, Wilson radyo+makine, Winona Charlie arayışı, Wolfgang sirk, Woodie kuzeyli sakal+Lucy+were-formlar, Wormwood lunar köken, Wortox Krampus dostluğu, Wurt küçük Merm, WX-78 binary "too late"). 16 karakter × 3-4 alan | ✅ |
| `0376` | 22 | **STRINGS.CHARACTER_DESCRIPTIONS** — bullet list "perks & quirks". Werebeaver=Kunduzkurt, Weremoose=Kurttos, Weregoose=Kurtkaz | ✅ |
| `0377` | 7 | **STRINGS.CHARACTER_DETAILS** — UI etiketleri: "Yetenekler ve Tuhaflıklar", "Söz", "Eli boş", "Constant'a Girerken Yanında", "Hayatta Kalma Şansı", "Animasyon Filmi Oynat" | ✅ |
| `0378` | 21 | **STRINGS.CHARACTER_NAMES** — 17 karakter özel isimleri korundu (Wilson P. Higgsbury, Bayan Wickerbottom, vb.); Random=Rastgele, Unknown=Bilinmeyen | ✅ |
| `0379` | 20 | **STRINGS.CHARACTER_QUOTES** — Karakter alıntıları, KISMİ persona: Wigfrid umlaut "Tüm dünyä bir sahnedir. Bänim için!", WX-78 BÜYÜK HARF "EMPATİ MODÜLÜ YANIT VERMİYOR", Wurt yarım Türkçe "Mermler ko-nu-kse-verlikleriyle ünlü", Wonkey "Uuk UUK!" | ✅ |
| `0380` | 21 | **STRINGS.CHARACTER_SURVIVABILITY** — risk seviyesi: Slim=Düşük, Grim=Vahim, None=Yok, Unknown=Bilinmiyor | ✅ |
| `0381` | 19 | **STRINGS.CHARACTER_TITLES** — Karakter unvanları: Korkusuz/Zaman Bekçisi/Aşçı/Performans Sanatçısı/Kuklacı/Hazmedilmez/Yaslı/Sessiz/Kütüphaneci/Ateş Uşağı/Centilmen Bilim İnsanı/Tamirci Hanım/Güçlü Adam/Lanetli/Oduncu/Yalnız/Ruh Aç/Mini Mini/Ruhsuz Otomaton | ✅ |
| `0382` | 3 | **STRINGS.COOKINGRECIPECARD_DESC** — 3 placeholder (yer tutucu) format string | ✅ |
| `0578` | 200 | **STRINGS.NAMES (1/15) BAŞLANGIÇ** — A-B item isimleri: Abigail/Karıncaaslanı/Bızonsığır/Yarasalisk/Mekanik Şah/Arıların Kraliçesi/Ayıger... 30+ yeni item glossary terimi (Birchnut=Huşfındığı, Sproutrock=Filiztaşı, Brightshade=Aydıngölge, Werebeaver=Kunduzkurt). Atriyum lore (Sequitor, Ancient Sentrypede), W.A.R.B.I.S./Forge BEETLETAUR=Cehennemi Domuzgöz | ✅ |

**Faz 3 toplam:** Oturum 5+6+7+8 = 873 + 444 = **1.317 string** (Faz 3'ün ~%26'sı tahmini)

## 🎯 Sıradaki Oturum (9) — Yol Haritası (Seçenek B devam)

### NAMES devam: 14 batch daha (~2.600 string, ~5-7 oturum)
- `0579` STRINGS.NAMES (B-C) — BLOWDART_LAVA sonrası
- `0580` STRINGS.NAMES (C-D)
- `0581` STRINGS.NAMES
- `0582-0592` STRINGS.NAMES devam (toplam 14 batch kaldı, her biri ~200 string)

### NAMES sonrası
- `0593` STRINGS.NAME_DETAIL_EXTENTION (1 batch, ek detay)
- `0594` STRINGS.NIGHTMARE_OVERGROWTH (1 batch, lore)
- `0595` STRINGS.PIGNAMES (1 batch, domuz isimleri)
- `0596-0631` PIG_* talkers (PIG_GUARD/PIG_TALK_*)
- `0632` STRINGS.PLAYING_CARD_NAMES (Balatro)
- `0633` STRINGS.PLAYS (Stage Play repertoire)
- `0635` STRINGS.PYROMANCY (Willow ateş büyüleri)
- `0636-0639` STRINGS.QUAGMIRE_* (Boğaz lore)
- `0650-0654` **STRINGS.RECIPE_DESC** (5 batch, ~956 tarif açıklaması) ⭐⭐
- `0655-0658` STRINGS.SCRAPBOOK (Faz 4)
- `0659-0683` SELECT/SET/SHADOW/SHARD/SHARKBOI/SIGNS/SKILLTREE bloklar
- `0684-0723` SKIN_DESCRIPTIONS + SKIN_NAMES (Faz 6)
- `0733-0736` STAGEACTOR (Faz 4)

### Faz 5 (CHARACTERS) sonra dönülecek
Item glossary tamamlandığında batch_0060'a dönüp 17 karakter speech çevirisine başla. Persona disiplini için `docs/character-voices.md` zorunlu.

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

### 2. Sıradaki batch'i çevir (Faz 3 başlıyor)
```bash
# Read — batch_0001..0760 arası NAMES/RECIPE_DESC/INV_DESC/COOKBOOK/PLANTREGISTRY
pipeline/batches/pending/batch_0001.json     # ← Faz 3 başlangıcı (NAMES item isimleri)

# Write (çevirisi yapılmış halde)
pipeline/batches/done/batch_0001.json
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

## 🗂️ Faz 2 ✅ tamamlandı (2026-04-28)

**Yapılan iş özeti (Oturum 1-4):**
- 4.439 string PO'da, 26 batch JSON done/ altında (priority + 0762-0784)
- Mod DST'de çalışıyor (mağarada da çalışıyor — hibrit AddSimPostInit + AddPlayerPostInit)
- Validate temiz: 0 hata, 0 boş msgstr, 70 false-positive glossary uyarısı
- DST mods/ klasörüne sync edildi

**Faz 2 nihai kapsam (in-game tam Türkçe):**
- Ana menü, Yeni Dünya Kurma, AYARLAR (tooltip'ler dahil), Mod yönetim, Sunucu lobi, Yükleme ekranları, Vefat ilanları, HUD, hata mesajları (50+), 35 emoji, yemek tipleri
- **Oturum 4 yenilikleri:** Sandbox menüsü tam, SaveLoad, Karalama Defteri, Server Admin (yasak/snapshot), Server Creation tam (4 playstyle/cave/preset/UGC), Server Listing tam (filtre/world progression tags), Süs Dolabı, Maceraya Kapı, Lunar/Shadow Rift'ler, Teleportato, Takas Hanı tam (Karganaval/Yavrukoon/Gölge Tüccar/Tüm mini oyunlar), Gardırop, Dünya Üretim cümleleri (45 isim+22 fiil), Dünya Sıfırlama, Demirhane/Boğaz Maç Sonu Paneli (TP sistem), Xbox kontrolcü diyalogları

**Sıradaki: Faz 3 — item çevirisi (~5.000 string)**
- `STRINGS.NAMES` (~1.500 item ismi) — en görünür kısım, glossary disiplini kritik
- `STRINGS.RECIPE_DESC` (~956)
- `STRINGS.INV_DESC` (envanter hover açıklamaları)
- `STRINGS.COOKBOOK` (yemek kitabı tarifleri)
- `STRINGS.PLANTREGISTRY` (Wickerbottom -W bitki kayıt)
- Strateji: Glossary'yi item-bazlı genişlet (~500 hedef), 2 tur insan QA
- Tahmini: ~25 batch, 4-5 oturum
