# Node
# Bağlı listenin tek bir düğümünü (elemanını) temsil eder.
# data: düğümün tuttuğu değer.
# next: bir sonraki düğüme referans; henüz bağlı değilse None.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev =None


# LinkedList (Singly Linked List)
# head, listenin ilk düğümüne referans tutar. Liste boşsa head None'dır.
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    # insert: listenin sonuna yeni bir değer ekler.
    def insert(self, data):
        yeni_node = Node(data)

        if self.head is None:
            self.head = yeni_node
            self.tail = yeni_node
            return

        simdiki = self.head
        while simdiki.next is not None:
            simdiki = simdiki.next
        simdiki.next = yeni_node
        yeni_node.prev=simdiki
        self.tail=yeni_node 

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
        simdiki=self.head

        while simdiki is not None:
            if simdiki.data== data:
                if simdiki.prev is None:
                    self.head =simdiki.next
                else:
                    simdiki.prev.next =simdiki.next
                if simdiki.next is None:
                    self.tail =simdiki.prev
                else :
                    simdiki.next.prev=simdiki.prev
                return True
            simdiki=simdiki.next
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


    def print_geriye(self):
        simdiki = self.tail
        if simdiki is None:
            print("Liste boş")
            return

        cikti = ""
        while simdiki is not None:
            cikti = cikti + str(simdiki.data)
            if simdiki.prev is not None:
                cikti = cikti + " -- "
            simdiki = simdiki.prev

        print(cikti)

    # reverse: listenin yönünü tersine çevirir (head sondan başa döner).
    def reverse(self):
        simdiki = self.head
        self.tail = self.head

        while simdiki is not None:
            sonraki = simdiki.next   # bir sonraki düğümü kaybetmeden önce sakla
            simdiki.next, simdiki.prev = simdiki.prev, simdiki.next

            if sonraki is None:
                self.head = simdiki
            simdiki = sonraki


# Test
if __name__ == "__main__":
    liste = LinkedList()
    liste.insert(10)
    liste.insert(20)
    liste.insert(30)
    liste.insert(40)
    print("İleri:")
    liste.print_liste()      # 10 -- 20 -- 30 -- 40

    print("Geri:")
    liste.print_geriye()     

    liste.delete(20)
    print("20 silindikten sonra ileri:")
    liste.print_liste()     
    print("20 silindikten sonra geri:")
    liste.print_geriye()     

    liste.reverse()
    print("Reverse sonrası ileri:")
    liste.print_liste()     
    print("Reverse sonrası geri:")
    liste.print_geriye()    
