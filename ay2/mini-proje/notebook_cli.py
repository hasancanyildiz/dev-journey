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

        baslik = input("Not başlığı: ")
        icerik = input("Not içeriği: ")

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