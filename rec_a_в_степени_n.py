def check(a,n):
    if n==1:
        return a
    return check(a,n-1)*a
    

a=int(input())
n=int(input())
print(check(a,n))