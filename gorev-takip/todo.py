import json

gorevler = []
id_sayacı = 1


def gorev_ekle(baslik):
    global id_sayacı

    gorev = {
        "gorev_id": id_sayacı,
        "baslik": baslik,
        "tamamlandi": False
    }
    gorevler.append(gorev)
    id_sayacı += 1
    return gorev


def gorev_listele():
    return gorevler


def gorevleri_yazdir(liste):
    if not liste:
        print("Görev yok")
        return
    for gorev in liste:
        if gorev["tamamlandi"]:
            durum = "✓"
        else:
            durum = " "
        print(f"[{durum}] {gorev['gorev_id']} {gorev['baslik']}")


def gorev_tamamla(gorev_id):
    for gorev in gorevler:
        if gorev["gorev_id"] == gorev_id:
            gorev["tamamlandi"] = True
            return True
    return False


def gorev_sil(gorev_id):
    for gorev in gorevler:
        if gorev["gorev_id"] == gorev_id:
            gorevler.remove(gorev)
            return True
    return False


def gorevleri_kaydet():
    with open("gorevler.json", "w", encoding="utf-8") as dosya:
        json.dump(gorevler, dosya, ensure_ascii=False, indent=4)


def gorevleri_yukle():
    global gorevler, id_sayacı
    try:
        with open("gorevler.json", "r", encoding="utf-8") as dosya:
            gorevler = json.load(dosya)
    except FileNotFoundError:
        gorevler = []

    if gorevler:
        id_sayacı = max(gorev["gorev_id"] for gorev in gorevler) + 1
    else:
        id_sayacı = 1


def menu_goster():
    print("\n    Görev Takip Uygulaması   ")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görevi Tamamla")
    print("4. Görev Sil")
    print("5. Çıkış")


def main():
    gorevleri_yukle()

    while True:
        menu_goster()
        secim = input("Seçim: ")

        match secim:
            case "1":
                baslik = input("Baslik giriniz: ")
                gorev = gorev_ekle(baslik)
                print(f"'{gorev['baslik']}' görevi eklendi.")
            case "2":
                gorevleri_yazdir(gorev_listele())
            case "3":
                try:
                    gorev_id = int(input("Tamamlanacak görev numarası: "))
                    if gorev_tamamla(gorev_id):
                        print(f"{gorev_id} numaralı görev tamamlandı")
                    else:
                        print("Hata: görev bulunamadı")
                except ValueError:
                    print("Hata: Geçerli bir numara girmelisiniz.")
            case "4":
                try:
                    gorev_id = int(input("Silinecek görev numarası: "))
                    if gorev_sil(gorev_id):
                        print(f"{gorev_id} li görev çıkarıldı")
                    else:
                        print("Hata: görev bulunamadı")
                except ValueError:
                    print("Hata: Geçerli bir numara girmelisiniz.")
            case "5":
                gorevleri_kaydet()
                print("Görevler kaydedildi")
                break
            case _:
                print("Hata: Geçersiz seçim, 1 ile 5 arası sayı giriniz")


if __name__ == "__main__":
    main()