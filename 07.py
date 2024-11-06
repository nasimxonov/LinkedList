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

    def average(self):
        current = self.head
        total = 0
        count = 0
        while current:
            total += current.data
            count += 1
            current = current.next
        return total / count if count > 0 else 0

l = LinkedList()
l.append(5)
l.append(10)
l.append
