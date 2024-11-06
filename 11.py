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

    def sort_linked_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        elements.sort()
        current = self.head
        for data in elements:
            current.data = data
            current = current.next

    def print(self):
        elementlar = []
        current = self.head
        while current:
            elementlar.append(current.data)
            current = current.next
        print("Sortlangan:", elementlar)

l = LinkedList()
l.append(9)
l.append(2)
l.append(7)
l.append(1)
l.append(5)
l.sort_linked_list()
l.print() 
