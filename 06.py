

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

    def manfiy_del(self):
        while self.head and self.head.data < 0:
            self.head = self.head.next
        
        current = self.head
        while current and current.next:
            if current.next.data < 0:
                current.next = current.next.next
            else:
                current = current.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

l = LinkedList()
elements = [12, -5, 8, -3, 4]
for element in elements:
    l.append(element)

l.manfiy_del()
print("Manfiy sonlarsiz:", l.to_list())
