# Steam Workshop — Türkçe Açıklama

> Bu dosya Steam Workshop'taki "Description" alanına yapıştırılır. Steam **BBCode** kullanır (`[b]`, `[h1]`, `[url]`, `[list]` vs. — Markdown DEĞİL).
>
> v1.0 yayın öncesi son kontrol: linkler çalışıyor mu, sürüm + tarih güncel mi, `Build` numarası DST'nin son sürümüne uygun mu.

---

## Workshop kart bilgileri (sol panel formu)

- **Title:** `Türkçe Yama`
- **Description (kısa, ana menüde mod listesinde gösterilen):** `Don't Starve Together için kapsamlı, bağlamsal Türkçe çeviri. Tüm UI + 17 karakter konuşması + lore + skin'ler. Mağarada da çalışır.`
- **Visibility:** Public
- **Tags:** `Language`, `Tweak`, `Translation`, `turkce`, `turkish`
- **Required items:** (yok — bağımsız mod)

---

## Description (BBCode)

```bbcode
[h1]Türkçe Yama — Don't Starve Together için tam Türkçe çeviri[/h1]

[b]Don't Starve Together'ı baştan sona Türkçe oynayın.[/b] Ana menüden son boss diyaloğuna kadar her şey — UI, ayarlar, item incelemeleri, karakter konuşmaları, lore, skin açıklamaları — bağlamsal olarak Türkçeye çevrildi. Motamot değil; Klei'nin gotik mizahı, kelime oyunları ve karakter ses tonları korundu.

[h1]✨ Öne çıkan özellikler[/h1]

[list]
[*][b]Tam çeviri[/b] — UI (4.439 string) + İtem isimleri (2.802 isim) + Karakter konuşmaları (17 karakter) + Lore + Skin açıklamaları + Wagstaff araştırma notları + Wendy hayalet iksirleri + Wickerbottom kütüphanesi + Wilson akademik gözlemleri.
[*][b]Mağarada çalışır[/b] — Önceki Türkçe yamalardaki en büyük bug çözüldü. Mağaraya inip Forest shard'ından Cave shard'ına geçtiğinde çeviri kaybolmaz.
[*][b]Karakter ses tonu korunur[/b] — Her karakterin kendine özgü Türkçe sesi var:
  [list]
  [*]Wilson akademik bilim adamı tonu ("Bilim diyor ki sıramı beklemeliyim").
  [*]Wendy melankolik kız ("Abigail... beni terk etmedi, sadece... yer değiştirdi").
  [*]WX-78 BÜYÜK HARFLE robot konuşması ("ETLİLERE LANET. METAL ÜSTÜN").
  [*]Wormwood yarım Türkçe bitki ("İyi yemek? Wormwood için çiçek? Mutlu...").
  [*]Wortox şiirsel kafiyeli ("Bir ruh, bir ruh, hepsi cana yakın").
  [*]Wigfrid Old Norse + Türkçe Viking konuşması ("Räğnarök yäklaşıyör!").
  [*]Webber çocuk ağzı ("Biz açız! Hepimiz!" — örümcek + çocuk çoğul).
  [*]Diğer 10 karakter de ayrı persona.
  [/list]
[*][b]Bağlamsal çeviri[/b] — Klei pun'ları Türkçe pun'la yeniden yaratıldı:
  [list]
  [*]Eyebrella → Gözlemsiye (göz + şemsiye)
  [*]Beefalo → Bızonsığır (bizon + sığır)
  [*]Cawnival → Karganaval (karga + karnaval)
  [*]Powder Monkey → Barut Maymunu (denizci argo)
  [*]Prestihatitator → Şapksihirbaz (şapka + sihirbaz)
  [*]Slurtle / Snurtle / Shelmet → Salyangurp / Sarsalyo / Kabukmiğfer (kabuk pun seti)
  [*]Magiluminescence → Sihirili Parıltı
  [/list]
[*][b]200+ terim glossary disiplini[/b] — Health/Sanity/Hunger asla "sağlık" değil — [b]Can/Akıl/Açlık[/b]. Spider Den asla "Örümcek Yuvası" değil — [b]Örümcek İni[/b]. Pig King asla "Domuz Kral" değil — [b]Domuzların Kralı[/b]. Tutarlılık her oturumda doğrulanır.
[*][b]Tek mod, çift shard[/b] — Forest + Cave için tek paket. Co-op'ta sadece host'ta yüklü olması yeterli (client_only_mod=true).
[*][b]Açık kaynak[/b] — GitHub'da gelişiyor, topluluk PR'ları kabul edilir, DST güncellemelerinde otomatik diff.
[/list]

[h1]🚀 Kurulum[/h1]

[olist]
[*]Bu sayfada [b]Subscribe[/b] (Abone Ol) tuşuna bas.
[*]Steam DST'yi otomatik indirir.
[*]DST'yi başlat → [b]Mods → Server Mods → Türkçe Yama → Enable → Apply[/b].
[*](İsteğe bağlı) Mod ayarlarından [i]Karakter Replikleri[/i] → Açık/Kapalı seçimi.
[/olist]

[b]Sunucu sahibi mi?[/b] Mod'u sunucu modlarına ekle, oyuncuların ayrıca yüklemesi gerekmez (`client_only_mod=true`).

[h1]🐛 Bug + yanlış çeviri bildirme[/h1]

[list]
[*]Steam Workshop yorum kısmı — kısa bug raporu için.
[*][url=https://github.com/aydincol4k/dst-turkce-yama/issues]GitHub Issues[/url] — detaylı rapor + ekran görüntüsü için (tercih edilen).
[*]Yanlış çeviri önerisi varsa: önce [url=https://github.com/aydincol4k/dst-turkce-yama/blob/main/docs/glossary.tsv]glossary.tsv[/url]'ye bak — terim oradaysa kararı destekleyen gerekçe bulursun.
[/list]

[h1]📜 Lisans + Katkı[/h1]

[list]
[*][b]Kod[/b] (Lua mod, Python pipeline): MIT
[*][b]Çeviri metinleri[/b] (PO + speech overrides): CC-BY-SA 4.0
[*][b]Katkı:[/b] Fork → translations/<konu> branch → PR. Detay [url=https://github.com/aydincol4k/dst-turkce-yama/blob/main/CONTRIBUTING.md]CONTRIBUTING.md[/url].
[/list]

[h1]🙏 Teşekkürler[/h1]

[list]
[*][b]Klei Entertainment[/b] — Don't Starve evrenini ve modlama API'sini açtığı için.
[*][b]Topluluk[/b] — Bug raporları + glossary önerileri + PR katkıları.
[*][b]Claude (Anthropic)[/b] — AI-destekli çeviri kanalı (sıfırdan yazıldı, mevcut Türkçe yamalar base alınmadı).
[/list]

[h1]ℹ️ Notlar[/h1]

[list]
[*]Bu yama [b]gayri resmi[/b] bir hayran çalışmasıdır. Klei Entertainment'la bağlantısı yoktur.
[*]Çeviriler Türkiye Türkçesi'dir. Kıbrıs / Azerice farklılıkları için fork yapılabilir (CC-BY-SA).
[*]Önceki rakip Türkçe yamalardan [b]hiçbir şey base alınmadı[/b] — sıfırdan AI-destekli + insan redakte.
[*]DST sürüm uyumluluğu: Klei her hafta yeni içerik ekliyor. Yeni string'ler için GitHub'da haftalık otomatik diff. Bir gün gecikmeli yetişiyoruz.
[/list]

[hr][/hr]

[b]Sürüm:[/b] 1.0.0 — [i](yayın tarihi v1.0'da güncellenecek)[/i]
[b]Build uyumu:[/b] DST 722900 ve sonrası
[b]Repo:[/b] [url=https://github.com/aydincol4k/dst-turkce-yama]github.com/aydincol4k/dst-turkce-yama[/url]
[b]Sahip:[/b] Aydın Çolak
```

---

## BBCode hızlı referans

| Markdown | BBCode |
|---|---|
| `**bold**` | `[b]bold[/b]` |
| `*italic*` | `[i]italic[/i]` |
| `# H1` | `[h1]H1[/h1]` |
| `## H2` | `[h2]H2[/h2]` |
| `[link](url)` | `[url=https://...]link[/url]` |
| `- liste` | `[list][*]item[/list]` |
| `1. liste` | `[olist][*]item[/olist]` |
| `---` | `[hr][/hr]` |
| `> alıntı` | `[quote]alıntı[/quote]` |

## Yayın öncesi kontrol listesi

- [ ] Sürüm numarası `modinfo.lua` ile aynı (1.0.0).
- [ ] Build numarası (`722900`) DST son sürümüne uygun.
- [ ] GitHub linki + Issues linki canlı.
- [ ] Abuse / küfür / copyright iddiası YOK.
- [ ] "Fan-made unofficial" + Klei Entertainment trademark notu var.
- [ ] Tags 5 adet (Steam max): Language, Tweak, Translation, turkce, turkish.
- [ ] Required items: yok (bağımsız mod).
- [ ] Visibility: Public.
- [ ] Türkçe karakterler doğru render (ş ç ğ İ ö ü).
