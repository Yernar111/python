# Алгоритм для выведения всех простых чисел не превосходящих N.
n=int(input())
a=[1]*(n+1)
for i in range(2,len(a)):
    if a[i]==1:
        print(i, end=" ")
        j=i*i
        while j<len(a):
            a[j]=0
            j+=i
