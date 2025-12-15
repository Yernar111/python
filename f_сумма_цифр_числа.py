def check(n):
    k=0
    while n!=0:
        k+=n%10
        n//=10
    return k

    
        
n=int(input())
print(check(n))