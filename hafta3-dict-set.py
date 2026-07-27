kisi ={"isim ":"Hasan","yas": 20,"sehir":"Ankara"}
print(kisi.get("isim"))
print(kisi.get("meslek"))  # yok, None döner
print(kisi.get("meslek", "Belirtilmemiş"))  

kisi.update({"yas": 21, "meslek": "Öğrenci"})
print(kisi)

print(kisi.keys())
print(kisi.values())
print(kisi.items())

for anahtar,deger in kisi.items():
    print(anahtar ,":",deger)

print()
print("Set ve kümeler")
sayilar1={1,2,3,4,5}
sayilar2={6,7,8,9,10,5}
# birleşim
print(sayilar1 | sayilar2)

# kesişim
print(sayilar1 & sayilar2)

# fark
print(sayilar1 - sayilar2)

sayilar1.add(10)
print(sayilar1)