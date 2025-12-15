# Ќайти наиболее подход€щий индекс дл€ числа K в отсортированном массиве
n = int(input())
k = int(input())
a=[]
for i in range(n):
    t=int(input())
    a.append(t)
a.sort()
if k<a[0]:
    print(0)
elif k>a[len(a)-1]:
    print(len(a)-1)
else:
    for i in range(1,len(a)):
        if k==a[i]:
            print(i)
            break
        elif k>a[i-1] and k<a[i]:
            print(i)
            break

