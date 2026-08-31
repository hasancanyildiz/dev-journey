class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Boş kuyruk, çıkarılacak eleman yok!")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Test
kuyruk = Queue()
kuyruk.enqueue("Ali")
kuyruk.enqueue("Ayşe")
kuyruk.enqueue("Mehmet")

print("Boyut:", kuyruk.size())
print("Dequeue:", kuyruk.dequeue())
print("Dequeue:", kuyruk.dequeue())
print("Boyut:", kuyruk.size())
print("Boş mu?", kuyruk.is_empty())