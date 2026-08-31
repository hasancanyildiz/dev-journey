try :
    sayı_1=int(input("Bir sayı giriniz : "))
    sayı_2=int(input("Bir sayı giriniz : "))
    toplam=sayı_1 /sayı_2
    print(f"sonuç :{toplam}")
except ZeroDivisionError:
        print("Sıfıra bölemzsin")
except ValueError:
    print("Hata geçerli sayı girilmedi")
finally:
    print("İşlem tamamlandı")        