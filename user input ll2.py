class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


nodes = []

for i in range(4):
    nodes.append(Node(int(input("Enter value: "))))


for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]


head = nodes[0]


current = head

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")