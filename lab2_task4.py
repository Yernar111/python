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

def mode(head):
    current = head
    while current:
        b[current.data]+=1
        current = current.next


n=int(input())
k=list(map(int, input().split()))
b=[0]*(max(k)+1)
a=Node(k[0])
for i in k[1:]:
    push_back(i,a)

mode(a)

max_=max(b)
for i in range(len(b)-1,0,-1):
    if b[i]==max_:
        print(i, end=" ")
