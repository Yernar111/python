class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # ссылка на следующий узел

class LinkedList:
    def __init__(self):
        self.head = None  # начало списка

    # добавление в начало
    def push_front(self, data):
        new_node = Node(data) # Создание нового узла
        new_node.next = self.head # Узел будет ссылаться в текущий хед(который был до появления этого узла)
        self.head = new_node # Новым хедом становится созданный узел

    # добавление в конец
    def push_back(self, data):
        new_node = Node(data) # Создание нового узла
        if not self.head:
            self.head = new_node # Если список пуст то хедом становится созданный узел
            return
        last = self.head # Проходимся по всем элементам до конца списка
        while last.next:
            last = last.next 
        last.next = new_node # last.next является подобием контейнера который хранит в себе узел

    # вывод списка
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# пример использования
ll = LinkedList()
ll.push_back(10)
ll.push_back(20)
ll.push_front(5)
ll.print_list()  # 5 -> 10 -> 20 -> None