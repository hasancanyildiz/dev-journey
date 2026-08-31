def toplama (a ,b):
    return (a+b)

sonuc= toplama(3,6)
print("Sonuç:", sonuc)

print(" ")
print("Defult değer : ")
def selam(isim ="Misafir"):
    print(f"Merhaba{isim}")

selam()
selam("Hasan")    

print("*args")
def toplamHesapla (*sayılar) :
    return sum(sayılar)

print(toplamHesapla(1,2,3,4,5,6))


print(" ")
print("**kwargs")
def bilgi_yazdır(**bilgiler):
    for anahtar,değer in bilgiler.items():
        print(f"{anahtar}: {değer}")

bilgi_yazdır(isim ="Hasan", yaş =21 ,boy=178)   