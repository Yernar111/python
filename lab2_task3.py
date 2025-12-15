class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def push_back(n,head):
    new = Node(n)
    last = head
    while last.next:
        last=last.next
    last.next=new

def write(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
        if current:
             current = current.next



n=int(input())
k=list(map(int, input().split()))
a=Node(k[0])

for i in k[1:]:
    push_back(i,a)

write(a)
