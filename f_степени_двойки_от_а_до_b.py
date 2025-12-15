def check(a):
    k=0
    while a!=1:
        k=a%2
        a//=2
        if k:
            return False
    return True

a=int(input())
b=int(input())
for i in range(a,b+1):
    if check(i):
        print(i, end=" ")