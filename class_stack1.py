# Реализация стэка через классы
class stack():
    def __init__(self):
        self.a=[]
    def push(self, n):
        self.a.append(n)
    def pop(self):
        if self.a:
            return self.a.pop()
        return None
    def top(self):
        if self.a:
            return self.a[-1]
        return None
    def is_empty(self):
        if self.a:
            return False
        return True
    

a = stack()

n=int(input())
a.push(n)
while (not a.is_empty()):
    k=str(input())
    if k=="push":
        m=int(input())
        a.push(m)
    elif k=="pop":
        a.pop()
    elif k=="top":
        print(a.top())