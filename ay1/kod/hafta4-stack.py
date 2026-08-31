class Stack:
    def __init__(self):
        self.items =[]

    def push (self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Boş stack,eleman çıkarılamaz")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("stack boş")
            return None
        return self.items[-1]#son eleman çıkarılır.

    def is_empty(self):
        return   len(self.items)==0
    def size (self):
        return len(self.items)


# Test
yigin = Stack()
yigin.push(1)
yigin.push(2)
yigin.push(3)

print("Boyut:", yigin.size())
print("Üstteki eleman (peek):", yigin.peek())

print("Pop:", yigin.pop())
print("Pop:", yigin.pop())

print("Boyut:", yigin.size())
print("Boş mu?", yigin.is_empty())