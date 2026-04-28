# DST Türkçe Yama

Don't Starve Together için açık kaynak, kapsamlı, **bağlamsal** Türkçe çeviri modu.

> 🚧 **Geliştirme aşamasında — Faz 3 (item + lore çevirisi).** Faz 2 UI ✅ %100 tamam: ana menü, ayarlar, dünya kurma, sunucu yönetimi, Süs Dolabı, Takas Hanı, Maç Sonu Paneli ve tüm HUD aksiyonları (Saldır/İncele/Kuşan...) tamamen Türkçe. Faz 3'te şu an: ACTIONS, BOARLORD (Forge patron), CARNIVAL_CROWKID + CARNIVAL_HOST (Karganaval), karakter seçim ekranı tüm bilgileri (biyografi/unvan/alıntı) ve **STRINGS.NAMES TAMAMEN BİTTİ! ⭐ 2.802 item ismi tam** — silah/zırh/yemek/balık/dragonfly/maxwell void cloth+stage play/merm ekosistemi/halloween/lavaarena forge zırh/moon items + ocean fishing 18 balık + Quagmire 70 yemek + Winter cooking 21 tarif + Wanda saat seti + Tavşan Kralı 3 form + Bilim Makinesi/Simya Motoru/Gölge Manipülatörü/Şapksihirbaz + Slingshot 18 mermi + WX-78 24 modül + Wagstaff teknobabel + W.A.R.B.O.T. patron + 10 Yıl etkinliği (YOTB-YOTC-YOTD-YOTH-YOTP-YOTR-YOTS) dahil. Tam yama (UI + itemler + 17 karakter konuşmaları) v1.0 ile gelecek.

## Özellikler

- 🤖 **AI-destekli + insan redakte:** Claude ile bağlamsal çeviri, glossary ve style-guide disipliniyle tutarlı kalite.
- 🕳️ **Mağarada çalışır:** `AddSimPostInit` + `AddPlayerPostInit` ile shard geçişlerinde çeviri yeniden yüklenir — yeraltında İngilizce'ye dönmez.
- 🎭 **Karakter ses tonu korunur:** 17 karakterin her biri için ayrı persona (Wilson akademik, Wendy melankolik, WX-78 BÜYÜK HARF, Wormwood yarım Türkçe, Wortox şiirsel kafiye...).
- 🎨 **Bağlamsal çeviri:** Motamot değil — Klei'nin gotik mizahı korunur, kelime oyunları Türkçe pun'larla yeniden yaratılır (`Eyebrella → Gözlemsiye`, `Pretty Parasol → Şirin Şemsiye`).
- 📜 **Açık kaynak:** Topluluk PR'larıyla canlı kalır, DST güncellemelerinde otomatik diff.
- 📦 **Tek mod:** Forest + Cave için tek mod, ayrı "server versiyonu" gerekmez.

## İlerleme

| Faz | Açıklama | Durum |
|---|---|---|
| 0 | Mod iskeleti + smoke test | ✅ |
| 1 | Pipeline + glossary + dokümantasyon | ✅ |
| 2 | UI çevirisi (4.439 string) | ✅ %100 |
| 3 | İtem isimleri + tarif/envanter açıklamaları + lore | 🟡 ~%78 (CHARACTER kartları tam, **NAMES 15/15 ⭐ TAMAMLANDI**) |
| 4 | Bilim/üretim/skill tree/sahne | ⬜ |
| 5 | 17 karakter konuşmaları (62.645 string) | ⬜ |
| 6 | Skinler + lore + vinyetler | ⬜ |
| 7 | QA playtest | ⬜ |
| 8 | Logo + Workshop varlıkları | ⬜ |
| 9 | v1.0 yayın | ⬜ |

**Toplam:** **8.644 / 85.706 msgid çevrildi (%10.09)** ⭐ %10 EŞİĞİ AŞILDI · 13 oturum tamamlandı (2026-04-26 → 2026-04-29). Detaylı durum: [`PROGRESS.md`](PROGRESS.md).

### Son oturumda eklenen Türkçe içerik (Oturum 13 — Lore + sahne oyunu temizliği)

- 🏷️ **286 string / 11 batch** — küçük lore + sahne oyunu + Quagmire blokları temizlendi.
- 🃏 **Balatro 52 oyun kartı tam** — Maça/Karo/Sinek/Kupa × As/2-10/Vale/Kız/Papaz tutarlı.
- 🎭 **Sahne oyunu repertoire tam** — Dört Şövalyem ve Ben (YOTH), Bir Görev Tamamlandı (Maxwell itirafı), Kasvet Örtüsü, Büyülü Bebek (9 sahne + Buluşma finalı).
- 🔥 **Willow Pyromancy ateş büyüleri tam** — Ateş Topu, Tutuşma=Combustion, Yanan Çılgınlık, Alev Atışı, Ay Alevi=Lunar Flame, Gölge Ateş=Shadow Fire (Embers=Köz birim).
- 🐷 **PIGNAMES tam (146 isim)** — 79 Roma imparatoru ve 20 Klei dev ekibi korundu, 47 yemek/şirin domuz ismi yerelleştirildi (Pastırma=Bacon, Mantı=Dumpling, Hor Hor=Oinkey, Domuzlu Bao=Porkbun, Yumurtbert=Eggbert).
- 🐐 **Quagmire (Boğaz) tam** — Yaşlı Keçi'nin BÜYÜK HARF konuşmaları (BUY/GREETING/SLEEP), 16 karakter Boğaz yetenekleri (Wickerbottom: "Olaya tam uygun kitabı yanında bulundurur, Yiyeceği inceleyerek Kemiren'in canının çekip çekmediğini belirler").
- 🌫️ **Atriyum gotik ilahi** — Nightmare Overgrowth 5 satırlık eski Türkçe karanlık şiir: "Yüzünü çevirenin terk ettiği zavallılar... Karanlık bizim kalkanımız oldu. Geçimimiz. Tesellimiz."

### Önceki oturum (Oturum 12 — NAMES BİTTİ! ⭐)

- 🏷️ **802 item ismi (S-Y aralığı) — STRINGS.NAMES TAMAMEN TAMAMLANDI (15/15)** — toplam 2.802 item ismi, NAMES sıfır kaldı.
- 🎬 **Shadow ekosistemi tam** (Maxwell void cloth zırhı: Karbumeranj=Gloomerang gloom+boomerang pun, Karemsiye=Umbralla umbra+brella pun, Gölge Orakçısı=Shadow Reaper, Boşluk Başlığı=Void Cowl), **Karabasan Köleler 6 form** (Mega Yıkım+Mürekkep Yıkımı + Allegiance: Dalga/Titrek/Hırıltı/Sırıtış/Çığlık + Boşluk Maskesi=Void Masque + Tenebrau Müjdecisi Latince).
- 🪶 **Walter Slingshot ekosistemi tam** — Sadık Sapan + 18 mermi türü (Cıvıkışlar=Ickies, Patlamalar=Kablooies, İğneli Zıngırlar=Stinger Zingers, Ay Atışları=Moonshots) + 4 lastik+çerçeve+tutamak modüler sistem.
- 🧪 **Wagstaff Wagpunk teknobabel tam** — 5 araştırma notu, 5 alet (Birleştirici Tampon=Reticulating Buffer, Widget Düzeltici=Widget Deflubber, Grommet İşaretleyici, Kavramsal Temizleyici, Kalibre Edilmiş Algılayıcı), 5 layman karşılığı (Tuhaf/Garip/Acayip/Komik/Acayip Alet), W.A.R.B.O.T. patron tam (Termalkilit Füzesi, Aydınlanmış formu).
- 🤖 **WX-78 24 modül devresi tam** — Fasulyepompa=Beanbooster, Gastronkazanç=Gastrogain, Korokutu=Chorusbox, Menzilpompa=Rangebooster, Sonik Çağırıcı, Yer Genişletici=Spatializer + Roto-Mapper=Dönen Haritacı + Zaptotom=Zaptrocuter + B.U.D.D.Y. radyo akronim.
- 🍽️ **Winter cooking 21 tarif tam** — Şen Meyve Sosu, Bibingka (Filipin), Lahana Sarması, Pavlova, Polonya Kurabiyeleri, Cennetlik Yumurta Likörü=Heavenly Eggnog, 9 winter food (Şeker Bastonu, Sonsuz Meyveli Kek, Çikolatalı Kütük Pasta).
- 🎉 **10 Yıl etkinliği tam** — YOTB Bızonsığır 9 doll, YOTC Havufare 4 spor salonu, YOTD Yusufçuk seti, YOTH Salıncaklı Kısrak+Şaka At=Shtick Horse Yiddish pun+Mızrak-Atılışı=Joust-a-Dash, YOTR Tavşan: Yastık Dövüşü Çukuru+Meydan Okuma Eldiveni, YOTS Yılan: Jubilemfener=Jubilantern (jubilation+lantern pun).
- 🎨 **Yeni Klei pun'ları Türkçe pun'la** — Reanimated Skeleton=Diriltilmiş İskelet, Boulderbough=Kayalık Dal (boulder+bough), Strident Trident=Tisli Trident (alliterasyon T-T), Pinchin' Winch=Cımbız Vinç (alliterasyon), Pith Pike=Özlü Kargı (alliterasyon P-P), Magiluminescence=Sihirili Parıltı, Tail o' Three Cats=Üç Kedinin Kuyruğu (cat-o-nine-tails pun), Spectackler Box=Göz Alıcı Olta Kutusu (spectacle+tackle pun), The Lazy Deserter=Tembel Asker Kaçağı, Knabsack=Kapçuval (Wortox), Twintailed Heart=Çift Kuyruklu Yürek, Mudslinger=Çamuratan (Wurt), Combriner=Kabukörgücü (Wurt), Skittersquid=Tıngır Mürekkep, Slurtle=Salyangurp+Snurtle=Sarsalyo+Shelmet=Kabukmiğfer (kabuk pun seti), Pipspook=Cıvılcuk, Ewecus=Koyuncuk (ewe+mucus), Auto-Mat-O-Chanic=Otomekanikçi, Terramite=Karasırrı (terra+mite), Warbler=Şakırdak, Doohickey=Cızbız + Gizmo=Mıkıcık (Klei comic argo), Air Unfreshener=Hava Bayatlatıcı (Klei dark humor), Gnomette=Cinciket, Wandering Trader=Gezgin Tüccar (Beefalo formunda gizli).

## Kurulum

> **Workshop link Faz 9'da eklenecek.** Şu an yerel test için:

1. Bu repo'yu klonla veya ZIP indir.
2. İçeriği şuraya kopyala: `Steam/steamapps/common/Don't Starve Together/mods/dst-turkce-yama/`
3. DST'yi başlat → **Mods → Client Mods → Türkçe Yama → Enable → Apply**.

## Çeviri kalitesi

Glossary'den örnekler (`docs/glossary.tsv` — 200+ zorunlu terim):

| EN | TR | Not |
|---|---|---|
| Health / Sanity / Hunger | Can / Akıl / Açlık | Asla "sağlık" değil |
| Spider Den | Örümcek İni | "in" mağara hissi korur |
| Pig King | Domuzların Kralı | "Domuz Kral" yasak |
| Eyebrella | Gözlemsiye | göz + şemsiye portmanto |
| Touch Stone | Diriliş Taşı | İşlevsel anlam |
| The Forge / The Gorge | Demirhane / Boğaz | Etkinlik adları |
| Curio Cabinet | Süs Dolabı | |
| Beefalo | Bızonsığır | bizon + sığır |
| Catcoon / Bunnyman | Kedikoon / Tavşanadam | |
| Werepig / Werebeaver | Kurtdomuz / Kunduzkurt | were- → kurt- |
| Cawnival | Karganaval | crow + carnival |
| Corvus Goodfeather | Corvus İyitüy | Karganaval host |
| Birchnut / Antlion / Batilisk | Huşfındığı / Karıncaaslanı / Yarasalisk | |
| Brightshade / Sproutrock | Aydıngölge / Filiztaşı | Ay/Atriyum lore |
| Nautopilot / Geothermite | Denizotopilot / Jeotakar | deniz+otopilot, jeotermal+akar |
| Hornucopia / Frostjaw | Boynuzkopya / Buzçene | boynuz+cornucopia, buz+çene |
| Figatoni / Figkabab | İncironi / İncirkebap | incir+rigatoni, incir+kebap |
| Toma Root / Dreadstone | Domarot / Korkutaş | tomato+root, dread+stone |
| Forget-Me-Lots / Mimicreep | Unutma-Beni-ler / Sinsimimik | not→lots, mimic+creep |
| Howlitzer / Inspectacles | Ulutop / İnceleme Gözlüğü | howl+howitzer, inspect+spectacles |
| Brightsmithy / Ryftstal | Aydındemirhane / Yarkristal | bright+smithy, rift+crystal |
| Florpkale / Mermhane | Flort-ifications / Armermry | Wurt florp+fortifications, armory+merm |
| Antchovy / Fallounder | Karıncamsi / Sonbalkan | ant+anchovy, fall+flounder |
| Sweetish Fish / Switcherdoodle | Tatlısveç Balığı / Karıştırgıç | sweet+Swedish, switcher+doodle |
| Prestihatitator / Alarming Clock | Şapksihirbaz / Korkutucu Çalar Saat | prestidigitator+hat, alarm clock pun |
| Deadelgänger / Warren Wreath | Ölüdoppelgänger / Tavşanyuva Çelengi | dead+doppelgänger, warren=tavşan yuvası |
| Prime Mate / Powdercake | Birinci Maymun / Barut Pastası | primate+first mate, dark humor |
| Short Circuit (rain) / Glossamer | Kısa Devre / Yaldız | NAMES.RAIN pun, gossamer ipek |
| Gloomerang / Umbralla | Karbumeranj / Karemsiye | Maxwell void cloth: gloom+boomerang, umbra+brella |
| Slurtle / Snurtle / Shelmet | Salyangurp / Sarsalyo / Kabukmiğfer | slug+turtle, snail+turtle, shell+helmet |
| Skittersquid / Pipspook | Tıngır Mürekkep / Cıvılcuk | skitter+squid, pip+spook |
| Magiluminescence / Jubilantern | Sihirili Parıltı / Jubilemfener | magic+luminescence, jubilation+lantern |
| Ewecus / Combriner | Koyuncuk / Kabukörgücü | ewe+mucus, Wurt shellweaver |
| Stinger Zingers / Pith Pike | İğneli Zıngırlar / Özlü Kargı | slingshot ammo, alliterasyon P-P |
| Mudslinger / Knabsack | Çamuratan / Kapçuval | Wurt mud+slinger, Wortox knab+sack |
| Doohickey / Gizmo | Cızbız / Mıkıcık | Winona klein comic argosu |
| Shtick Horse / Joust-a-Dash | Şaka At / Mızrak-Atılışı | YOTH 10. yıl, Yiddish shtick |
| Tail o' Three Cats / The Lazy Deserter | Üç Kedinin Kuyruğu / Tembel Asker Kaçağı | cat-o-nine-tails, lazy+deserter Klei pun |

## Lisans

- **Kod** (Lua mod, Python pipeline): [MIT](LICENSE)
- **Çeviri metinleri** (`languages/*.po`, `scripts/speech_overrides/*.lua`): CC-BY-SA 4.0

## Katkı

Yanlış çeviri / eksik metin / bug için **Issues** sekmesi. PR rehberi `CONTRIBUTING.md` (yakında).

---

**Sahip:** [@aydincol4k](https://github.com/aydincol4k) · **Build:** DST `722900` · **Sürüm:** `0.8.1-faz3`
