n = int(input())
a=[0]*n
b=[0]*n
for i in range(n):
    t=int(input())
    a[i]=t
b[0]=a[0]
for i in range(1,n):
    b[i]=b[i-1]+a[i]
print(a)
print(b)