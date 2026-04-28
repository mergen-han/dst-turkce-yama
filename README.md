# DST Türkçe Yama

Don't Starve Together için açık kaynak, kapsamlı, **bağlamsal** Türkçe çeviri modu.

> 🚧 **Geliştirme aşamasında — Faz 3 (item + lore çevirisi).** Faz 2 UI ✅ %100 tamam: ana menü, ayarlar, dünya kurma, sunucu yönetimi, Süs Dolabı, Takas Hanı, Maç Sonu Paneli ve tüm HUD aksiyonları (Saldır/İncele/Kuşan...) tamamen Türkçe. Faz 3'te şu an: ACTIONS, BOARLORD (Forge patron), CARNIVAL_CROWKID + CARNIVAL_HOST (Karganaval), karakter seçim ekranı tüm bilgileri (biyografi/unvan/alıntı) ve **item isimlerinin 7/15'i çevrildi (~1.400 item)** — silah/zırh/yemek/balık/dragonfly/maxwell+stage play/merm ekosistemi/halloween/lavaarena forge zırh/moon items dahil. Tam yama (UI + itemler + 17 karakter konuşmaları) v1.0 ile gelecek.

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
| 3 | İtem isimleri + tarif/envanter açıklamaları + lore | 🟡 ~%50 (CHARACTER kartları tam, NAMES 7/15) |
| 4 | Bilim/üretim/skill tree/sahne | ⬜ |
| 5 | 17 karakter konuşmaları (62.645 string) | ⬜ |
| 6 | Skinler + lore + vinyetler | ⬜ |
| 7 | QA playtest | ⬜ |
| 8 | Logo + Workshop varlıkları | ⬜ |
| 9 | v1.0 yayın | ⬜ |

**Toplam:** **6.956 / 85.706 msgid çevrildi (%8.12)** · 10 oturum tamamlandı (2026-04-26 → 2026-04-28). Detaylı durum: [`PROGRESS.md`](PROGRESS.md).

### Son oturumda eklenen Türkçe içerik (Oturum 10)

- 🏷️ **600 item ismi (F-M aralığı)** — Halloween 14 şeker + 9 iksir + 6 deney + 6 süs, Pearl/Hermit Crab tam ekosistemi (Çay Dükkanı, Kaplıca, 9 çay tarifi), Lavaarena Forge zırh seti tam (~25 zırh/silah/miğfer), Stage play maske seti (Visionist/Elytra/Artificer/Halfwit/Sage/Toady), Maxwell tam (Kabus Kilidi, Gramofon, Taht), Merm ekosistemi tam (Mermhane, Florpkale, Kraftsmerm), Moon items derinlik (Aycam, Aykayası, Semavi Sunak/Mabet/Sunu serisi).
- 🎨 **Yeni Klei pun'ları Türkçe pun'la** — Forget-Me-Lots=Unutma-Beni-ler (multiplicity pun), Asparagazpacho=Kuşkonmazpacho, Howlitzer=Ulutop (howl+howitzer), Inspectacles=İnceleme Gözlüğü (inspect+spectacles), Mimicreep=Sinsimimik, Crustashine=Kabukparlak, Moggles=Köstgözlük, Lureplant=Tuzakbitki, Vitreoasis=Camsı Vaha, Astroggles=Astrgözlük, Ryftstal=Yarkristal (rift+crystal), Brightsmithy=Aydındemirhane, Moongleam=Aypırıltı, Florpkale=Flort-ifications (Wurt florp+fortifications), Friend-O-Matic=Dost-O-Matik.
- 🍽️ **Yiyecek/içecek pun'ları** — Mourning Glory=Yas Çiçeği (mourning+morning glory), Vigor Mortis=Vigor Mortis (rigor mortis pun, Latince korunur), Long Pig=Uzun Domuz (kanibalist eufemizm), Slightly Less Shoddy Tool=Biraz Daha Az Baştan Savma Alet (Klei dark humor).
- 🐾 **Karakter & boss isimleri** — Pearl, Hutch, Bernie özel isim korundu; YOTH 4 atlı (Pascal/Desdemona/Fermin/Warren) korunur; Lavae lava+larva pun korunur; Treeguard=Ağaçmuhafız, Volt Goat=Şimşek Keçisi, Mandrake=Adamotu, Saladmander=Salatamender.

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

## Lisans

- **Kod** (Lua mod, Python pipeline): [MIT](LICENSE)
- **Çeviri metinleri** (`languages/*.po`, `scripts/speech_overrides/*.lua`): CC-BY-SA 4.0

## Katkı

Yanlış çeviri / eksik metin / bug için **Issues** sekmesi. PR rehberi `CONTRIBUTING.md` (yakında).

---

**Sahip:** [@aydincol4k](https://github.com/aydincol4k) · **Build:** DST `722900` · **Sürüm:** `0.6.0-faz3`
