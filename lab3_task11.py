n,m = map(int,input().split())
a=list(map(int,input().split()))
b=[0]*(n+1)
for i in range(1,n+1):
    b[i]=b[i-1]+a[i-1]

l=1; r=len(a)
while l<=r:
    mid=(l+r)//2
    for i in range(mid,n+1):
        cur=b[i]-b[i-mid]
        if cur>=m:
            ans=mid
            r=mid-1
            break
    else:
        l=mid+1
    
print(ans)



