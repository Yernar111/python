n = int(input())
a=[]
t=int(input())
a.append(t)
m=k=a[0]
h=j=0
for i in range(1,n):
    t=int(input())
    a.append(t)
    if a[i]>m:
        m=a[i]
        h=i
    if a[i]<k:
        k=a[i]
        j=i

a[h]=k
a[j]=m
print(a)
