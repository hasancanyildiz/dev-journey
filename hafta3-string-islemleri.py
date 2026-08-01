metin = " Merhaba Dünya  "

#stript : baştaki ve sondaki bolukları siler
print(metin.strip())

#split kelimelere ayırır(liste yapar)
print(metin.strip().split())

#join bir listeyi belirli bir ayraçla birleştirir
kelimeler =["Python","öğreniyorum"]
print(" -- ".join(kelimeler))

#replace belirli bir kelimeyi değistirir
print(metin.replace("Dünya", "Python"))

#f-string ile değişken gömme

isim ="Hasan"
print(f"Merhaba {isim}")

#format ile aynı işlemi yapma
print("Merhaba {}".format(isim))