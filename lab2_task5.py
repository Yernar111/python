class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.num=1

def push_back(n,head):
    last = head
    if last.data==n:
        return
    while last.next:
        if last.data==n or last.next.data==n:
            return
        last=last.next
    new = Node(n)
    last.next=new
    head.num+=1


def write(head):
    print("All in all:",head.num)
    print("Students: ")
    current = head
    while current:
        print(current.data)
        current = current.next


n=int(input())
k=input()
a=Node(k)
for i in range(1,n):
    k=input()
    push_back(k,a)

write(a)

