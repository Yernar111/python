class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None   
        self.next = None   



def push_front(value):
    global a
    if not a:
        a = Node(value)
        return
    new_node = Node(value)
    new_node.next = a
    a.prev = new_node 
    a = new_node


def push_back(value):
    global a
    if not a:
        a = Node(value)
        return
    new_node = Node(value)
    temp = a
    while temp.next:   
        temp = temp.next
    temp.next = new_node
    new_node.prev = temp

def pop_back():
    global a
    temp = a
    if not temp.next:
        print(temp.data)
        a = None
        return
    while temp.next.next:
        temp = temp.next
    print(temp.next.data)
    temp.next = None

def pop_front():
    global a
    a = a.next
    if a:
        a.prev = None


def print_forward():
    global a
    if not a:
        print("empty")
        return
    temp = a
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


def print_backward():
    global a
    if not a:
        print("empty")
        return
    temp = a
    while temp.next:   
        temp = temp.next
    while temp:        
        print(temp.data, end=" ")
        temp = temp.prev
    print()

def back():
    global a
    temp = a
    while temp.next:
        temp=temp.next
    print(temp.data)


a = None

i=["string"]
while i[0]!="exit":
    i=input().split()
    if i[0]=="add_front":
        push_front(i[1])
        print("ok")
    elif i[0]=="add_back":
        push_back(i[1])
        print("ok")
    elif i[0]=="erase_front":
        if a:
            print(a.data)
            pop_front()
        else:
            print("error")
    elif i[0]=="erase_back":
        if a:
            pop_back()
        else:
            print("error")
    elif i[0]=="front":
        if a:
            print(a.data)
        else:
            print("error")
    elif i[0]=="back":
        if a:
            back()
        else:
            print("error")
    elif i[0]=="clear":
        a = None
        print("ok")
    elif i[0]=="exit":
        print("goodbye")