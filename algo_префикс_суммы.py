a=list(map(int,input().split()))
l,r = map(int,input().split()))
b=[0]*(len(a))
b[0]=a[0]
for i in range(1,len(a)):
    b[i]=a[i]+b[i-1]

print(b[r]-b[l-1])

