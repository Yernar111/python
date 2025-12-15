# Решение задачи ax+by=gcd(a,b) с помощью расширенного алгоритма Эвклида. 
# Решение является рекурсивным. Во время выполнения рекурсии мы находим gcd(a,b) такой что b=0, a=gcd(a,b). Далее выведенная формула позволяет найти x и y для текущего a и b. 

def check(a,b):
    if b==0:
        return a,1,0
    gcd,x1,y1=check(b,a%b)
    x=y1
    y=x1-a//b*y1
    return gcd,x,y

a=int(input())
b=int(input())
gcd,x,y=check(a,b)
print(x,y)