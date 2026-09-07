# Node
# Bağlı listenin tek bir düğümünü (elemanını) temsil eder.
# data: düğümün tuttuğu değer.
# next: bir sonraki düğüme referans; henüz bağlı değilse None.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList (Singly Linked List)
# head, listenin ilk düğümüne referans tutar. Liste boşsa head None'dır.
class LinkedList:
    def __init__(self):
        self.head = None

    # insert: listenin sonuna yeni bir değer ekler.
    def insert(self, data):
        yeni_node = Node(data)

        if self.head is None:
            self.head = yeni_node
            return

        simdiki = self.head
        while simdiki.next is not None:
            simdiki = simdiki.next
        simdiki.next = yeni_node

    # search: verilen değeri listede arar. Bulursa True, bulamazsa False döner.
    def search(self, data):
        simdiki = self.head
        while simdiki is not None:
            if simdiki.data == data:
                return True
            simdiki = simdiki.next
        return False

    # delete: verilen değere sahip ilk düğümü listeden çıkarır.
    def delete(self, data):
        onceki = None
        simdiki = self.head

        while simdiki is not None:
            if simdiki.data == data:
                if onceki is None:
                    # silinecek düğüm head ise, head'i bir sonrakine kaydır
                    self.head = simdiki.next
                else:
                    # onceki düğümü, silinecek düğümü atlayıp bir sonrakine bağla
                    onceki.next = simdiki.next
                return True
            onceki = simdiki
            simdiki = simdiki.next
        return False

    # print_liste: listenin tüm elemanlarını baştan sona yazdırır.
    def print_liste(self):
        simdiki = self.head
        if simdiki is None:
            print("Liste boş")
            return

        cikti = ""
        while simdiki is not None:
            cikti = cikti + str(simdiki.data)
            if simdiki.next is not None:
                cikti = cikti + " -- "
            simdiki = simdiki.next

        print(cikti)

    # reverse: listenin yönünü tersine çevirir (head sondan başa döner).
    def reverse(self):
        onceki = None
        simdiki = self.head

        while simdiki is not None:
            sonraki = simdiki.next   # bir sonraki düğümü kaybetmeden önce sakla
            simdiki.next = onceki    # şu anki düğümün yönünü tersine çevir
            onceki = simdiki         # önceki'yi bir ileri taşı
            simdiki = sonraki        # şu anki'yi bir ileri taşı

        self.head = onceki  # liste tersine döndüğü için yeni head, eski son düğüm


# Test
if __name__ == "__main__":
    liste = LinkedList()
    liste.insert(10)
    liste.insert(20)
    liste.insert(30)
    liste.print_liste()          # 10 -- 20 -- 30

    print(liste.search(30))      # True (artık son eleman da doğru bulunuyor)
    print(liste.search(99))      # False

    liste.delete(20)
    liste.print_liste()          # 10 -- 30

    liste.reverse()
    liste.print_liste()          # 30 -- 10