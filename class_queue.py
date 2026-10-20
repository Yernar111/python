# Реализация очереди через классы
# Очередь подходит для: Task scheduling in operating systems, BFS, print job management
class queue():
    def __init__(self):
        self.a=[]
    def push(self, n):
        self.a.append(n)
    def front(self):
        if a:
            return self.a[0]
        return None
    def pop(self):
        if a:
            return self.a.pop(0)
        return None
    def is_empty(self):
        if self.a:
            return False
        return True

a = queue()

n=int(input())
a.push(n)
while (not a.is_empty()):
    k=str(input())
    if k=="push":
        m=int(input())
        a.push(m)
    elif k=="front":
        print(a.front())
    elif k=="pop":
        a.pop()