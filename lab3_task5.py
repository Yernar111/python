n,m = map(int, input().split())
a=[]
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    a.append(max(x2,y2))

l=1; r=10**9
ans = r
while l<=r:
    mid = (l+r)//2
    t=0
    for i in range(n):
        if a[i]<=mid:
            t+=1
    if t>=m:
        ans=mid
        r=mid-1
    else:
        l=mid+1
print(ans)

    

