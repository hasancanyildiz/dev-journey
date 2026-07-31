def kare_topla(sayilar):
    toplam = 0
    for sayi in sayilar:
        kare = sayi ** 2
        toplam += kare
    return toplam

liste = [1, 2, 3, 4]
sonuc = kare_topla(liste)
print(f"Toplam: {sonuc}")