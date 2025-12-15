def check(a,i,k,m):
    if i==len(a):
        return k
    if a[i]>m:
        return check(a,i+1,1,a[i])
    if a[i]==m:
        return check(a,i+1,k+1,m)
    return check(a,i+1,k,m)
    


n=int(input())
a=input().split()
b=[0]*n
for i in range(n):
    b[i]=int(a[i])
print(check(b,1,1,b[0]))