class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

# Connecting nodes
n1.next = n2
n2.next = n3
n3.next = n4

# Head points to first node
head = n1

# Traversing the linked list
current = head

while current is not None:
    print(current.data)
    current = current.next