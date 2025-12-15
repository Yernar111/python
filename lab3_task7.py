n,m = map(int,input().split())
a=list(map(int,input().split()))
l=1; r=max(a); ans=r
while(l<=r):
    mid=(l+r)//2
    t=0
    for i in range(n):
        t+=int((a[i]+mid-1)/mid)
    if t<=m:
        ans=mid
        r=mid-1
    else:
        l=mid+1
print(ans)

