# DST Türkçe Yama

Don't Starve Together için açık kaynak, kapsamlı, **bağlamsal** Türkçe çeviri modu.

> 🚧 **Geliştirme aşamasında — Faz 3 (item + lore çevirisi).** Faz 2 UI ✅ %100 tamam: ana menü, ayarlar, dünya kurma, sunucu yönetimi, Süs Dolabı, Takas Hanı, Maç Sonu Paneli ve tüm HUD aksiyonları (Saldır/İncele/Kuşan...) tamamen Türkçe. Faz 3'te şu an: ACTIONS, BOARLORD (Forge patron), CARNIVAL_CROWKID + CARNIVAL_HOST (Karganaval), karakter seçim ekranı tüm bilgileri (biyografi/unvan/alıntı) ve **item isimlerinin 10/15'i çevrildi (~2.000 item)** — silah/zırh/yemek/balık/dragonfly/maxwell+stage play/merm ekosistemi/halloween/lavaarena forge zırh/moon items + ocean fishing 18 balık + Quagmire 70 yemek + Wanda saat seti + Tavşan Kralı 3 form + Bilim Makinesi/Simya Motoru/Gölge Manipülatörü/Şapksihirbaz dahil. Tam yama (UI + itemler + 17 karakter konuşmaları) v1.0 ile gelecek.

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
| 3 | İtem isimleri + tarif/envanter açıklamaları + lore | 🟡 ~%62 (CHARACTER kartları tam, NAMES 10/15) |
| 4 | Bilim/üretim/skill tree/sahne | ⬜ |
| 5 | 17 karakter konuşmaları (62.645 string) | ⬜ |
| 6 | Skinler + lore + vinyetler | ⬜ |
| 7 | QA playtest | ⬜ |
| 8 | Logo + Workshop varlıkları | ⬜ |
| 9 | v1.0 yayın | ⬜ |

**Toplam:** **7.556 / 85.706 msgid çevrildi (%8.82)** · 11 oturum tamamlandı (2026-04-26 → 2026-04-28). Detaylı durum: [`PROGRESS.md`](PROGRESS.md).

### Son oturumda eklenen Türkçe içerik (Oturum 11)

- 🏷️ **600 item ismi (M-S aralığı)** — Sivrisinek seti tam (Skeeter Bomb=Sivrisinek Bombası, Fertilizzzer=Vızılgübre zzz vızıltı pun), Mantar tam (Boomshroom=Patmantar, Funcap=Şenşapka, Glowcap=Parlakşapka, Mushtree 4 renk), Mutator yumurta seti 7 tip (Switcherdoodle=Karıştırgıç), Karabasan serisi (Nightmarebeak=Karabasangaga, Yakıt/Sur/Işık), Wanda saat seti tam (Backtrek/Backstep/Ageless/Rift/Second Chance/Korkutucu Çalar Saat), **Quagmire 70 yemek tarifi tam** (Lazanya/Pizza/Köri/Spagetti/Mantı/Ratatuy/Cheesecake), **Tavşan Kralı 3 form** (Wrathful/Fortuitous/Benevolent), **Ocean fishing tam** (8 şamandıra+8 yem+5 spinnerbait+4 spoon + 18 balık türü), Bal Kabağı serisi tam, Domuzların Kralı tam (Clout Snout=Yumruk Burun, Altın Kemer), Tüm pişirme istasyonları (Bilim Makinesi/Simya Motoru/Gölge Manipülatörü/Şapksihirbaz).
- 🎨 **Yeni Klei pun'ları Türkçe pun'la** — Antchovy=Karıncamsi (ant+anchovy → karınca+hamsi), Sweetish Fish=Tatlısveç Balığı (Swedish+sweet pun), Fallounder=Sonbalkan (fall+flounder), Popperfish=Patbalığı, Spittlefish=Tükürük Balığı, Boomshroom=Patmantar, Switcherdoodle=Karıştırgıç (-gıç eki Türkçe alet), Permafrost Pengull=Buzul Pengul, Premier Gardeneer Hat=Mükemmel Bahçemühendis Şapkası, Powdercake=Barut Pastası (Klei dark humor), Prime Mate=Birinci Maymun (primate+first mate çift pun), Alarming Clock=Korkutucu Çalar Saat (alarm clock pun), Deadelgänger=Ölüdoppelgänger, Warren Wreath=Tavşanyuva Çelengi (warren=tavşan yuvası YOTR pun), Short Circuit=Kısa Devre (NAMES.RAIN Klei pun!), Prestihatitator=Şapksihirbaz (prestidigitator+hat çift pun), Glossamer Saddle=Yaldız Eyeri.
- 🐰 **Tavşan ekosistemi tam** — Rabbit King 3 form (Öfkeli/Rastlantısal/İyiliksever), Burrowing Horn=Kazıcı Boynuz, Royal Rabbit Enforcer=Kraliyet Tavşan İcra Memuru, Warren Wreath (YOTR), Tavşan Kafesi/Deliği.
- 🍳 **Quagmire (Boğaz) tam** — Kemiren'in Sunağı (Gnaw=Kemiren), 70 yemek tarifi (uluslararası mutfak: İtalyan/Fransız/Asya), Sammy/Pipton (Lucid=Net Akıllı/Cognizant=Farkına Varan Bog Merm), Şekerağacı (Sugarwood), Annecik=Mumsy (anne keçi), Eski Sikke/Safir Madalyon/Kemiren'in Lütfu para birimleri.

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

## Lisans

- **Kod** (Lua mod, Python pipeline): [MIT](LICENSE)
- **Çeviri metinleri** (`languages/*.po`, `scripts/speech_overrides/*.lua`): CC-BY-SA 4.0

## Katkı

Yanlış çeviri / eksik metin / bug için **Issues** sekmesi. PR rehberi `CONTRIBUTING.md` (yakında).

---

**Sahip:** [@aydincol4k](https://github.com/aydincol4k) · **Build:** DST `722900` · **Sürüm:** `0.7.0-faz3`
