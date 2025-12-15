# Tree Traversal(обход дерева) - способ последовательно посетить все узлы дерева(поддерева) в определенном порядке.
# Pre-order - сначала посещаем текущий корень(выводим), затем обходим левое поддерево и в конце правое. Для каждого поддерева также сначала посещаем(выводим) корень, а затем выполняем следующие шаги. 
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

def search(a,m):
    if m==a.data :
        return a
    elif m<a.data:
        return search(a.left, m)
    elif m>a.data:
        return search(a.right, m)

def preorder(a):
    if not a:
        return
    print(a.data, end=" ")
    preorder(a.left)
    preorder(a.right)



n=int(input())
b=list(map(int,input().split()))
a=None
for i in b:
    a=insert(a,i)

m=int(input())
k=search(a,m)
preorder(k)