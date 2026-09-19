# Not Defteri CLI

Ay 2 mini projesi için yaptığım basit bir komut satırı not defteri. Not ekleyebiliyorsun, arayabiliyorsun, listeleyebiliyorsun ve silebiliyorsun.

Arama kısmında binary search kullandım (görevin şartıydı zaten), bu yüzden not eklerken liste otomatik olarak alfabetik sıraya giriyor. Sıralı olmasa binary search zaten çalışmazdı.

## Nasıl çalıştırılır

```bash
python3 notebook_cli.py
```

Açılınca şöyle bir menü çıkıyor:

```
1. Not Ekle
2. Not Ara (Binary Search)
3. Notları Listele
4. Not Sil
5. Çıkış
```

Sayıyı yazıp Enter'a basman yeterli.

## Notlar

- Notlar sadece programı çalıştırdığın süre boyunca bellekte duruyor, kapatınca gidiyor. Dosyaya kaydetme yok şu an, belki sonra eklerim.
- Arama tam eşleşme arıyor (büyük/küçük harf önemli değil ama başlığın tamamını yazman lazım). Kelimenin bir kısmını yazınca bulamıyor, sonraki geliştirmede bakarım.

## Kullanılan araçlar

Python 3, başka bir şey yok.
