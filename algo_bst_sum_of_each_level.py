# Вывести количество уровней в дереве, затем сумму значении каждого уровня по отдельности
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

def levels(a,i): # i - индекс текущего уровня, a - узел
    global num # Изначально равен одному, так как корень уже является первым уровнем
    if not a:
        return
    c[i]+=a.data
    levels(a.left,i+1) # Увеличиваем индекс так как спускаемся на следующий уровень
    levels(a.right,i+1)
    num=max(num,i+1) # Если мы спустились на уровень глубже чем в предыдущий раз, то теукщий уровень(i+1 так как уровни начинаются с одного, а индексы с нуля)


n=int(input())
b=list(map(int,input().split()))
a=None
for i in b:
    a=insert(a,i)
num=1 # Количество уровней
c=[0]*n # В худшем случае длина массива будет n(если вдруг элементы будут в убывающем или возрастающем порядке)
levels(a,0)
print(num)
for i in range(num):
    print(c[i],end=" ")