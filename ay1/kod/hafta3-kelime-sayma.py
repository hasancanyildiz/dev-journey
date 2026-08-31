with open("ornek.txt" ,"r") as dosya:
    metin =dosya.read()


kelime_sayısı=len(metin.split())

with open ("sonuc.txt","w") as dosya:
    dosya.write(f"Toplam kelime sayısı{kelime_sayısı}" )

print(f"İşlem tamam. kelime sayısı {kelime_sayısı}")