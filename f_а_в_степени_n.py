# Только для положительного/отрицательного основания и положительной показатели степени
def check(a,n):
    k=1
    for i in range(n):
        k*=a
    return k
        
a=int(input())
n=int(input())
print(check(a,n))