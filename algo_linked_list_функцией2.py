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

def push_front(n):
    global head
    new = Node(n)
    new.next = head
    head = new

def write(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next


k=list(map(int, input("push_back: ").split()))
head=Node(k[0])
for i in k[1:]:
    push_back(i,head)

m=list(map(int, input("push_front: ").split()))
for i in m:
    push_front(i)

write(head)
