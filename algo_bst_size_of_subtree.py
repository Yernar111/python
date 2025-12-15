# Найти количество элементов в поддереве корнем которого является элемент K(корень включительно).
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

def search(a,k): # Сначала ищем узел k
    if k==a.data :
        return a
    elif k<a.data:
        return search(a.left, k)
    elif k>a.data:
        return search(a.right, k)

def search_num(k):
    if not k: # Для пустоты возвращаем 0
        return 0 
    return 1+search_num(k.left)+search_num(k.right) # Плюсуем 1 так как корень тоже считаем 



n=int(input())
b=list(map(int,input().split()))
a=None
for i in b:
    a=insert(a,i)

m=int(input())
k=search(a,m)
print(search_num(k))
