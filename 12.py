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

    def swap_min_max(self):
        if not self.head:
            return
        
        min_node = max_node = self.head
        current = self.head

        while current:
            if current.data < min_node.data:
                min_node = current
            if current.data > max_node.data:
                max_node = current
            current = current.next

        if min_node != max_node:
            min_node.data, max_node.data = max_node.data, min_node.data

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Almashtirilgan:", elements)

ll = LinkedList()
ll.append(4)
ll.append(1)
ll.append(7)
ll.append(3)
ll.append(9)
ll.swap_min_max()
ll.display()  

#gpt