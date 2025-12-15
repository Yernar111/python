def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

n=int(input())
m=int(input())
print(gcd(n,m))