# DST Türkçe Yama

Don't Starve Together için açık kaynak, kapsamlı, **bağlamsal** Türkçe çeviri modu.

> 🚧 **Geliştirme aşamasında — Faz 3 (item + lore çevirisi).** Faz 2 UI ✅ %100 tamam: ana menü, ayarlar, dünya kurma, sunucu yönetimi, Süs Dolabı, Takas Hanı, Maç Sonu Paneli ve tüm HUD aksiyonları (Saldır/İncele/Kuşan...) tamamen Türkçe. Faz 3'te şu an: ACTIONS, BOARLORD (Forge patron), CARNIVAL_CROWKID + CARNIVAL_HOST (Karganaval), karakter seçim ekranı tüm bilgileri (biyografi/unvan/alıntı) ve **item isimlerinin 4/15'i çevrildi (~800 item)** — silah/zırh/yemek/balık/dragonfly/dreadstone/chess piece/critter dahil. Tam yama (UI + itemler + 17 karakter konuşmaları) v1.0 ile gelecek.

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
| 3 | İtem isimleri + tarif/envanter açıklamaları + lore | 🟡 ~%38 (CHARACTER kartları tam, NAMES 4/15) |
| 4 | Bilim/üretim/skill tree/sahne | ⬜ |
| 5 | 17 karakter konuşmaları (62.645 string) | ⬜ |
| 6 | Skinler + lore + vinyetler | ⬜ |
| 7 | QA playtest | ⬜ |
| 8 | Logo + Workshop varlıkları | ⬜ |
| 9 | v1.0 yayın | ⬜ |

**Toplam:** **6.356 / 85.706 msgid çevrildi (%7.42)** · 9 oturum tamamlandı (2026-04-26 → 2026-04-28). Detaylı durum: [`PROGRESS.md`](PROGRESS.md).

### Son oturumda eklenen Türkçe içerik (Oturum 9)

- 🏷️ **600 item ismi (B-F aralığı)** — Karganaval mini oyun seti (Yumurta Telaşı, Yem için Yaygara, Sepetteki Yumurtalar), CHESSPIECE figürünleri (~50 boss heykelciği), Critter (yavru evciller: Yavruşa, Sevimli Gözcü, Kedicik, Kuzucuk, Güveşa, Civciv, Yavruvarg), tekne ekipmanları (Yusufçuk Tekne, Korsan Yelkenli, Denizotopilot), tarım bitkileri (Domarot, Bahçe Kazgereci, Kakaş Kovası).
- 🎨 **Yeni Klei pun'ları Türkçe pun'la** — Nautopilot=Denizotopilot (deniz+otopilot), Geothermite=Jeotakar (jeotermal+akar), Hornucopia=Boynuzkopya (boynuz+cornucopia), Frostjaw=Buzçene, Figatoni=İncironi (incir+rigatoni), Figkabab=İncirkebap, Ice Flingomatic=Buz Fırlatomatik, Toma Root=Domarot.
- 🛡️ **Boss & lore kartı** — Boarrior=Yabansavaşçı, Possessed Varg=Ele Geçirilmiş Varg, Celestial Scion=Semavi Veliaht, Ancient Fuelweaver=Kadim Yakıtdokur, Crystal Deerclops=Kristal Geyikgöz, Volatile Canary=Patlayıcı Kanarya, Dreadstone=Korkutaş.
- 🔠 **Akronim ve özel isim koruma** — T.I.N.G.L.E. (elektrikli çit), W.A.R.B.O.T., Houndius Shootius (Klei Latince pun) çevrilmedi.

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

## Lisans

- **Kod** (Lua mod, Python pipeline): [MIT](LICENSE)
- **Çeviri metinleri** (`languages/*.po`, `scripts/speech_overrides/*.lua`): CC-BY-SA 4.0

## Katkı

Yanlış çeviri / eksik metin / bug için **Issues** sekmesi. PR rehberi `CONTRIBUTING.md` (yakında).

---

**Sahip:** [@aydincol4k](https://github.com/aydincol4k) · **Build:** DST `722900` · **Sürüm:** `0.5.0-faz3`
