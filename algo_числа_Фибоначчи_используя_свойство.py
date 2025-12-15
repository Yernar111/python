# Используем мемоизацию и свойство числа Фибоначчи с четным индексом F_2n = F_n * (F_n+1 + F_n-1)
def check(n,a={}):
    if n<=2:
        return 1
    if n in a:
        return a[n]
    
    if n%2==0:
        a[n]=check(n//2, a)*(check(n//2+1, a)+check(n//2-1, a))
        return a[n]

    a[n]=check(n-1, a)+check(n-2, a)
    return a[n]

n=int(input())
print(check(n))