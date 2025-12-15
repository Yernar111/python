def check(a,n):
    b=[0]*n
    for i in range(n):
        a.append(int(input()))
    b[0]=a[0]
    for i in range(1,n):
        b[i]=b[i-1]+a[i]
    return b
    
n=int(input())    
a=[]*n
print(check(a,n))