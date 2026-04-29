# DST Türkçe Yama — Çeviri İlerlemesi

> Bu dosya her çeviri oturumu sonu güncellenir. Aydın'ın "ne çevirildi, ne kaldı" görmesi + sonraki oturumdaki Claude için referans.

**Toplam hedef:** 85.706 msgid / 970 batch
**Son güncelleme:** 2026-04-29 (Oturum 16 ✅ — **PIG_TALK serisi TAMAMLANDI** ⭐ 36/36 batch + RABBIT serisi tam — 41 batch / 136 string)

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

**Şu ana kadar çevrilen toplam:** 9.755 / 85.706 msgid (%11.38)

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

### ✅ Oturum 9 — 2026-04-28 (3 batch / 600 string) — STRINGS.NAMES B-F

**Aydın'ın "devam" komutu:** Seçenek B devam — 3 NAMES batch (B-F arası ~600 item ismi).

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0579` | 200 | **STRINGS.NAMES (2/15)** B-C: BLOWDART_LAVA2→Erimiş Oklar, Blueprint→Plan, Boards→Tahta, **Boarrior→Büyük Demirhane Yabansavaşçısı**, **Nautopilot→Denizotopilot** (deniz+otopilot pun), Marotter Raft→Denisamur Salı, Bone Bouillon→Kemik Bulyonu, **Lunar Grimoire→Ay Büyü Kitabı**, **Volatile Canary→Patlayıcı Kanarya**, Cawnival/Karganaval mini oyun seti tam (Yumurta Telaşı/Yem için Yaygara/Sepetteki Yumurtalar/Kuş Yuvası Top Bırakma/Yuva Bekçisi/Guguklu Çark), Carnival Vest→Cıvıl Cıvıl Atkı/Pelerin/Pelerincik, **Carrat→Havufare**, **Catcoon→Kedikoon** | ✅ |
| `0580` | 200 | **STRINGS.NAMES (3/15)** C-C: Cave Banana→Mağara Muzu, Sinkhole→Obruk, **Geothermite→Jeotakar** (geothermal+mite), Fumarole→Volkan Bacası, **Charlie's Beckoning Hand→Çağıran El**, Mockingbird→Alaycı Kuş, Playbill→Oyun Afişi, **Kingly Figure→Kral Heykelciği**, Queenly→Kraliçe, Pawn→Piyon, Rook→Kale, **Knight→At** (satranç), **Hornucopia→Boynuzkopya** (cornucopia pun), Frostjaw→Buzçene, **Possessed Varg→Ele Geçirilmiş Varg**, Celestial Scion→Semavi Veliaht, Great Depths Worm→Büyük Derinlik Solucanı, **Cookie Cutter→Bisküvi Kesici**, Dragon Fruit→Ejderha Meyvesi, Bunch o' Stone→Tomar Taş, Crab Knight→Yengeç Şövalyesi, Yolnumarası heykelcikler (YOTH/YOTS/YOTD) | ✅ |
| `0581` | 200 | **STRINGS.NAMES (4/15)** C-F: Critter (yavru evciller) tam: Broodling→Yavruşa, Friendly Peeper→Sevimli Gözcü, Kittykit→Kedicik, Ewelet→Kuzucuk, Mothling→Güveşa, Vargling→Yavruvarg, **Cookie Crumbles→Kurabiye Kırıntıları**, **Dreadstone→Korkutaş**, **Dragonfly→Yusufçuk**, Dragonpie→Ejderha Pastası, **Houndius Shootius→Houndius Shootius** (özel, korunur), **Toma Root→Domarot** (Klei pun, doma+rot), **Garden Digamajig→Bahçe Kazgereci** (dig+thingamajig), **Bucket-o-poop→Kakaş Kovası**, **T.I.N.G.L.E. Düğümü** (akronim korunur), **Ice Flingomatic→Buz Fırlatomatik** (fling+omatic pun), **Figatoni→İncironi**, **Figkabab→İncirkebap**, Anenemy Trap→Düşmanavar Tuzağı, Werepig figürünleri tam, **Eyebrella→Gözlemsiye**, Picnic Casket→Piknik Tabutu, Lucky Beast→Şanslı Canavar (YOTH dragon dance kostümü) | ✅ |

**Faz 3 toplam:** Oturum 5+6+7+8+9 = 873 + 444 + 600 = **1.917 string** (Faz 3'ün ~%38'i tahmini)

### ✅ Oturum 10 — 2026-04-28 (3 batch / 600 string) — STRINGS.NAMES F-M

**Aydın'ın "devam" komutu:** Seçenek B devam — 3 NAMES batch (F-M arası ~600 item ismi).

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0582` | 200 | **STRINGS.NAMES (5/15)** F-H: Çiğ Balık/Balık Bifteği/Balık Pastırması, Çiçek/Solmuş Çiçek serisi, **Forget-Me-Lots→Unutma-Beni-ler** (Klei multiplicity pun), **Asparagazpacho→Kuşkonmazpacho**, **Icker→Yapışkak** (Atriyum jel), **Saladmander→Salatamender** (glossary), **Mourning Glory→Yas Çiçeği**, Ghostly Elixir serisi tam (Vigor Mortis Latince korunur), Halloween 14 şeker + 9 iksir + 6 deney + 6 süs + 4 zırh, **Ham Bat→Jambon Sopa**, Briar Wolf→Çalı Kurdu, **Crabby Hermit→Huysuz Münzevi** (Pearl), Pearl ekosistemi başlangıcı (Çay Dükkanı/Kaplıca/Çay tarifleri) | ✅ |
| `0583` | 200 | **STRINGS.NAMES (6/15)** H-L: Hermit/Pearl tam (Bohça/Sallanır Sandalye/İnci/Yer), Hot Spring, **Howlitzer→Ulutop** (howl+howitzer pun), **Long Pig→Uzun Domuz** (kanibalist eufemizm), Hutch (özel), Buz/Buz Sandığı/Buz Asası, **Inspectacles→İnceleme Gözlüğü** (inspect+spectacles pun), Ipekak Şurubu, **Mimicreep→Sinsimimik**, Kitcoon Nursery+9 biyom Yavrukoon, Klaus+Pascal/Desdemona/Fermin/Warren (4 atlı, özel), KNOWN_*_SEEDS 15 tohum (Domarot/Şalgam dahil), Koalafant, Krampus, **Lavaarena Forge zırh seti tam** (~25 zırh/silah/miğfer; Steadfast/Silken/Jagged tonlamaları), Lavae/Lava lore, **Treeguard→Ağaçmuhafız**, **Crustashine→Kabukparlak**, Volt Goat=Şimşek Keçisi, Lucy the Axe→Balta Lucy, Bright-Eyed Frog, **Brightshade Helm→Aydıngölge Miğfer**, **Ryftstal→Yarkristal** (rift+crystal), **Lunaform Burst→Aybiçim Patlaması**, Deadly Brightshade=Ölümcül Aydıngölge | ✅ |
| `0584` | 200 | **STRINGS.NAMES (7/15)** L-M: **Brightsmithy→Aydındemirhane** (lunar forge), Tuzakbitki, Lutefisk (İskandinav), Mad Scientist Lab, Malbatross→Malbatros tam, **Mandrake→Adamotu** (klasik), Marble (mermer) serisi tam, **Stage play maske seti tam** (Visionist/Elytra/Artificer/Halfwit/Sage/Toady + 8 karakter maskesi), Mast (gemi direği)+Lightning Conductor+Winged Sail+Dragonfly Wing Mast, Maxwell tam (Kafa/Işık/Anahtar/Kabus Kilidi/Gramofon/Taht), **Merm ekosistemi tam** (Mermhane=Armermry, **Florpkale=Flort-ifications** Wurt florp+fortifications pun, Kraftsmerm=Craftsmerm, Lunar/Shadow Merm, Royal-In-Progress, Slightly Less Shoddy Tool=Klei dark humor), Miasma=Miyazma, Friend-O-Matic→Dost-O-Matik, Milky Whites=Sütlü Beyazlar, **Moggles→Köstgözlük** (mole+goggles), Splumonkey ekosistemi (Pirate Bandana, Kaptan Üç Köşeli Şapka, Moon Quay), Moon items derinlik (Moonglass=Aycam, Moonrock=Aykayası, Celestial Altar=Semavi Sunak/Sanctum=Mabet/Tribute=Sunu serisi tam, **Astroggles→Astrgözlük**, **Moongleam→Aypırıltı**), Moose1/2=Tos/Kaz (glossary), Moqueca | ✅ |

**Faz 3 toplam:** Oturum 5+6+7+8+9+10 = 1.917 + 600 = **2.517 string** (Faz 3'ün ~%50'si tahmini)

### ✅ Oturum 11 — 2026-04-28 (3 batch / 600 string) — STRINGS.NAMES M-S

**Aydın'ın "devam" komutu:** Seçenek B devam — 3 NAMES batch (M-S arası ~600 item ismi).

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0585` | 200 | **STRINGS.NAMES (8/15)** M-P: Sivrisinek seti tam (Skeeter Bomb=Sivrisinek Bombası, **Fertilizzzer=Vızılgübre** zzz vızıltı pun, Blood Shot=Kan Şotu Merm tonik), **Mosling=Tosçuk** (Moose=Tos+küçültme), Sıcak Punç, **Portal Paraphernalia=Geçit Pılı Pırtısı** (P-P alliterasyon), Mantar serisi tam (**Boomshroom=Patmantar**, **Funcap=Şenşapka**, **Glowcap=Parlakşapka**, Mushlight=Mantarışığı, Mushtree=Mantarağaç 4 renk), Mutated Bearger/Bird/Buzzard/Deerclops/Hound/Pengull tam, **Switcherdoodle=Karıştırgıç** (mutator yumurta seti 7 tip; -gıç eki Türkçe), **Permafrost Pengull=Buzul Pengul**, Karabasan serisi tam (Nightmarebeak=Karabasangaga, Karabasan Yakıtı/Sur/Işık/Tılsım), **Grim Galette=Vahim Galette** (Fransızca korunur), Thulesit Madalyon, **Sabah Yıldızı** (Morning Star silah), Kara Kılıç, Karanlık, **Güherçile** (Nitre), Kum Püskürtücü/Öğütücü (Brightsmithy boss silahı), **Premier Gardeneer Hat=Mükemmel Bahçemühendis Şapkası** (gardener+engineer pun), Ocean fishing tam (8 şamandıra+8 yem+5 spinnerbait+4 spoon), Ocean fish 18 tür (**Antchovy=Karıncamsi**, **Sweetish Fish=Tatlısveç Balığı**, **Popperfish=Patbalığı**, **Fallounder=Sonbalkan**, Spittlefish=Tükürük Balığı, Bloomfin Tuna=Çiçekyüzgeçli Tuna), **Terrorclaw=Dehşetpençe** (Atriyum boss), **Knobbly Tree=Tümsekli Ağaç**, Above-Average Tree Trunk=Ortalama Üstü Ağaç Gövdesi (Klei klişe), Ortak Yosun Tabağı (Wurt offering pot), Soğan, **Yanardöner Cevher** (opal), **Tembel Toplayıcı/Kaşif**, **Ay Çağırıcısı'nın Asası**, **Palmcone=Palmiyekozak** seti, **Scorpeon=Akrepon**, **Stuffed Pepper Poppers=Doldurulmuş Patbiberler**, Yutkun seti, Mantı (Pierogi glossary tutarlı), **Aydıngölge Çekici** (Brightshade Smasher), Salamura Ringa, Pig Elite 4 isim (Wade/Ignatius/Dmitri/Sawyer korunur), Domuz seti tam | ✅ |
| `0586` | 200 | **STRINGS.NAMES (9/15)** P-Q: **Domuzların Kralı** (glossary), Domuz Adam/Tapıncağı/Postu/Meşalesi, **Clout Snout=Yumruk Burun** (Pig King para), Altın Kemer, Çam Kozalağı/Fidanı, Ay Quay Korsan Sancağı, Yaba (Pitchfork), Yapraklı Et (Wormwood), Bahçemühendis Şapkası, Mahsul/Vahşi Mahsul, **4 Playbill (Stage play)**: Büyülü Bebek, Dört Şövalyem ve Ben (YOTH), Bir Görev Tamamlandı (Maxwell itirafı), **Kasvet Örtüsü=The Pall**, **Inthralled Corpse=Boyun Eğdirilmiş Ceset**, **Deadelgänger=Ölüdoppelgänger** (Klei dead+doppelgänger pun), Wanda saat seti tam (**Backtrek/Backstep/Ageless/Rift/Second Chance/Alarming Clock=Korkutucu Çalar Saat**), Polonya Kurabiyeleri, **Polly Roger** (özel; Jolly Roger pun), Nar serisi tam, Gölet/Yılanbalığı/Tatlı Su Balığı/Su Yosunu, Gübre, Taşınabilir 5 alet (Öğütme Değirmeni/Tencere/Kamp Ateşi/Baharat İstasyonu/Çadır), Patates serisi tam (**Şık Sarmal Yumrular** Klei eufemizm), **Powdercake=Barut Pastası** (Klei dark humor), **Powder Monkey=Barut Maymunu**, **Waterfowl Can=Su Kuşu Sulayıcısı**, **Prime Mate=Birinci Maymun** (primate+first mate Klei pun), **Puffin=Deniz Papağanı**, Bal Kabağı serisi tam, **Bright Boxer/Shadow Boxer** punching bag, Saf Parıltı, Karabasan Tılsımı, Mor Cevher, **Kemiren'in Sunağı** (Quagmire), **Quagmire 70 yemek tarifi tam** (Lazanya, Pizza, Köri, Spagetti, Hamburger, Ratatuy, Bruskette, Mantı, Cheesecake, Et Wellington, Yengeç Ravyoli vb.), Yengeç Tuzağı, **Annecik=Mumsy** (anne keçi), Billy (oğlak özel), Keçi Sütü | ✅ |
| `0587` | 200 | **STRINGS.NAMES (10/15)** Q-S: Quagmire kalan tam (Bog Merm=Bataklık Merm, **Sammy/Pipton** Lucid/Cognizant, Sokak Lambası, Demir Çit, **Kemiren Tapıcısı**, Salmon=Somon, Tuz seti tam, Ağaç Sızıntı Kiti, **Sugarwood Tree=Şekerağacı**, Spotty Shrub=Benekli Çalı, Domarot tutarlı, **Şalgam**, Buğday, Slaughter Tools=Kesim Aletleri), Tavşan ekosistemi tam (**Warren Wreath=Tavşanyuva Çelengi** YOTR pun, Tavşan Kafesi, **Burrowing Horn=Kazıcı Boynuz**, **Rabbit King 3 form**: Wrathful=Öfkeli/Fortuitous=Rastlantısal/Benevolent=İyiliksever, Royal Rabbit Enforcer=Kraliyet Tavşan İcra Memuru), **Short Circuit=Kısa Devre** (RAIN Klei pun!), Yağmurluk/Şapka/Ölçer, Plak (Record), Kırmızı Cevher/Fener/Aymerceği/Kese/Şapka/Mantar/Şenşapka, Sazlık, **Yaz Yeleği=Summer Frest**, **Eserkalı=Relic**, **Bilim Makinesi/Simya Motoru/Gölge Manipülatörü**, **Prestihatitator=Şapksihirbaz** (prestidigitator+hat pun!), Clean Sweeper=Temiz Süpürge (skin tool), Et Heykel + Diriliş Taşı (glossary), **Resurrection Sickness=Diriliş Hastalığı**, **Yürek Tılsımı**, **Gergedankardeş Snapback/Düz Vizör**, Kavrulmuş Hindi, **Kızılkuş/Karkuşu**, **Demirzırhlı Kostüm Deseni**, Rocks/Boulder/Mini Glacier/Lava Pit serisi, **Stone Fruit=Taş Meyve** (Avocado bush) tam, **Mekanik Kale=Clockwork Rook**, Halat, **Mağaracı Köprü Kiti**, **Pembe Gözlükler=Rose-Colored Glasses** (klişe deyim), Çürük Yumurta, Arı Sütü, Moloz, **Thulesit Tacı/Sopası**, **Pusuda Karabasan/Dinlenmiş Dehşet** (Ruins shadeling), Kadim Sandık, Eyer 6 tip tam (**Glossamer=Yaldız Eyeri**), Taze Salsa, **Tuz Yalağı=Salt Lick**, **Salty Dog=Tuzlu Köpek** (eski denizci argosu), Kumdan Kale, Kum Sivrisi (Antlion) | ✅ |

**Faz 3 toplam:** Oturum 5+6+7+8+9+10+11 = 2.517 + 600 = **3.117 string** (Faz 3'ün ~%62'si tahmini)

### ✅ Oturum 12 — 2026-04-29 (5 batch / 802 string) — STRINGS.NAMES TAMAMLANDI! ⭐

**Aydın'ın "devam 5 batch oturum iş yap" komutu:** Seçenek B son sprint — 5 NAMES batch ile NAMES tamamen bitti.

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0588` | 200 | **STRINGS.NAMES (11/15)** S başlangıcı: Fidan, **Hurdacı Şapauldron** (chapeau+pauldron+scrappy WX-78 hat pun), **Ufuk Genişletici** (Wagstaff monocle), **Kıvılcım Kasası** (security pulse cage; alliterasyon), **Tohum Paket-le** (-le ek), **Gözcübekçi=Ocuvigil** (oculus+vigil sentry pun), **Sadık Bant** (Winona iletişim), **Shadow ekosistemi tam** (Gölge Dansçı/Kazıcı/Düellocu/Oduncu/Madenci, Gölge Atriyum, Şah/At/Kale satranç tutarlı, Gölge Tokmak=Shadow Maul, Bızonsığır Kasvet Çanı, Gölge Sanat Kaidesi=Shadowcraft Plinth, Asalak Gölgecik), **Karabasan Köleler tam** (Mega Yıkım/Mürekkep Yıkımı + Allegiance: Dalga/Titrek/Hırıltı/Sırıtış/Çığlık + Boşluk Maskesi=Void Masque, **Tenebrau Müjdecisi** Latince), **Kayaçene=Rockjaw** (Frostjaw paralel), **Kabukörgücü=Combriner** (Wurt shellweaver), **Maskaralık=Shenanigans** (Maxwell), **Slingshot ekosistemi tam** (Walter ana silah; **Sadık Sapan**, 18 mermi türü: **Cıvıkışlar=Ickies/Patlamalar=Kablooies/İğneli Zıngırlar=Stinger Zingers/Ay Atışları=Moonshots** Klei pun, 4 lastik + 4 çerçeve + 4 tutamak konfig sistemi), **Salyangurp=Slurtle/Sarsalyo=Snurtle/Kabukmiğfer=Shelmet** (kabuk pun seti), **Cıvılcuk=Pipspook** (pip+spook küçük hayalet), **Küçük Geştalt** (Almanca lunar), **Koyuncuk=Ewecus** (ewe+mucus pun), **Özlü Kargı=Pith Pike** (pith+pike alliterasyon), **Sarmal Mızrak/Battle Spear/Elding Spear** (Wigfrid Old Norse), **Spider seti tam** (Hemşire Örümcek/Mağara/Tükürükçü/Sallanan Derinlik/Paramparça/Deniz Yürüyücü/Ağsı Düdük), **Tıngır Mürekkep=Skittersquid**, **Hava Sancısı=Weather Pain** (Wickerbottom asası), Spore tam 5 renk | ✅ |
| `0589` | 200 | **STRINGS.NAMES (12/15)** S sonu + T: **Diriltilmiş İskelet=Reanimated Skeleton** (Stalker), **Kadim Yakıtdokur=Ancient Fuelweaver** (Atriyum boss glossary), **Dokunmuş Gölge=Woven Shadow**, Korsan Haritası, Glommer/Arp/Maxwell heykelleri, **W.O.B.O.T.** (Walter köpek robot akronim), Patlıcan Dolması, Sukulent 4 form, Batık Sandık, **Göz Alıcı Olta Kutusu=Spectackler Box** (spectacle+tackle pun), Destek Sütunu seti tam (Korkutaş Sütunu Atriyum), **Deniz ve Kara=Surf 'n' Turf**, Şık Yelek/Esintili/Şişme Yelek, **Aydıngölge Kılıç=Brightshade Sword** (lunar boss silah), Kış Şöleni Masası, **Şekerleme Çuvalı=Napsack** (nap+knapsack), **Trusty Slingshot=Sadık Sapan**, Olta Kutusu/Reklamı/Kabı, **Uzunkuş seti tam** (Tallbird/Egg/Yuva/Smallish=Ufaklık), Tamales, **Telekonum Odağı/Asası=Telebase/Telestaff**, **Teleportato 5 parça** (Tahta Şey/Kutu/Krank/Metal Patates/Halka Şey Klei nonsense), Tentacle (Dokunaç/Diken/Lekeleri/Yavru), **Gözalıcı Sandık=Conspicuous Chest** (Terrarium dropper), **Dehşetgaga=Terrorbeak**, **Thulesit Böcek Ağı**, **Gölge Buhurdanı=Shadow Thurible** (Wendy summon), **Biletkoon=Ticoon** (ticket+raccoon pun), **Çapaotları=Tillweeds**, **Toadstool tam** (Mantarkurbağa+Çile), **Domarot tam** (Toma Root/Roasted/Giant tutarlı), Silindir Şapka/Sihirbazın Silindiri, Meşale/Hortum/Tourtiere, **Tembel Asker Kaçağı=The Lazy Deserter** (Klei pun), **Yabongoril=Boarilla** (glossary), **Elektrikli Cızır=Electrical Doodad** (transistor), **Düşmanavar=Anenemy** (glossary), **Maxwell'in Diş Tuzağı**, **Ağaç Reçeli=Tree Jam** (Wormwood), **Kayalık Dal=Boulderbough** (boulder+bough pun, Atriyum tree rock), **Tisli Trident=Strident Trident** (alliterasyon T-T), **Trinket 1-46 tam** (kitsch koleksiyonlar: Erimiş Bilye/Cinciket=Gnomette/Hava Bayatlatıcı=Air Unfreshener Klei dark humor/Truva Atı Oyuncağı/Beyaz-Siyah Şah/Kale/At satranç çiftleri/Gord Düğümü), **Balık Tartı-Matik=Fish Scale-O-Matic** (scale çift anlam pun), **Yuvarlanan Ot=Tumbleweed** (glossary), **Toprak Sıkıştırıcı=Terra Firma Tamper** (Latin), 23 Turf tipi (Guano/Damalı/Tuğla/Altın/Yaprak Döken/Pullu Döşeme/Mantar/Krater/Mozaik 3 renk) | ✅ |
| `0590` | 200 | **STRINGS.NAMES (13/15)** Turf sonu + U + V + W başlangıcı: **Arnavut Kaldırımı=Cobblestones**, Kadim Döşeme/Karo/Tuğla İşi serisi (Ruins+Imitation), **Kadim Mabet Taş İşçiliği** (Sanctum=Mabet glossary), Mağara Volkan Bacası Çim, Hindi Yemeği, Şalgam (glossary), **Horultaplumbağa=Snortoise** (glossary), Çubuksu Ağaç tam, **Retinatraş=Retinazor + Spazmatizma=Spazmatism** (Terraria cross-promo bossları), Şemsiye/Unagi/Bilinmiyor, **Sanctum Vault tam** (Mabet Eserkalı/Replikalar 3 form/Avizesi/Uçurum=Chasm/Taşıma Küresi/Aysi Rün Taşı/Heykeli/Yol İşareti, **Şaşırtıcı Alev=Flummoxing Flame**), Kahvaltı Tavası/Sebze İğnesi/Viktoryen Kostüm, **Voidcloth Maxwell zırhı tam** (Kara Paçavralar=Dark Tatters, **Boşluk Başlığı=Void Cowl**, **Karbumeranj=Gloomerang** Klei pun gloom+boomerang, Boşluk Tamir Kiti, **Gölge Orakçısı=Shadow Reaper** scythe, **Karemsiye=Umbralla** Klei pun umbra+brella), **Şimşek Keçisi Chaud-Froid** (Fransız mutfak Warly), Vafıl, **W.A.R.B.O.T. patron tam** (Termalkilit Füzesi=Thermalock Missile, Üs/Parçalar/Bacak/Aydınlanmış formu, Açıklanmamış Yapı), **Wagdrone seti** (Karasırrı Bariyer=Terramite, **Şakırdak=Warbler**, Jiroskopik Çekirdek, Karasırrı yer drone), **Wagpunk seti tam** (Otomekanikçi=Auto-Mat-O-Chanic, **W.A.R.B.I.S. Baş Donanımı** akronim, Hurda, Kinetoklasmik Alan Genişletici, Altyapı Tahminleyicisi, Dayanaksal Seçici, Kavramsal Üretici=Notional Fabricator), **Wagstaff seti tam** (5 araştırma notu, **Cızırtılı Yayın=Grainy Transmission** 5 entry, 5 alet teknobabel: Birleştirici Tampon/Widget Düzeltici/Grommet İşaretleyici/Kavramsal Temizleyici/Kalibre Edilmiş Algılayıcı + 5 layman: Tuhaf/Garip/Acayip/Komik/Acayip Alet), Plank/Antika/Pullu, **Walls 9 tip tam** (Korkutaş/Saman/Ay Kayası/Thulesit+Arşiv/Hurda/Taş+Arşiv/Tahta), MacTusk (özel)/Tam Şapkası (glossary)/Mors Kampı/Dişi, Walter+Çamağacı Öncüsü, Wanda, **Tuhaf Bızonsığır=Odd Beefalo + Gezgin Tüccar=Wandering Trader** (Beefalo formunda gizli tüccar), Gardırop, Varg/Yavruvarg/Tapıncak, Warly, Savaşçı Kostüm Deseni, Katil Arı Kovanı, **Kısa Devre=Short Circuit** (RAIN glossary), Su Balonu/Sulama Kabı, **Karpuz seti tam** (Moda Karpuz/Karpuzlu Buz/Izgara/Devasa), Su Yosunu/Deniz Filizi/**Tohum Kabuğu=Seedshell** Klei pun, Yangın Pompası, Yüce Ağaç Gövdesi/Kökü, Deniz Kaplumbağası, Wigfrid+Savaş Miğferi/Komutan Miğferi/**Savaş Rönd** (Old Norse), **Wavey Jones** (Davey Jones pun), Yağlı Kağıt, Maxwell+**Codex Umbra** (Latin glossary), Webber+Kafatası+Yavru Örümcek, Ateş Isırganı/Unutma-Beni-ler/Dikenli Sarmaşık/Çapaotu, Wendy+**Daimi Sunak=Perennial Altar** (resurrection), **Were-item 3 put** (Ucuz Kunduz/Kaz/Tos Putu kitsch=ucuz), Wes/Wickerbottom/Willow+**Gökselce Köz=Ethereal Ember**/Wilson, **Cımbız Vinç=Pinchin' Winch** (alliterasyon Wickerbottom), Winona+G.E.M.eratör/Jeneratör/Mancınık/Kararsız İletim/**Cızbız=Doohickey + Mıkıcık=Gizmo** (Klei comic argosu)/Kalibre Algılayıcı/Pratik Kumanda/Spot Işığı | ✅ |
| `0591` | 200 | **STRINGS.NAMES (14/15)** WINONA sonu + Winter cooking tam + WX-78 modülleri tam + Y serisi: **W.I.N.bot** (Winona robot)/**Portasol** (portable+parasol)/Telenakil İstasyonu, **Winter cooking 21 tarif tam** (Şen Meyve Sosu=Merry Berrysauce, Bibingka Filipin, Lahana Sarması, Festival Balık Yemeği, Güzel Sos=Good Gravy, Latkes/Lutefisk/Sıcak Punç/Panettone/Pavlova, **Salamura Ringa=Pickled Herring** glossary, **Polonya Kurabiyeleri** glossary, Bal Kabağı Turtası, **Kavrulmuş Hindi** glossary, Tavuk İçi=Stuffing, Tatlı Patates Güveci, Tamales, Tourtiere), Kış Şapkası/Termal Ölçer, **Yılbaşı Neşesi=Holiday Cheer**, Tuğla Fırın, **9 Winter food: Zencefilli/Şekerli Kurabiye, Şeker Bastonu, Sonsuz Meyveli Kek, Çikolatalı Kütük Pasta, Erikli Puding, Elma Şarabı, Sıcak Kakao, Cennetlik Yumurta Likörü=Heavenly Eggnog**, Festival Süsü/Muhteşem/Şampiyon/Hoşnut Eden/Festival Işığı/Duygusal Süs (boss/forge/gorge varyantları), Kış Şöleni Ağacı/Festival Ağaç Saksısı, **Wobster ekosistemi tam** (Yuva/Ay/Ölü/Lezzetli; Klei lobster pun korunur), **Woby+Atıştırmalığı** (Walter köpek), Wolfgang+**Antrenör Düdüğü=Coaching Whistle**, Wonkey, Sert Tahta Şapka, Woodie, Dünya, **Derinlik Solucanı seti tam** (Worm/Hole/Sick Hole/Glow Berry=Parlak Meyve, Esrarengiz Bitki, Wormwood, **Büyük Derinlik Solucanı=Great Depths Worm** Atriyum boss, Toprak Höyük), **Wortox seti tam** (Decoy=Wortox?, **Kapçuval=Knabsack** Klei pun knab+knapsack, **Çift Kuyruklu Yürek=Twintailed Heart** reviver, Ruh/Ruh Kavanozu), Wurt+**Parlak/Korkunç Çamuratan=Brilliant/Dreaded Mudslinger** (lunar/shadow swamp item), **WX-78 24 modül devresi tam** (Fasulyepompa=Beanbooster, Soğutucu, Yeniden Sindirim, Termal, Aydınlatma+Süper, Dayanıklı=Hardy+Süper, **Gastronkazanç=Gastrogain** Klei pun gastric+gain+Süper, İşlem+Süper, Hızlandırıcı+Süper, **Korokutu=Chorusbox**, Optoelektronik, **Menzilpompa=Rangebooster**, **Sonik Çağırıcı=Sonic-Invoker**, Bloklama, Dönüş Devresi, **Yer Genişletici=Spatializer**, Elektriklendirme), Yedek Şasi 3 entry, **Taşınabilir Depo Ünitesi/Dönen Haritacı=Roto-Mapper/Zaptotom=Zaptrocuter+Kumandası**, **Besin Tuğlası=Nutribrick** WX-78 yiyecek, **Hayalet Aktarım Modülü=Spectral Transfer Module**, Katlanmış/Genişleyen Depo, Devre Çıkarıcı, Ele Geçirilmiş Şasi, **Biyo Tarayıcı=Bio Scanalyzer** (3 entry), **B.U.D.D.Y.** (Wickerbottom radyo akronim), **Sihirili Parıltı=Magiluminescence** (yellow amulet Klei portmanto), Sarı Cevher/Aymerceği, **Yıldız Çağırıcısı'nın Asası=Star Caller's Staff**, **YOTB Bızonsığır seti tam** (Tapıncak, 9 doll: Şanslı Canavar/Süslenmiş/Festival/Resmi/Donmuş/Çiçekli/Demirzırhlı/Viktoryen/Savaşçı, 3 desen parçası, Sahne, Dikiş Makinesi, Hakem Kabini), **YOTC Havufare seti tam** (4 spor salonu+kit, Kontrol/Bitiş/Başlangıç noktaları, Tartı, Tohum Paketi+Premium), **YOTD Yusufçuk seti** (Pençe Çapa/Kürek/Tekne Dümeni), **YOTH 10. yıl seti** (Salıncaklı Kısrak=Rocking Mare, Yaldızlı Şövalye Miğferi, Mekanik At Tapıncağı, **Şaka At=Shtick Horse** Yiddish pun, **Mızrak-Atılışı=Joust-a-Dash**), **YOTP Domuzların Kralı 3 yemek** (Sunak Kebabı, Sekiz Hazineli Çamur Pasta, Çubukta Balık Kafaları), **YOTR Tavşan 12. yıl** (Kısa/Uzun Tavşan Lambası, **Yastık Dövüşü Çukuru/Çanı/Kit**, **Tavşanadam Meşalesi**, Tavşan Rulosu/Ay Pastası/Ay Jeli/Şişlenmiş Puflar, Tavşanadam Tapıncağı, **Meydan Okuma Eldiveni=Glove of Challenge**), YOTS Yılan başlangıcı (**Jubilemfener=Jubilantern** Klei pun jubilation+lantern, Derinlik Solucanı Tapıncağı) | ✅ |
| `0592` | 2 | **STRINGS.NAMES (15/15) SON BATCH! ⭐** YOTS_WORM=Yaldızlı Derinlik Solucanı + Kedikoon Tapıncağı=Catcoon Shrine. **STRINGS.NAMES TAMAMEN BİTTİ — 2.802 item ismi tam** | ✅ |

**Faz 3 toplam:** Oturum 5+6+7+8+9+10+11+12 = 3.117 + 802 = **3.919 string** (Faz 3'ün ~%78'i tahmini, NAMES 15/15 ⭐)

### ✅ Oturum 13 — 2026-04-29 (11 batch / 286 string) — Küçük lore blokları temizlendi

**Aydın'ın "devam" komutu:** NAMES sonrası küçük lore + sahne oyunu + Quagmire blokları temizlendi.

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0593` | 20 | **STRINGS.NAME_DETAIL_EXTENTION** — Lavaarena Forge zırh stat detayları (Koruma %/Hareket Hızı %/Hızlı Bekleme %/Geri İtilme Direnci/Yoldaş Güçlendirici/Fiziksel-Sihir Hasar/Alınan-Verilen İyileştirme). 11 zırh + 8 şapka stat satırı | ✅ |
| `0594` | 5 | **STRINGS.NIGHTMARE_OVERGROWTH** — Atriyum karanlık ilahi 5 satır (gotik şiir, Maxwell-tarzı eski Türkçe: "Yüzünü çevirenin terk ettiği zavallılar... Karanlık bizim kalkanımız oldu. Geçimimiz. Tesellimiz.") | ✅ |
| `0595` | 146 | **STRINGS.PIGNAMES** tam — 79 Roma imparatoru (Augustus/Tiberius/Caligula/Nero/Vespasian/Titus/Trajan/Hadrian/Marcus/Commodus/Caracalla/Diocletian/Constantine/Justinian vs.) **özel isim korunur**, 20 Klei dev ekibi (Mickey/Cheeky Chris/Kevin/Ju-lian/Alia/Tatham/Brook/Matt/Alex/Kris/Kelly/Eugene/Graham/Jamie/Jeff/Joe/Corey/Bryce/Bug/Seth) korunur, 47 yemek/şirin domuz ismi (Hugo/Ay Pastası/Bagel/Bisküvi/Pastırma/Hamilton/Brownie/Tereyağ=Butters/Ton/Yonca/Krema/Mantı=Dumpling/Yumurtacık/Vafıl/Trüf/Patatesçik/Çedar/Bal Kabağı/Yulafçık/Hor Hor=Oinkey/Domuzlu Bao=Porkbun/Yumurtbert/Cips/Meyvecik/Huysuzcuk=Crabby/Arpa/Zeytin/Turşu/Kıvrılan=Wiggles/Pastırma/Kokuşmuş/Tuzlu) | ✅ |
| `0632` | 53 | **STRINGS.PLAYING_CARD_NAMES** — Balatro 52 oyun kartı tam (As/2-10/Vale/Kız/Papaz × Maça/Karo/Sinek/Kupa) + Generic Oyun Kartı | ✅ |
| `0633` | 13 | **STRINGS.PLAYS** — Stage play repertoire: **Dört Şövalyem ve Ben** (My Knights Four and I, YOTH), **Bir Görev Tamamlandı** (Maxwell itirafı), **Kasvet Örtüsü** (The Pall glossary), **Büyülü Bebek** (Enchanted Doll) Act 1-3 Scene 1-3 + **Buluşma** finalı (Türkçe tiyatro: "1. Perde - 2. Sahne") | ✅ |
| `0634` | 1 | **STRINGS.PSN** — PlayStation™Network marka korunur | ✅ |
| `0635` | 6 | **STRINGS.PYROMANCY** — Willow ateş büyüleri tam: **Ateş Topu** (2 Köz), **Tutuşma=Combustion** (4 Köz), **Yanan Çılgınlık=Burning Frenzy** (2 Köz), **Alev Atışı=Flame Cast** (1 Köz), **Ay Alevi=Lunar Flame** (5 Köz), **Gölge Ateş=Shadow Fire** (5 Köz). Embers=Köz birim tutarlı | ✅ |
| `0636` | 22 | **STRINGS.QUAGMIRE_CHARACTER_DESCRIPTIONS** — Boğaz etkinliği karakter özellikleri: Wigfrid (Bızonsığır kestiğinde fazladan et—Toplama), Maxwell (Gölge Oduncu çağırır—Toplama), Webber (Tohum eker hızlı—Tarım), Wendy (Izgara verimi—Pişirme), Wes (Uzman pazarlıkçı—Alışveriş), Wickerbottom (Olay kitabı + Yiyeceği inceler Kemiren'in canının çekip çekmediğini—Tarım), Willow (Kütükler uzun yanar—Pişirme), Wilson (Tencere verimi—Pişirme), Winona (Hızlı eylem—Tarım), Wolfgang (Fırın verimi—Pişirme), Woodie (Hızlı odun kesim—Toplama), WX-78 (Robotik koşma hızı—Toplama). PLACEHOLDER'lar Türkçe YERTUTUCU. Random=Rastgele bir hayatta kalan seç | ✅ |
| `0637` | 7 | **STRINGS.QUAGMIRE_ELDER_TALK_BUY** — Yaşlı Keçi BÜYÜK HARF (WX-78 tarzı): "TEŞEKKÜRLER. ŞİMDİ YAŞLIYI DİNLENDİR.", "EVET. SEN İYİ KEÇİ.", "BELKİ ŞİMDİ EVLERİ ONARIRIZ", "BOL ŞANS. KEMİREN İLE.", "TEŞEKKÜRLER, KÜÇÜK KEÇİ." | ✅ |
| `0638` | 7 | **STRINGS.QUAGMIRE_ELDER_TALK_GREETING** — Yaşlı Keçi karşılama BÜYÜK HARF: "HRF? TAKAS YAPAR? MALZEME?", "HRF? UYKU... YAŞLIYA KARABASAN VERİYOR", "HRF! KEMİREN DOMUZLARA KIZGIN", "HRF! KEÇİLERİN ÇOĞU DOMUZLARA YARDIM ETMEZ", "HRF? ...YAŞLI GİDERSE KÜÇÜK DOMUZLAR NE YAPAR?". HRF keçi sesi korunur | ✅ |
| `0639` | 6 | **STRINGS.QUAGMIRE_ELDER_TALK_SLEEP** — Yaşlı Keçi uyku mırıltı: "...HRMFFF...", "(HORLAMA) ...p...pullar...", "...v...veba...", "...zzzZZzzz...", "...k-KEMİREN...", "...g-gök..." (kıyamet öncesi rüya parçaları) | ✅ |

**Faz 3 toplam:** Oturum 5-13 = 3.919 + 286 = **4.205 string** (Faz 3'ün ~%84'ü tahmini)

### ✅ Oturum 14 — 2026-04-29 (2 batch / ~400 string) — RECIPE_DESC başladı

**Aydın'ın "devam" komutu + compact hazırlığı:** RECIPE_DESC'in ilk 2 batch'i çevrildi (kalan 3 batch Oturum 15'te tamamlandı).

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0650` | ~200 | **STRINGS.RECIPE_DESC** A-C: Wilson tarzı kısa tarif açıklamaları (sihirli hatıra=Abigail Çiçeği, "İnsan değerini kanıtla"=Başarıkonak, ölümden korur=Tılsım, "Tekne frenleri"=Çapa, **Battlesong serisi tam** Wigfrid: "Yüreklere bir kaside"=Sağlık Kazanma/"Sözel domates fırlat"=Alay/"Düşmüş yoldaşlarının yüreklerini coştur"=Diriliş, **Kitap kütüphanesi tam** Wickerbottom: "Arıcılığın ABCsini öğren"/"Kütüphaneci kuralı: Dewey Ondalık Sistemi"/"Yağmurlu güne sakla", **Boomerang/Bumeranj=Aşağıdaki memleketten geliyor** Avustralya pun, Boat ekosistemi başlangıcı (Hazır dikkat tekne/Birinin şamandırası başkasının bariyeri/Rekabeti suya gömer Klei pun), **Bookstation+Birdcage+Bedroll**, Carnival ekosistemi tam (Spread cheer=Neşe yayıver, Egg-citement=Yum-uyanış pun, Cawnival decor 4 yumurta+lamba+bitki, 6 mini oyun: Yumurta Telaşı/Yem Yaygara/Hafıza Sayım), Carrat/Cattoy/Catcoonhat, **Chesspiece sketch/builder serisi başlangıcı** (Anchor/Antlion/Bearger/Beequeen/Bishop/Butterfly/Carrat/Catcoon/Clay Hound+Warg/Crab King/Daywalker/Deerclops/Dragonfly/Eye of Terror/Formal/Guardian/Hornucopia/Kitcoon/Klaus/Knight/Malbatross/Manrabbit/Minotaur/Moon) | ✅ |
| `0651` | ~170 | **STRINGS.RECIPE_DESC** C-M devam: Chesspiece kalan (Moon/Moosegoose/Muse/Pawn/Pipe/Rook/Sharkboi/Stalker/Toadstool/Twins of Terror/WAGBOSS Lunar/Robot/Warg Mutated/Wormboss/YOTD/YOTH/YOTS sketches), **Cookbook+Cookpot+COTL** (Cult of the Lamb cross-promo: Kuzu kuru oyma/rafine heykel/göz kamaştırıcı anıt), **Critter ekosistemi tam** (Bulbin/Broodling/Eye of Terror/Glomling/Kittykit/Ewelet/Mothling/Civciv/Yavruvarg dostluk), **Decor seti** (Centerpiece/Flowervase/Lamp/Pictureframe/Portraitframe), **Dock/Dragonboat/Dragonfly furniture**, **Dumbbell tam** (Sticks and stones/altın standart/yontulmuş vücut/yanığı hisset), **Halloween 6 deney** (Sıvı cesaret/Yüreğine iyi/Bir değişim demleniyor/Belkemiği fidanları), **Ghostly Elixir 9 form** (Wendy iksir Abigail), Glasscutter+Goggles+Gold tools, **Hermit Crab Tea ekosistemi tam** Pearl (8 çay: Karnında ateş/Ay yerlileri/Aklı uçurumdan/Havalı olmak), **Kitcoon decor**, Lantern/Lighter/Lightning Rod, **Lunar Forge+Lunarplant Hat+Kit**, **Mad Science Lab/Magician Chest/Mast** çift entries | ✅ |
| `0652` | ~184 | (Oturum 15'te yapıldı) — bkz aşağı | (15) |
| `0653` | ~199 | (Oturum 15'te yapıldı) — bkz aşağı | (15) |
| `0654` | ~155 | (Oturum 15'te yapıldı) — bkz aşağı | (15) |

### ✅ Oturum 15 — 2026-04-29 (8 batch / 575 string) — RECIPE_DESC TAMAMLANDI ⭐ + PIG_TALK Elite başladı

**Aydın'ın "devam" komutu (compact sonrası):** Oturum 14'ten kalan 3 RECIPE_DESC bitirildi → **Faz 3'ün son büyük bloğu kapandı** ⭐, ardından PIG_TALK serisi başladı (Pugna domuz Tarzanvari kırık dil).

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0652` | 184 | **STRINGS.RECIPE_DESC** M-R: Mast Malbatross/Yusufçuk YOTD ("hiçbir Yusufçuk zarar görmedi"), **Meatrack** "Kurutmaca raflarının kralı" (jerky pun), **Mermhat** Mermleştir/**Mermarmory** "iyi oturan miğfer"/**Workmermship** mermhirlik (Klei pun), Mighty Gym "Pazılar konuşsun!", Minerhat "Geceyi kafanla aydınlat", Minifan "esinti yaratmak için koşman gerek", **Molehat** "Kokuvizyon" (Smell-E-Vision pun), Moondial/Moonglass/Moon Sketch, Moonstorm goggles "patates gözleri", **Mosquito ekosistemi** (bomba/gübre/merhem/koku), Multi tool "İki kat kullanışlı", **Mushroom Light** "mantar-Odasına" (mush-Room pun), **Mutator 7 form** (Dropper/Healer/Hider/Moon/Spitter "tıpatıp aynısı" spitting image pun/Warrior/Water "ağız sulandırıcı"), Nightlight "Geceyi rüyalarınla aydınlat", **Nightsword** "Berrak rüya hasarı", Nonslipgrit, Oar "Çek, çek, çek küreklerini" (Row Row Row pun), **Oar Driftwood** "Kürek demediğime sevinmedin mi" (Oarn't pun), **Ocean fishing 8 bobber+9 lure+spinner/spoon serisi tam** ("There's snow better time"=Balık tutmak için kar uygun zaman yok kar pun), Oneman Band "çılgın müzisyenlerin hayran kitlesi", Orange Amulet/Staff "yürümeyi sevmeyenler için", Panflute "Vahşi canavarları yatıştıran", Perdfan "Ekstra şanslı, ekstra büyük", Petals/Petals Evil "Yapraklarını arındır/lekele", Phonograph "karabasanlarının müziğini dinle", Pickaxe/Piggyback/Pighouse/Pigskin/Pigshrine "Müreffeh Domuz", Pirate flag, Pitchfork, Plant Registry Hat, **Pocketwatch 9 form Wanda tam** (Dismantler/Heal "Hissettiğin kadar yaşlısın"/Parts/Portal "arkadaşlarla daha güzel"/Recall/Revive "vakitsiz sonunu geri al"/Warp/Weapon "Bu saat SANA çalar"=This clock strikes YOU pun), Polly Rogers "tüylü dostla birlikte", Portable Blender/Cookpot/Firepit/Spicer/Tent, Pottedfern, **Premium Watering Can** "Sulamada bir inovasyon", Pumpkin Hat 2 entry, **Punching Bag 3 form**, Purple Amulet "Çılgınlığı tetikle", **Quagmire ekosistemi 27 entry tam** (Pot/Pot Hanger/Pot Syrup/Bowl Silver/Plate Silver/Casseroledish/Hoe/Key+Park/Crabtrap/Crate Grill+Small+Oven+Pot Hanger/Flour/Goatmilk/Pigeon/Salt+Rack/Sapbucket "Salak olma şurubu musluktan al"=sap pun/Slaughtertool "Et ağaçta yetişmiyor"/Spotspice/Seedpacket 7+1 tip/Portal Key/Bucket), Rabbit Hat/House/**Rabbitkinghorn** "ne tüy olursa" (any hare pun), Raincoat/Rainhat/Rainometer, Razor "hippi sakal", Record "Constant klasikleri", Red Gem/Lantern, Refined Dust, Reflective vest, **Research Lab 4 tier** ("Bu artık bilim sayılır mı ki?" Tier 3), Reskin tool, **Resurrection Statue** "Etin gücüyle dirilt", **Reviver** "Hayalet bir dostun ürkütücü dirilişi", Rope, Rope Bridge "Şüpheni askıya al" (suspend disbelief pun), Rose Glasses "yeni mercekten Charlie", Ruins Hat "kadim güç alanı", **Ruinsrelic 6 entry** (Bowl/Chair/Chipbowl "Çift batırma yok"/Plate "şık kırık"/Table/Vase "Sahte-antika"), Ruins Bat, Saddle Horn, **Saddle 5 tip** (Basic/Race "Belki"/Shadow "dizginleri ele al hüküm sür"=reins/reign pun/War "patron için taht"/Wathgrithr "Savaşçı ve atı tek vücut"), Saltbox, Saltlick | ✅ |
| `0653` | 199 | **STRINGS.RECIPE_DESC** R-T: Saltlick Improved "lüks tatlar", **Salty Dog hat** "yaşlı denizci için tuzlu refakatçi", Scarecrow "sonbahar moda", Sculptingtable "Mermer kil gibi", Seafaring Prototyper, Security Pulse Cage, Seedpouch, Sentryward "haritacının silahı", Sewing kit/mannequin/tape, **Shadow ekosistemi tam** (Digger "Kazı kazı çukur"/Duelist "Eterik koruma"/Lumber "Ağaçlara kin"/Miner/Battleaxe "düşene kadar baltalarsın"/Beef Bell/Forge Kit "Kendi rahatın için dehşetler"), Shellweaver "tutam tuzla", Shovel+**Lunarplant** ("kürek+çapa çapraz tozlanması"), Siesta Hut "sıcaktan kaç akıl yenile", Sisturn "yorgun ruhuna istirahat", Sleepbomb, **Slingshot ekosistemi 30 entry tam Walter**: Slingshot "Maceraya onsuz çıkma", **18 mermi**: Container/Dreadstone/Freeze/Gelblob "Yapışkak ve iğrenç" (sticky icky)/Gold "şıklıkları"/Gunpowder "Sahneye patlayarak gir"/Honey/Horrorfuel/**Lunarplanthusk** "Sarmaşkan davanı çöz" (vine-detta=vendetta pun)/Marble "Sakın kaybetme"/**Moonglass** "Beklentileri paramparça et" (shatter expectations)/Poop "İğrenç"/Purebrilliance "Ay'ın ötesinde sevineceksin" (over the moon)/Rock/Scrapfeather "Şoke edici şekilde şok edici"/Slow "fizik kuralları da neymiş?"/Stinger/Thulecite "Ne ters gidebilir ki?", **5 frame** (Bone/Gems/Wagpunk 2 form "büyük adam mı?")/4 handle (Jelly "yapışkan"/Silk/Sticky "Sapanına bağlan" Wormwood/Voidcloth)/3 band (Pigskin/Tentacle "Daha da uzağa"/Mod kit), Slow Farmplot, Soil Amender "denizden besinler", Spear "Sivri ucunu kullan", Spear Wathgrithr/Lightning "Şimşeğin gücü emrinde", Spicepack, **Spice 4 tip** (Chili "Tokat acı"/Garlic "savunma amaçlı ağız kokusu"/Salt/Sugar), **Spider 5 entry** (Spiderden Bedazzler/Eggsack/Hat "anne diyecek"/Healer "iğrenç sümüksü"/Repellent "alana ihtiyacın"/Whistle), **Staff Lunar+Tornado** ("Düşmanlarını uçur götür" blow away pun), **Steering Wheel** "teker tek önemli" (wheely pun), Stone Chair/Stool/Table 2, Strawhat, Succulent Potted, Super Tackle "Olta gibi takıldım" (hooked pun), Support Pillar 2, Sweater Vest, Sword Lunarplant, Table Winters Feast "etrafına toplan", Tacklecontainer "Taktiksel olarak", Tackle Station "yem-balık usulü", **Telebase** "Sadece cevher ekle", **Telestaff** "Uzayı bük! Zaman bükümü ayrı satılır", Tent "Akıl yeniler zamana ve açlığa", Thulecite, Thulecite Bugnet "kadim usülde", Ticoon Builder, Tillweed Salve, **Top Hat 2 form** (Tophat/Magician "Kara büyü"), Torch, **Town Portal** "kum gücüyle topla", **Transistor** "Bilim başlasın! Bzzzt!", **Transmute serisi 27 entry tam** (Beardhair/Beefalowool/Bluegem/Boneshard/Cutstone/Dreadstone/Flint/Goldnugget/Greengem/Horrorfuel/Houndstooth/Log/Marble/Meat/Moonglass Charged/Moonrocknugget/Nightmarefuel/Nitre/Opalpreciousgem/Orangegem/Poop/Purebrilliance/Purplegem/Redgem/Rocks/Smallmeat/Twigs/Yellowgem; Klei pun "Çürüğü Gübreye dönüştür"), Trap/Bramble/Teeth, Treasurechest, Tree Growth Solution "yeni boyutlara", **Trident** "Çalkantılı sularda coş" (rock out pun), Trophyscale Fish/Veggies, Trunkvest Summer/Winter, Turfcraftingstation, **Turf 31 tip yer döşeme tam** (Archive/Beard Rug/Carpetfloor 2/Cave/Checkerfloor/COTL Brick+Gold "altın çağ için zemin"/Deciduous/Desertdirt/Dragonfly/Forest/Fungus 4 renk/Grass/Marsh/Meteor 2/Monkey "muz kokulu"/Mosaic 3 renk/Mud/Pebblebeach/Road "hiçbir yere giden yol"/Rocky/Ruinsbrick+Tiles+Trim 6 entry/Savanna/Shellbeach/Sinkhole/Underrock/Vault/Vent/Woodfloor), Twigs "Tek bir dal her şeyi değiştirebilir" | ✅ |
| `0654` | 155 | **STRINGS.RECIPE_DESC** U-Z: Umbrella, **Vaultrelic 3 entry** (Bowl "patine kazanıyor"/Planter/Vase "geçmiş çağdan"), **Voidcloth Maxwell tam** (Hat "hiçbir ışık delemez"/Boomerang "dönüp dönüp gelmeye"/Kit/Scythe "bitki nüfusunu seyrelt"/Umbrella "gölgesi koruma"), Wagboss Robot 2 entry "Önce inşa et. Sonra panikle.", Wagpunk Bits/Hat/Floor "Okyanusu küçült! Kalıcı olarak.", Walking Stick, **Wall 9 tip duvar** (Dreadstone/Hay/Moonrock "Ay delisi"/Ruins/Scrap "kabaca duvar şeklinde hurda"/Stone/Wood + Walter "Şıklıktan önce şekil ve işlev"), **Wandering Trader Livinglog** "Hayat ağaçi çığlıktır" (Wormwood Life wood pun), Wardrobe, Warg Shrine, Waterballoon "Küresel yangın söndürme", Watering Can, Watermelon hat "ferahlatıcı yapışkan", Waterpump "Su, su her yerde su", **Wathgrithr 3 entry** (Hat "Tek boynuzlu at"/Improved "Valkyrie kraliçesine"/Shield "kendine inanırsa"), Waxpaper, **Waxwell Journal** "Aklını başından alır" (blow your mind pun), **Wendy 2 grave** ("Hiç kimse mezarsız ölmeyi hak etmez"/"Ölüm sadece bir aksaklıktır"=Death is but inconvenience), **Wereitem 3** (Beaver/Goose/Moose lanetler), Whip "Yapıcı geri bildirim dağıt", Winch, **Winona BATTERY+Catapult+Remote+Spotlight+Storage Robot+Telebrella+Teleport Pad** ("makine teslim eder" delivers pun), **Wintercooking 18 tarif tam** (Berrysauce "karnını jöleyle"/Bibingka "yapraklayacak"=leaf you pun/Cabbagerolls/Festivefish/Gravy "et suyu treni"/Latkes "latke kadar seveceksin"=a latke/A lot pun/Lutefisk "Deni-mevsim afiyetler"=sea-son's eatings pun/Mulleddrink/Panettone/Pavlova/Pickledherring/Polishcookie "babcia"=Polonyalı nine/Pumpkinpie "Kabakkün haberleri"=gourd tidings pun/Roastturkey "Gulguluyla mideye"/Stuffing "Suratını doldur"/Sweetpotato "marşmelov dünyası"/Tamales/Tourtiere), Winterhat/Winterometer/Wintersfeastoven/Winter Treestand "ağacı dik ve süsle", **Winter Ornament Boss 2 form**, Woby Treat, Wolfgang Whistle "İçindeki antrenörü", **Woodcarvedhat** "(tahtaya vur)" (knock on wood), Wood Chair/Stool/Table 2, **Wormwood 9 entry kırık dil** ("El yapımı!"/"Kolun ne kadar taşıyabilirse"/Carrat dönüşüm/Saladmander/Lightflier/Lureplantbulb "Kola mal olur ama bacağa olmaz"=arm/leg pun/Reeds "Sazo okumayı bilmek"=reed/read pun/Sapling "Kolundan dışarı büyü"), **Wortox 3** (Nabbag "Doldur ve savur"/Reviver/Souljar "kavanoza doldurabilecekken"), **Wurt 2 swamp** (Lunar/Shadow), **WX-78 28 modül BÜYÜK HARF tam** (BEE "VIZILDAT"/COLD/DIGESTION/HEAT/LIGHT 2/MAXHEALTH 2/MAXHUNGER 2/MAXSANITY 2/MOVESPEED 2/MUSIC "AKORT AYARI"/NIGHTVISION/RADAR/SCREECH/SHIELDING/SPIN "DÖNE DÖNE"/STACKSIZE "FAZLA DÜŞÜNME"/TASER/Backupbody/Drone Delivery+Scout+Zap Remote/Gestalttrapper/Moduleremover "ÇOKKAT-LAYANLARA"=a-ply pun/Scanner), W Radio Wickerbottom, Yellow Amulet/Staff, **YOTB tam 6 entry** (Beefaloshrine/Pattern Fragment 3 form fearsome/formal/festive/Post/Sewing Machine/Stage), **YOTC tam 11 entry** (Carratshrine/Gym Direction+Reaction+Speed+Stamina/Race Checkpoint+Finish+Start+items/Scale/Seedpacket+Rare), **YOTD 4 entry** (Anchor "altın standart"/Dragonshrine/Oar/Steeringwheel "altın için yarış"=go for gold pun), **YOTH 3 entry** (Chair Rocking/Knightshrine/Knightstick "Atlı maytap"=horse around pun), **YOTP 3 food**, **YOTR 7 entry** (Decor 2/Fightring/Food 4/Rabbitshrine/Token "yastık savaşı"), **YOTS 3 entry** (Lantern Post/Snakeshrine), **YOT_CATCOONSHRINE** "yakalanması zor kedikoon" — **STRINGS.RECIPE_DESC TAMAMEN BİTTİ ⭐** | ✅ |
| `0596` | 4 | **STRINGS.PIG_ELITE_FIGHTER_INTRO** — Pugna domuz BÜYÜK HARF Tarzanvari ("BEN YARDIM!", "EZ! EZ!", "YUMRUK ZAMAN!", "BEN NEREYİ EZ?") | ✅ |
| `0597` | 4 | **STRINGS.PIG_ELITE_FIGHTER_OUTRO** — ("DOMUZCUK, FIRLA!", "BEN YUMRUKLA!", "BEN GİT ŞİMDİ!", "GÖRÜŞÜRÜZ!") | ✅ |
| `0598` | 3 | **STRINGS.PIG_ELITE_GOLD** — ("BENİM!", "BENİM ALTIN!", "BEN ALTIN AL!") | ✅ |
| `0599` | 2 | **STRINGS.PIG_ELITE_INTRO** — ("KRAL İÇİN!", "ALTIN AL!") | ✅ |
| `0600` | 6 | **STRINGS.PIG_ELITE_POST_MATCH** — ("SEN BUNDA KÖTÜ. GELİŞ", "BİR DAHA DENE?", "SEN LAYIK RAKİP", "SEN BİZİ HÜRMETLENDİR", "İYİ MAÇ. BİZ ŞİMDİ YATAĞA", "SEN HİLECİ. BİZ HİLECİYİ SEVMEZ") | ✅ |

**Faz 3 toplam:** Oturum 5-15 = 4.605 + 575 = **~5.180 string** (Faz 3'ün **~%99'u** — RECIPE_DESC %100 TAM ⭐, PIG_TALK Elite serisi başladı).

**%11 EŞİĞİ AŞILDI** — 9.044 → 9.619 (%10.55 → %11.22) ⭐⭐

### ✅ Oturum 16 — 2026-04-29 (41 batch / 136 string) — PIG_TALK serisi TAM ⭐ + RABBIT

**Aydın'ın "devam" komutu (compact sonrası):** Oturum 15'te başlayan PIG_TALK Elite Pugna serisi tamamlandı (5/36 → 36/36 ⭐), sonrasında RABBIT (Tavşanadam) feryat/dövüş serisi de tamamlandı. **Faz 3 ~%100 bitti** — sadece SCRAPBOOK/SKILLTREE/STAGEACTOR Faz 4 kaldı.

| Batch | Sayı | Kapsam | Durum |
|---|---|---|---|
| `0601` | 3 | **STRINGS.PIG_ELITE_SALTY** — Pugna domuz BÜYÜK HARF Tarzanvari ("HİLECİ!", "ADİL DEĞİL", "ÖYLE YAPMAK YASAK!") | ✅ |
| `0602` | 4 | **STRINGS.PIG_ELITE_SMACK** — ("SEN GİT EZ!", "BEN SENİ EZ!", "UZAK DUR!", "EĞLENCE!") | ✅ |
| `0603` | 3 | **STRINGS.PIG_GUARD_TALK_FIGHT** — Pig Guard krala sadakat ("KRAL İÇİN!", "SAVUN!", "KRALI KORU!") | ✅ |
| `0604` | 3 | **STRINGS.PIG_GUARD_TALK_GOHOME** — ("SAVUNMAK GEREK!", "BEN KORU", "KRAL! KRAL!") | ✅ |
| `0605` | 3 | **STRINGS.PIG_GUARD_TALK_LOOKATWILSON** — ("SEN ŞİMDİ GİT", "SEN UZAĞA GİT", "SEN BURADA KALMA") | ✅ |
| `0606` | 3 | **STRINGS.PIG_GUARD_TALK_TORCH** — meşale yakıt durum ("MEŞALE BİTİYOR", "MEŞALEYİ PARLAT", "DAHA ÇOK YANSIN") | ✅ |
| `0607` | 2 | **STRINGS.PIG_TALK_ATTEMPT_TRADE** — ("NE VAR SENDE?", "İYİ ŞEY OLSA İYİ.") | ✅ |
| `0608` | 3 | **STRINGS.PIG_TALK_CONTEST_OOOH** — yarışma ünlemleri ("OOOH", "VAAY", "GÜZEL ŞEY") | ✅ |
| `0609` | 2 | **STRINGS.PIG_TALK_CONTEST_PANIC** — ("SEÇMEK GEREK!", "SEÇİM ZOR!") | ✅ |
| `0610` | 2 | **STRINGS.PIG_TALK_EAT_MEAT** — ("NOM NOM NOM", "MIIIK!") | ✅ |
| `0611` | 3 | **STRINGS.PIG_TALK_FIGHT** — ("BEN ÖLDÜR ŞİMDİ!", "SEN GİT EZ!", "RAAAWR!") | ✅ |
| `0612` | 5 | **STRINGS.PIG_TALK_FIND_LIGHT** — karanlıktan korkup ışığa sığınma ("KORKUNÇ", "KARANLIK SEVMEM", "GÜNEŞ NEREDE?", "ATEŞ YANINA KAL", "ATEŞ İYİ") | ✅ |
| `0613` | 4 | **STRINGS.PIG_TALK_FIND_MEAT** — ("BEN AÇ!", "MIIIK!", "BEN YEMEK YE!", "YEMEK ZAMANI!") | ✅ |
| `0614` | 4 | **STRINGS.PIG_TALK_FOLLOWWILSON** — domuz takip ("SEN ARKADAŞ", "BEN ARKADAŞ SEV", "SEN İYİSİN", "BEN GEL ARKANDAN!") | ✅ |
| `0615` | 7 | **STRINGS.PIG_TALK_GAME_CHEER** — yarış tezahürat ("EZ! EZ!", "VUR!", "HAYDİ DOMUZLAR!", "RAAAWR!", "PİS KOKARSIN!", "ALTIN AL!", "KAFADAN VUR!") | ✅ |
| `0616` | 3 | **STRINGS.PIG_TALK_GAME_GOTO** — ("BAŞLIYOR!", "BU EN SEVDİĞİM!", "YAŞA!") | ✅ |
| `0617` | 2 | **STRINGS.PIG_TALK_GIVE_GIFT** — ("SEN AL BUNU", "ARKADAŞ İÇİN") | ✅ |
| `0618` | 2 | **STRINGS.PIG_TALK_GO_HOME** — ("EV ZAMANI!", "EV! EV!") | ✅ |
| `0619` | 3 | **STRINGS.PIG_TALK_HELP_CHOP_WOOD** — ağaç kesim yardım ("AĞAÇ ÖLDÜR!", "KÖTÜ AĞAÇ EZ!", "BEN AĞAÇ YUMRUKLA!") | ✅ |
| `0620` | 3 | **STRINGS.PIG_TALK_LOOKATWILSON** — ilk karşılaşma ("SEN KİM?", "SEN DOMUZ DEĞİL", "SENDE ET VAR?") | ✅ |
| `0621` | 2 | **STRINGS.PIG_TALK_MISC_GAME_CHEER** — ("HAYDİ! HAYDİ! HAYDİ!", "HOMURT!") | ✅ |
| `0622` | 3 | **STRINGS.PIG_TALK_MISC_GAME_GOTO** — ("BAŞLIYOR!", "ÇEKİL YOLUMDAN!", "YAŞA!") | ✅ |
| `0623` | 3 | **STRINGS.PIG_TALK_PANIC** — ("HAYIRRR!", "ÇOK KARANLIK! ÇOK KARANLIK!", "AAAAAAAAAH!!") | ✅ |
| `0624` | 5 | **STRINGS.PIG_TALK_PANICBOSS** — boss korku ünlemleri ("AHHHH", "OY OY!", "BEN KORK", "KÖTÜ!", "OHHH!") | ✅ |
| `0625` | 4 | **STRINGS.PIG_TALK_PANICELECTRICITY** — şimşek panik ("AAYYY!", "AAAAH!", "SEVMEM BUNU!", "BEN KIZAR!") | ✅ |
| `0626` | 3 | **STRINGS.PIG_TALK_PANICFIRE** — ateş panik ("SICAK SICAK SICAK!", "AAYYY!", "YAKIYOR!") | ✅ |
| `0627` | 3 | **STRINGS.PIG_TALK_PANICHAUNT** — hayalet ("ÜRPERTİCİ!", "AAAAH!!", "HAYALET! HAYALET!") | ✅ |
| `0628` | 4 | **STRINGS.PIG_TALK_PANICHOUSEFIRE** — ev yangını ("EV YANIYOR!", "EŞYALARIM!", "AAAH! ATEŞ!", "PANİK!") | ✅ |
| `0629` | 3 | **STRINGS.PIG_TALK_RESCUE** — yardım ("BEN YARDIM SANA!", "OY! OY!", "BEN YARDIM!") | ✅ |
| `0630` | 4 | **STRINGS.PIG_TALK_RUNAWAY_WILSON** — ("ÇOK YAKIN!", "UZAK DUR!", "SEN GERİ ÇEKİL!", "ORASI BENİM YERİM.") | ✅ |
| `0631` | 3 | **STRINGS.PIG_TALK_RUN_FROM_SPIDER** — ("ÖRÜMCEK KÖTÜ!", "ÖRÜMCEK SEVMEM!", "KORKUNÇ ÖRÜMCEK!") — **PIG_TALK serisi TAMAMEN BİTTİ ⭐** | ✅ |
| `0640` | 3 | **STRINGS.RABBIT_BATTLECRY** — Tavşanadam savaş çığlığı ("ZIPLA!", "ÖLDÜR!", "ÖL!") | ✅ |
| `0641` | 2 | **STRINGS.RABBIT_GIVEUP** — vazgeçme ("BİTTİ.", "SONRA.") | ✅ |
| `0642` | 5 | **STRINGS.RABBIT_MEAT_BATTLECRY** — ahlaki öfke et yiyene ("ET!", "PİS!", "KATİL!", "İNTİKAM!", "CANAVAR!") | ✅ |
| `0643` | 4 | **STRINGS.RABBIT_PANICBOSS** — ("KAÇ!", "AHHH!", "ÇILGIN BU", "EHHH!") | ✅ |
| `0644` | 3 | **STRINGS.RABBIT_PANICELECTRICITY** — ("OFF!!", "ACIDI!", "BATTI!") | ✅ |
| `0645` | 3 | **STRINGS.RABBIT_PANICFIRE** — ateş ünlem ("EEEH!", "OOH!", "AAAH!") | ✅ |
| `0646` | 4 | **STRINGS.RABBIT_PANICHAUNT** — hayalet ("KORKTUM!", "AAAH!!", "OHH!", "HAYALET!") | ✅ |
| `0647` | 3 | **STRINGS.RABBIT_PANICHOUSEFIRE** — ("EVİM!", "ATEŞ!", "YANIYOR!") | ✅ |
| `0648` | 4 | **STRINGS.RABBIT_RESCUE** — kurtarma saldırı ("ÖLDÜR!", "DÖVÜŞ!", "ISIR!", "YUMRUKLA!") | ✅ |
| `0649` | 4 | **STRINGS.RABBIT_RETREAT** — ("UZAĞA!", "ACIDI!", "EVE!", "KAÇ!") | ✅ |

**Faz 3 toplam:** Oturum 5-16 = ~5.180 + 136 = **~5.316 string** (Faz 3 **%100 TAM** ⭐, küçük PIG/RABBIT mob talker setleri kapandı)

**Toplam ilerleme:** 9.619 → 9.755 (%11.22 → %11.38)

## 🎯 Sıradaki Oturum (17) — Yol Haritası

### **EN YÜKSEK ÖNCELİK:** Faz 4 başla — SCRAPBOOK
- `0655-0658` STRINGS.SCRAPBOOK (4 batch, ~600 SPECIALINFO + CATS/SUBCATS/FOODTYPE) — uzun item açıklamaları, Klei mizahı disiplini

### Faz 4 (devam)
- `0680-0683` STRINGS.SKILLTREE (4 batch, ~400 string) — Wendy/Wickerbottom/Wilson/Wolfgang/WX-78 vb. yetenek ağacı
- `0733-0736` STRINGS.STAGEACTOR (4 batch, ~600 string) — Atriyum sahne oyunu replikleri
- Diğer küçük SET/SHADOW/SHARD/SIGNS bloklar

### Faz 6 — SKINS (sonra)
- `0684-0723` SKIN_DESCRIPTIONS + SKIN_NAMES (40 batch, ~7.806 string)

### Faz 5 (CHARACTERS) — EN SON
Item glossary tamamlandığında batch_0060'a dönüp 17 karakter speech çevirisine başla. Persona disiplini için `docs/character-voices.md` zorunlu.

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
