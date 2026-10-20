# Совершенный вид связного списка
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def push_back(n,tail):
    if not tail:
        global head
        head = tail = Node(n)
        return tail
    new = Node(n)
    new.prev = tail
    tail.next = new
    #tail = new
    return new

def push_front(n,head):
    if not head:
        global tail
        head = tail = Node(n)
        return head
    new = Node(n)
    new.next = head
    head.prev = new
    #head = new
    return new

def pop_back(tail):
    if not tail:
        return None
    tail = tail.prev
    tail.next = None
    return tail

def pop_front(head):
    if not head:
        return None
    head = head.next
    head.prev=None
    return head


a=list(map(int,input("push_back: ").split()))

head=None; tail = None

for i in a:
    tail=push_back(i,tail)

a=list(map(int,input("push_front: ").split()))

for i in a:
    head=push_front(i,head)

current=head
while current:
    print(current.data, end=" ")
    current=current.next

tail=pop_back(tail)
head=pop_front(head)

print()

current=head
while current:
    print(current.data, end=" ")
    current=current.next
