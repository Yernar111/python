def check(k,i,n):
    if (i==k):
        return n
    if check1(n+1):
        return check(k,i+1,n+1)
    return check(k,i,n+1)

def check1(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

k=int(input())
print(check(k,i=1,n=2))
    