class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.summa = 0

    def append(self, data):
        new_node = Node(data)
        self.summa += data 
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def sum(self):
        return self.summa

l = LinkedList()
elements = [10, -3, 5, 8, 6]
for element in elements:
    l.append(element)

print("Yigindi:", l.sum())
