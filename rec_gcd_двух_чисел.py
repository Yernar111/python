def check(a,b):
    if b==0:
        return a
    return check(b,a%b)

n=int(input())
m=int(input())
print(check(n,m))
    