n = int(input())
a=[]
for i in range(n):
    t=int(input())
    a.append(t)

m,k=0,0
for i in range(len(a)):
    if a[i]>m:
        k=m
        m=a[i]
    elif a[i]>k and a[i]<m:
        k=a[i]
print(k)