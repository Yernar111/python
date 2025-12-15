class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None   # ссылка на предыдущий узел
        self.next = None   # ссылка на следующий узел


# Добавление в начало
def push_front(value):
    global a
    if not a:
        a = Node(value)
        return
    new_node = Node(value)
    new_node.next = a
    a.prev = new_node # новая голова
    a = new_node


# Добавление в конец
def push_back(value):
    global a
    if not a:
        a = Node(value)
        return
    new_node = Node(value)
    temp = a
    while temp.next:   # ищем последний элемент
        temp = temp.next
    temp.next = new_node
    new_node.prev = temp

def pop_back():
    global a
    if not a:
        print("empty")
        return
    temp = a
    if not temp.next:
        a = None
        return
    while temp.next.next:
        temp = temp.next
    temp.next = None

# Удаление первого элемента
def pop_front():
    global a
    if not a:
        print("empty")
        return
    a = a.next
    a.prev = None


# Вывод слева направо
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


# Вывод справа налево
def print_backward():
    global a
    if not a:
        print("empty")
        return
    temp = a
    while temp.next:   # идем в конец
        temp = temp.next
    while temp:        # идем назад
        print(temp.data, end=" ")
        temp = temp.prev
    print()


m=list(map(int, input("push_back: ").split()))

a = None

for i in m:
    push_back(i)

m=list(map(int, input("push_front: ").split()))

for i in m:
    push_front(i)

print_forward()
"\n"
print_backward()

pop_front()
pop_back()

print_forward()
"\n"
print_backward()

pop_front()
pop_back()
print_backward()
