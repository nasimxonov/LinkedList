

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

    def remove_dup(self):
        current = self.head
        prev = None
        s_d = set()
        while current:
            if current.data in s_d:
                prev.next = current.next
            else:
                s_d.add(current.data)
                prev = current
            current = current.next

    def print(self):
        elementlar = []
        current = self.head
        while current:
            elementlar.append(current.data)
            current = current.next
        print("Dublikatsiz:", elementlar)

l = LinkedList()
l.append(1)
l.append(2)
l.append(2)
l.append(3)
l.append(4)
l.append(4)
l.append(5)
l.remove_dup()
l.print() 