# Есть дерево бинарного поиска, надо найти количество единичных треугольников. Единичные треугольники в дереве получаются когда рисуешь горизонтальную линию между двумя узлами имеющих одного родителя 
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(a, k):
    if not a:
        return Node(k)
    if k<a.data:
        a.left = insert(a.left, k) 
    elif k>a.data:
        a.right = insert(a.right, k)
    return a

def order(a):
    global c
    if not a:
        return
    if a.left and a.right:
        c+=1
    if a.left:
        order(a.left)
    if a.right:
        order(a.right)



n=int(input())
b=list(map(int,input().split()))
a=None
for i in b:
    a=insert(a,i)
c=0
order(a)
print(c)