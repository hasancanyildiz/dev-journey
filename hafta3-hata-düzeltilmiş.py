sozluk = {"isim": "Hasan", "yas": 20}

try:
    print(sozluk["meslek"])
except KeyError:
    print("Hata: 'meslek' anahtarı sözlükte bulunamadı!")