class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def push_back(n,head):
    new = Node(n)
    last = head # Переменная которая хранит в себе ссылку на обьект класса. Через эту переменную можно получать доступ к атрибутам обьекта через точку и изменять их.
    while last.next:
        last=last.next
    last.next=new

def write(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next


n=int(input())
k=list(map(int, input().split()))
a=Node(k[0])
for i in k[1:]:
    push_back(i,a)

write(a)
