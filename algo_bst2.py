# Дерево бинарного поиска с вставкой новых элементов и поиском минимума и максимума
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(a,k):
    if not a:
        return Node(k)
    if k<a.data:
        a.left = insert(a.left, k) 
    elif k>a.data:
        a.right = insert(a.right, k)
    return a

def search_min(a):
    current = a
    while current.left:
        current=current.left
    return current.data

def search_max(a):
    current=a
    while current.right:
        current=current.right
    return current.data

b=list(map(int,input().split()))
a=None
for i in b:
    a=insert(a,i)

print(search_min(a))
print(search_max(a))