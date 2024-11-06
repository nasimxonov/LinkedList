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

    def min(self):
        if not self.head:
            return None
        minn = self.head.data
        current = self.head.next
        while current:
            if current.data < minn:
                minn = current.data
            current = current.next
        return minn

ll = LinkedList()
elements = [7, -2, 5, 10, 1]
for element in elements:
    ll.append(element)

min_element = ll.min()
print("Eng kichik element:", min_element)
