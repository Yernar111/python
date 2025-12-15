# Создаем dictionary ключ которого индекс, а значение это число Фибоначчи под этим индексом. С помощью этого можно сохранить значение i-того числа Фибоначчи в памяти и не вычислять повторно
def check(n,a={}):
    if n<=2:
        return 1
    if n in a:
        return a[n]

    a[n]=check(n-1, a)+check(n-2, a)
    return a[n]

n=int(input())
print(check(n))