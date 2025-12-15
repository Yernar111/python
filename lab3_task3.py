def binary_search1(a,m):
    s=0; f=len(a)-1; ans = len(a)
    while s<=f:
        mid = (s+f)//2
        if a[mid]>=m:
            ans = mid
            f = mid-1
        else:
            s=mid+1
    return ans

def binary_search2(a,m):
    s=0; f=len(a)-1; ans = -1
    while s<=f:
        mid = (s+f)//2
        if a[mid]<=m:
            ans = mid
            s=mid+1
        else:
            f=mid-1
    return ans



n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in range(m):
    l1,r1,l2,r2 = map(int, input().split())
    L1 = binary_search1(a,l1)
    R1 = binary_search2(a,r1)
    t1 = max(0, R1-L1+1)

    L2 = binary_search1(a,l2)
    R2 = binary_search2(a,r2)
    t2 = max(0,R2-L2+1) 

    L=max(l1,l2)
    R=min(r1,r2)
    t3 = 0
    if L<=R: 
        li = binary_search1(a,L)
        ri = binary_search2(a,R)
        t3 = max(0,ri-li+1) 
    print(t1+t2-t3)