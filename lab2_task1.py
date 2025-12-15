class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input())
a=None; tail = None
k=list(map(int, input().split()))
a = tail = Node(k[0])
for i in range(1,n):
    new = Node(k[i])
    tail.next = new
    tail = new

m=int(input())
ind = 1; z = 0
min_= abs(a.data - m)
current = a.next
while current:
    if (abs(current.data-m)<min_):
        min_=abs(current.data-m)
        z = ind
    ind+=1
    current = current.next

print(z)

