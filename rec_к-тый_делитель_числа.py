# К-тый делитель числа N
def check(n,k,i,t):
    if i==k:
        return t
    if n%(t+1)==0:
        return check(n,k,i+1,t+1)
    return check(n,k,i,t+1)
    

n=int(input())
k=int(input())
print(check(n,k,i=1,t=1))