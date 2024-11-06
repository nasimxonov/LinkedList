

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

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

l = LinkedList()
elements = [4, 9, 2, 7]
for element in elements:
    l.append(element)

l.reverse()
print("Teskari:", l.to_list())
