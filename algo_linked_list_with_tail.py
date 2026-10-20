class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input())
head=None; tail = None
for i in range(n):
    k=int(input())
    if not head:
        head = tail = Node(k)
        continue
    new = Node(k)
    tail.next = new
    tail = new

current = head
while current:
    print(current.data, end=" ")
    current = current.next

