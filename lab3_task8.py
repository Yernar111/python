n,m = map(int,input().split())
a=list(map(int,input().split()))
b=[0]*(len(a))
b[0]=a[0]
for i in range(1,len(a)):
    b[i]=a[i]+b[i-1]

for i in range(m):
    k=int(input())
    l=0; r=len(a)-1; ans = r
    while l<=r:
        mid = (l+r)//2
        if k<=b[mid]:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    print(ans+1)