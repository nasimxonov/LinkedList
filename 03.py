

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

    def max(self):
        if not self.head:
            return None
        maxx = self.head.data
        current = self.head.next
        while current:
            if current.data > maxx:
                maxx = current.data
            current = current.next
        return maxx

ll = LinkedList()
elements = [3, 15, 7, 2, 9]
for element in elements:
    ll.append(element)

max_element = ll.max()
print("Eng katta element:", max_element)
