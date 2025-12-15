# Утверждение что любое четное число больше двух можно представить в виде суммы двух простых чисел
def is_prime(a):
    for i in range(2,int(pow(a,0.5))+1):
        if a%i==0:
            return False
    return True

n=int(input())
for i in range(2,n):
    if is_prime(i) and is_prime(n-i):
        print(i,n-i)
        break
