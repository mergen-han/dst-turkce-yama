name = "Türkçe Yama"
author = "Aydın Çolak (aydincol4k) ve katkıda bulunanlar"
version = "0.1.0-faz0"
description = [[Don't Starve Together için tam Türkçe çeviri modu (geliştirme aşamasında).

Faz 0 — Smoke test sürümü. Yalnızca ana menüdeki "Play" butonu Türkçeleştirilmiştir; Türkçe karakterlerin (ş ç ğ İ ö ü) düzgün render edilip edilmediği kontrol edilir.

Açık kaynak: github.com/aydincol4k/dst-turkce-yama
Lisans: MIT (kod) + CC-BY-SA 4.0 (çeviriler)]]

forumthread = ""

api_version = 10

dst_compatible = true
dont_starve_compatible = false
reign_of_giants_compatible = false
shipwrecked_compatible = false
hamlet_compatible = false

client_only_mod = true
all_clients_require_mod = false

-- icon_atlas = "modicon.xml"
-- icon = "modicon.tex"
-- ^ Faz 8'de SDXL üretimi modicon eklenecek; Faz 0 smoke testte modicon olmaması mod yüklenmesini engellemez (sadece sarı uyarı simgesi gösterir).

priority = 100

server_filter_tags = { "turkce", "turkish" }

configuration_options = {
    {
        name = "speech_overrides",
        label = "Karakter Replikleri",
        hover = "Karakterlerin item incelemelerini Türkçeleştir.",
        options = {
            { description = "Açık", data = true },
            { description = "Kapalı", data = false },
        },
        default = true,
    },
    {
        name = "debug_log",
        label = "Geliştirici Logu",
        hover = "Konsola çeviri yükleme bilgisi yazdırır (geliştirme için).",
        options = {
            { description = "Kapalı", data = false },
            { description = "Açık", data = true },
        },
        default = true,
    },
}
