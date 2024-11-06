class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        next = Node(data)
        if not self.head:
            self.head = next
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = next

    def juft_toq(self):
        juft = 0
        toq = 0
        current = self.head
        while current:
            if current.data % 2 == 0:
                juft += 1
            else:
                toq += 1
            current = current.next
        return juft, toq

l = LinkedList()
elements = [12, 5, 8, 7, 4, 9]
for element in elements:
    l.append(element)

juft, toq = l.juft_toq()
print("Juft sonlar:", juft)
print("Toq sonlar:", toq)
