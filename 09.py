

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

    def double_elements(self):
        current = self.head
        while current:
            current.data *= 2
            current = current.next

    def print(self):
        elementlar = []
        current = self.head
        while current:
            elementlar.append(current.data)
            current = current.next
        print("Kopaytirilgan:", elementlar)

l = LinkedList()
l.append(3)
l.append(6)
l.append(9)
l.double_elements()
l.print() 
