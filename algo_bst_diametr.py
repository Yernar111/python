# Найти максимальное расстояние между любыми двумя узлами(количество узлов).
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
    else:
        a.right = insert(a.right, k)
    return a

def check(a):
    global c
    if not a:
        return 0
    left=check(a.left) # Глубина левого поддерева(количество узлов)
    right=check(a.right) # Глубина правого поддерева(количество узлов)
    c=max(c,left+right+1) # Наибольшее расстояние проходящее через текущий корень это сумма узлов в левом и правом поддереве плюс 1(текущий корень). Сравниваем все это с предыдущим максимумом
    return 1+max(left,right) # Возвращаем максимальную глубину текущего поддерева(выбираем между левым и правым). При суммировании добавляем 1 так как считаем и сам корень 


n=int(input())
b=list(map(int,input().split()))
a=None
for i in b:
    a=insert(a,i)
c=0 # Хранит в себе наибольшее расстояние между двумя узлами
check(a)
print(c)