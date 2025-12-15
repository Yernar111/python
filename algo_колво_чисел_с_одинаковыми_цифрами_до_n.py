# Количество чисел состоящих из одинаковыми цифр до N. (все однозначные числа состоят из 1 одинаковой цифрой)
m=int(input())
for i in range(m):
    n=input()
    k=(len(n)-1)*9
    h=int("1"*len(n))
    while h<=int(n):
        k+=1
        h+=int("1"*len(n))
    print(k)