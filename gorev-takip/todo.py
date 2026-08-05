import json

gorevler = []


def gorev_ekle(baslik):
    yeni_id = len(gorevler) + 1
    gorev = {
        "id": yeni_id,
        "baslik": baslik,
        "tamamlandi": False
    }
    gorevler.append(gorev)
    print(f"'{baslik}' görevi eklendi.")


def gorev_listele():
    if not gorevler:
        print("Görev yok")
        return
    for gorev in gorevler:
        if gorev["tamamlandi"] == True:
            durum = "✓"
        else:
            durum = " "
        print(f"[{durum}] {gorev['id']} {gorev['baslik']}")


def gorev_tamamla(id):
    for gorev in gorevler:
        if gorev["id"] == id:
            gorev["tamamlandi"] = True
            print(f"{id} numarali görev tamamlandı")
            return
    print(f"Hata görev bulunamadı")


def gorev_sil(id):
    for gorev in gorevler:
        if gorev["id"] == id:
            gorevler.remove(gorev)
            print(f"{id} li görev çıkarıldı")
            return
    print(f"Hata görev bulunamadı")


def gorevleri_kaydet():
    with open("gorevler.json", "w", encoding="utf-8") as dosya:
        json.dump(gorevler, dosya, ensure_ascii=False, indent=4)


def gorevleri_yukle():
    global gorevler
    try:
        with open("gorevler.json", "r", encoding="utf-8") as dosya:
            gorevler = json.load(dosya)
    except FileNotFoundError:
        gorevler = []


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
                gorev_ekle(baslik)
            case "2":
                gorev_listele()
            case "3":
                try:
                    id = int(input("Tamamlanacak görev numarası: "))
                    gorev_tamamla(id)
                except ValueError:
                    print("Hata: Geçerli bir numara girmelisiniz.")
            case "4":
                try:
                    id = int(input("Silinecek görev numarası: "))
                    gorev_sil(id)
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