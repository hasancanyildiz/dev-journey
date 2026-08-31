# Terminal Komutları - Cheat Sheet

## Temel Dosya/Klasör İşlemleri
- `pwd` — Bulunduğun konumu gösterir
- `ls` — Dosya/klasörleri listeler
- `ls -la` — Gizli dosyalar dahil, detaylı listeleme
- `cd` — Klasör değiştirir
- `cd ..` — Bir üst klasöre çıkar
- `mkdir` — Yeni klasör oluşturur
- `touch` — Boş dosya oluşturur
- `rm` — Dosya siler
- `rm -r` — Klasörü (içindekilerle) siler
- `cp` — Dosya kopyalar
- `mv` — Dosya taşır / yeniden adlandırır

## Dosya İçeriği Görüntüleme
- `cat` — Dosya içeriğini ekrana yazdırır
- `less` — Uzun dosyayı sayfa sayfa gösterir (q ile çık)
- `echo` — Ekrana veya dosyaya metin yazar
- `echo "metin" > dosya` — Dosyanın üzerine yazar
- `echo "metin" >> dosya` — Dosyanın sonuna ekler

## Arama
- `grep "kelime" dosya` — Dosya içinde metin arar
- `find . -name "*.txt"` — Dosya adına göre arama yapar
- `find . -size 1033c` — Belirli boyuttaki (byte) dosyayı arar
- `find / -user X -group Y -size Nc` — Sahiplik ve boyuta göre sistem genelinde arama

## Dosya Analizi
- `file dosya` — Dosyanın gerçek türünü söyler (metin mi, binary mi vb.)
- `du dosya` / `du -h klasor/` — Disk kullanım boyutunu gösterir

## Özel Karakter/İsim Sorunları İçin
- `./dosya` — Tire ile başlayan dosya adlarında, "gerçek dosya" olduğunu belirtir
- `cat -- "isim"` — `--` ile başlayan dosya adlarında kullanılır
- `"isim with spaces"` — Boşluklu dosya adlarını tek argüman olarak okutur
- `./*` — Klasördeki tüm dosyaları ifade eder

## SSH Bağlantısı
- `ssh kullanici@sunucu -p port` — Uzak sunucuya bağlanır
- `exit` — Bağlantıdan/oturumdan çıkar

## OverTheWire Bandit İlerleme
Level 0 → 6 tamamlandı.
