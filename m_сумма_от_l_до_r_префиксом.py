n = int(input())
l = int(input())
r = int(input())
a=[0]*n
b=[0]*(r+1)
for i in range(n):
    t=int(input())
    a[i]=t
b[0]=a[0]
for i in range(1,r+1):
    b[i]=b[i-1]+a[i]
print(a)
if l==0:
    print(b[r])
else:
    print(b[r]-b[l-1])
