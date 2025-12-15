class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input())
k=int(input())
a = tail = Node(k)
for i in range(1,n):
    k=int(input())
    new = Node(k)
    tail.next = new
    tail = new

m=int(input())
p=int(input())
new = Node(m)
if p==0:
    new.next = a
    a = new
else:
    ind = 0
    current = a
    while ind<p-1:
        ind+=1
        current = current.next
    new.next = current.next
    current.next = new

current = a
while current:
    print(current.data, end=" ")
    current = current.next

