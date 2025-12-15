def check(a,i,k,m):
    if i==len(a):
        return m
    if a[i]>k:
        return check(a,i+1,a[i],k)
    if a[i]>m and a[i]<k:
        return check(a,i+1,k,a[i])
    return check(a,i+1,k,m)

n=int(input())
a=[0]*n
for i in range(n):
    a[i]=int(input())
print(check(a,i=0,k=0,m=0))