class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        next_data = Node(data)
        if not self.head:
            self.head = next_data
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = next_data

    def kopaytirish(self):
        current = self.head
        product = 1
        while current:
            product *= current.data
            current = current.next
        return product

l = LinkedList()
l.append(2)
l.append(3)
l.append(4)
print("Kopaytma:", l.kopaytirish()) 
