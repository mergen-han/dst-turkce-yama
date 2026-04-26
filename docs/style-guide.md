# DST Türkçe Yama — Çeviri Stil Rehberi

Bu rehber, çevirilerin **tutarlı**, **bağlamsal** ve **Klei'nin tonuna sadık** kalmasını sağlar. Glossary (`glossary.tsv`) terim sözlüğüdür; bu dosya **dilbilgisi ve üslup kurallarıdır**.

> Kural çatışırsa: glossary > style-guide > genel Türkçe.

---

## 1. Üslup ve hitap

### "Sen / Siz" ayrımı
- **Sen:** Karakterlerin oyuncuya hitabı, oyun içi tooltip'ler, item açıklamaları, replikler.
- **Siz:** Sistem mesajları, hata mesajları, lobby/menu yönergeleri ("Lütfen bekleyiniz", "Sunucuya bağlanılıyor").
- Karakter karakterle konuşurken **karakter ses tonu** kuralları geçerli (bkz. `character-voices.md`).

### "Lütfen" ve resmiyet
- Sistem mesajlarında *gereksiz* "lütfen" kullanma; doğal Türkçe yeter.
  - ❌ "Lütfen bir karakter seçiniz."
  - ✅ "Bir karakter seç."
  - ✅ "Sunucuya bağlanılıyor..."

### Ünlemler
- Klei'nin orijinal tonu **gotik mizah** — abartılı duygusallıktan kaçın.
- Karakter repliklerinde ünlem orijinaldeki sıklıkla. Wilson "Hmm." der, "HARİKA!" demez.
- Wendy ünlem **kullanmaz**, melankolik nokta.
- Willow ünlem **bolca** kullanır.

---

## 2. Dilbilgisi

### Sayı + isim
- Türkçede sayıdan sonra isim **tekildir.**
  - ❌ "30 günler", "5 örümcekler"
  - ✅ "30 gün", "5 örümcek"

### Çoğul ek
- İngilizce her zaman çoğul ekli ("3 spiders") değil; Türkçe daha esnek.
- Belirsiz çoğullukta `-ler/-lar` koru: "Örümcekler saldırıyor."
- Sayılı bağlamda atla: "3 örümcek geldi."

### Büyük harf kullanımı
- **Özel isimler ve ürün isimleri:** Her sözcüğün ilk harfi büyük.
  - ✅ "Şirin Şemsiye", "Domuzların Kralı", "Kara Kılıç"
- **UI butonları:** İlk harf büyük, gerisi küçük.
  - ✅ "Yeni oyun", "Sunucuya bağlan"
- **Sistem mesajları:** Cümle gibi yaz (sadece ilk harf + özel isim).

### Noktalama
- Cümle sonu noktası **bırak** (Klei orijinalleri böyle).
- Karakter repliklerinde üç nokta (`…` veya `...`) Wendy/Maxwell için doğal.
- Tırnak içinde italic gerekmez; düz metin.

### Türkçe diakritikler
- **UTF-8 olarak doğal yaz:** ş ç ğ İ ı ö ü Ş Ç Ğ İ Ö Ü.
- Smoke test (Faz 0) doğruladı: DST `fonts.zip` fallback atlas'ı bu karakterleri render eder.
- ASCII transliterasyon (s/c/g/I) **YASAK.**

---

## 3. Kelime oyunları (pun) ve mizah

### Strateji: Anlam koru, kelime değiştir
İngilizce pun'ı motamot çevirme; Türkçede de pun yarat.

**Örnekler:**
| EN | TR | Açıklama |
|---|---|---|
| Eyebrella (eye + umbrella) | Gözlemsiye (göz + şemsiye) | Portmanto korunmuş |
| Pretty Parasol | Şirin Şemsiye | İki kelime de "Ş" ile başlar, kafiye |
| Ham Bat | Jambon Sopa | Aynı saçma birliktelik |
| Pierogi | Mantı | Yerelleştirme — Türk damağına yakın eşdeğer |
| Jerky | Pastırma | Aynı |
| Drumstick | But | Tavuk budu, kısa ve net |

### Kafiye/aliterasyon mümkünse koru
- "Spider Den" → "Örümcek İni" (her iki dilde Ö/İ ile başlıyor değil ama "in" mağara hissi koruyor)
- Wortox karakteri **şiirsel kafiye** yapar — onun replikleri özel kategori (bkz. `character-voices.md`).

### "Don't translate" listesi
Bunları çevirme:
- Karakter özel isimleri (Wilson, Maxwell vb.)
- "Krampus", "Klaus" gibi mitolojik isimler
- Marka isimleri (Steam, Klei)

---

## 4. Bağlam yakalama (motamot karşıtlığı)

### Eylem fiili seçimi
- "Examine" → "İncele", "Bak" değil. Karakter eşyaya bilgece bakıyor.
- "Pick up" → "Topla" (objeye göre "Al" da olur, ama envanter bağlamında "Topla").
- "Equip" → "Kuşan" (zırh/silah), "Tak" (mücevher).
- "Eat" → "Ye". "Drink" → "İç". Klasik.
- "Investigate" → "Araştır" (cesaret), "Bak" (merak).

### "The X" → tanımlık atlanır
- "The Spider Queen" → "Örümcek Kraliçesi" (önünde "O" yok).
- "The Forest" biyom adı → sadece "Orman".

### "It's a..." kalıbı
- Karakter inceleme: "It's a spider!" → "Bu bir örümcek!" (motamot OK).
- Ama Wilson akademik olduğunda: "Arachnida sınıfından bir örnek." (persona'ya göre).

### Soru cümleleri
- "What is it?" → "Bu nedir?" (kısa) veya "Acaba ne ola ki?" (Wickerbottom).
- Karakter ses tonu önemli.

---

## 5. Birim ve sayı çevirisi

| EN | TR |
|---|---|
| 30 days | 30 gün |
| 5 stacks | 5 yığın |
| -10 health | -10 can |
| 100% sanity | %100 akıl |
| ½ stack | ½ yığın (½ veya 1/2, Klei orijinaline bak) |

**Yüzde:** `%100` formatında, `%` önde (Türkçe norm).

**Para birimi:** DST'de para yok ama "1 nugget" → "1 külçe".

---

## 6. Escape ve özel karakterler

### DST gettext-lite kuralları
- Sadece `\n`, `\r`, `\"` escape edilir.
- Backslash kendisi escape edilmez (`\\` YOK).
- UTF-8 doğal Türkçe karakterler.

### Yeni satır
- `\n` orijinaldeki yerinde kalır (UI satır kırma).
- Türkçe çeviri uzunluk değişirse `\n`'i koru ama dengele (örn. iki kısa satır → bir uzun satır olabilir, UI sığarsa).

### Yer tutucular (placeholder)
- `{1}`, `%s`, `%d` gibi yer tutucuları **AYNEN** koru.
- Yerini değiştir, ama Türkçe söz dizimine uydur:
  - EN: `Day {1} starts now.` → TR: `{1}. gün başlıyor.`
  - EN: `Welcome back, {name}!` → TR: `Tekrar hoş geldin, {name}!`

---

## 7. Karakter ses tonu

Detaylı persona kuralları için: **`character-voices.md`**.

Kısa özet:
- **Wilson** akademik centilmen
- **Willow** manyak çocuksu
- **Wolfgang** kırık aksanlı güçlü adam
- **Wendy** melankolik şair
- **WX-78** BÜYÜK HARF mekanik
- **Wickerbottom** pedanti kütüphaneci ("müteşekkirim", "lakin")
- **Maxwell** alaycı kibirli
- **Wormwood** yarım Türkçe, basit
- **Wortox** şiirsel kafiye yapar (en zor)
- ...

---

## 8. Kalite kontrolü (her batch için)

1. Glossary'ye sadakat: `validate_po.py` otomatik kontrol eder.
2. UTF-8 + BOM yok: aynı validator.
3. Escape disiplini: aynı validator.
4. Karakter ses tonu: insan QA — Faz 5'te detaylı.
5. Gözden geçirme: Aydın her batch'i merge öncesi okur.

---

## 9. Yaygın hatalar (kaçınılacak)

❌ "Sağlık" yerine **"Can"** (bar başlığı kuralı)
❌ "Domuz Kral" → **"Domuzların Kralı"**
❌ "Akıl sağlığı" → **"Akıl"**
❌ "30 günler" → **"30 gün"**
❌ Türkçe karakter olmayan transliterasyon (s/c/g/i) → **UTF-8 doğal**
❌ Tüm cümleyi büyük harf (WX-78 hariç!) → **Cümle tipi**
❌ Karakterler arası ton karışması (Wilson'ı Willow gibi yazma)
❌ "Lütfen" gereksiz fazla kullanım
❌ Pun'ı kelime kelime çevirme

---

## 10. Bu rehbere katkı

Yeni kural önerisi → GitHub Issue veya PR. Tüm değişiklikler `validate_po.py` testlerinden geçmeli.
