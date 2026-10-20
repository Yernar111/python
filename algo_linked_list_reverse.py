class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def push_back(n,head):
    if not head:
        return Node(n) # После первой итерации переменная становится обьектом класса Node.
    new = Node(n) 
    last = head # Операции над переменной отразятся на атрибутах оригинального обьекта
    while last.next:
        last=last.next
    last.next=new
    return head # Голова никак не поменялась но все равно возвращаем значение. 

def reverse(head):
    prev = None
    current = head
    while current:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
    return prev # Новой головой становится prev

def write(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next


a = None
k=list(map(int, input().split()))

for i in k:
    a = push_back(i,a)

a = reverse(a)

write(a)
