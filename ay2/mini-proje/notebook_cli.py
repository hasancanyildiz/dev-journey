
class Not:

    def __init__(self, baslik, icerik):
        # Başlık
        self.baslik = baslik

        # İçerik
        self.icerik = icerik


class NoteManeger:

    def __init__(self):
        # Notların tutulacağı liste
        self.notlar = []

    def not_ekle(self):

        # .strip() ile başta/sonda kalan boşlukları temizliyoruz,
        # yoksa arama sırasında (orada strip yapıldığı için) eşleşme bulunamaz
        baslik = input("Not başlığı: ").strip()
        icerik = input("Not içeriği: ").strip()

        if not baslik:
            print("Başlık boş olamaz.\n")
            return

        yeni_not = Not(baslik, icerik)

        # Notu listeye ekle
        self.notlar.append(yeni_not)

        # Notları alfabetik sıraya koy
        self.notlar.sort(key=lambda not_: not_.baslik.lower())

        print("Not başarıyla eklendi.")

    def notlari_listele(self):
        if not self.notlar:
            print("Henüz hiç not yok.")
            return

        print("\n--- Notlar (alfabetik) ---")

        # indeks: 0'dan başlayıp listenin son elemanına kadar gider
        for indeks in range(len(self.notlar)):
            # indeks'teki notu listeden çekiyoruz
            not_ = self.notlar[indeks]

            # Kullanıcıya 1'den başlayarak göstermek için indeks + 1 yazıyoruz
            print(f"{indeks + 1}. {not_.baslik}")

        print()

    def not_ara(self):
        # Başlığa göre binary search ile arama yapar
        if not self.notlar:
            print("Aranacak yok")
            return
        aranan = input("Aranacak başlık: ").strip().lower()

        # alt üst: arama yapılan aralığın sınırları
        alt = 0
        ust = len(self.notlar) - 1

        while alt <= ust:
            # orta: aralığın tam ortasındaki indeks
            orta = (alt + ust) // 2
            orta_baslik = self.notlar[orta].baslik.lower()

            if orta_baslik == aranan:
                # Eşleşme bulundu, notu göster
                bulunan = self.notlar[orta]
                print(f"\nBulundu -> Başlık: {bulunan.baslik}")
                print(f"İçerik: {bulunan.icerik}\n")
                return
            elif orta_baslik < aranan:
                # Aranan sağ yarıda, alt sınırı ileri al
                alt = orta + 1
            else:
                # Aranan sol yarıda, üst sınırı geri al
                ust = orta - 1

        # Döngü bitti, eşleşme yok
        print("Bu başlıkta bir not bulunamadı.\n")

    def not_sil(self):
        # Önce mevcut notları numaralı göster
        self.notlari_listele()
        if not self.notlar:
            return
        try:
            # Kullanıcıdan silinecek notun numarasını al
            secim = int(input("Silinecek notun numarasını gir: "))
            if 1 <= secim <= len(self.notlar):
                # Numaradan 1 çıkar, gerçek liste indeksine ulaş
                silinen = self.notlar.pop(secim - 1)
                print(f"'{silinen.baslik}' silindi.\n")
            else:
                print("Geçersiz numara.\n")
        except ValueError:
            # Sayı yerine harf/boş girilirse buraya düşer
            print("Lütfen bir sayı gir.\n")


def menu():
    # Program açılınca tek bir yönetici nesnesi oluşturuluyor
    yonetici = NoteManeger()

    while True:
        # Menü seçenekleri her turda ekrana basılır
        print("""
1. Not Ekle
2. Not Ara (Binary Search)
3. Notları Listele
4. Not Sil
5. Çıkış
""")
        secim = input("Seçiminiz: ").strip()

        # Kullanıcının seçimine göre ilgili metod çağrılır
        if secim == "1":
            yonetici.not_ekle()
        elif secim == "2":
            yonetici.not_ara()
        elif secim == "3":
            yonetici.notlari_listele()
        elif secim == "4":
            yonetici.not_sil()
        elif secim == "5":
            print("Görüşürüz!")
            break
        else:
            print("Geçersiz seçim, tekrar dene.\n")


if __name__ == "__main__":
    # Dosya doğrudan çalıştırılırsa menüyü başlat
    menu()