# Если К положительное: подвинуть вправо, иначе влево
def check(a,k):
    for i in range(len(a)-k,len(a)):
        print(a[i], end=" ")
    for i in range(len(a)-k):
        print(a[i], end=" ")

def check1(a,k):
    for i in range(k,len(a)):
        print(a[i], end=" ")
    for i in range(k):
        print(a[i], end=" ")

n=int(input())
k=int(input())
a=[]
for i in range(n):
    t=input()
    a.append(t)
if k>=0:
    check(a,k)
else:
    check1(a,abs(k))