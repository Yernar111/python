# Находм есть ли число в отсортированном массиве, если есть пишем индекс в котором лежит число. 
a=input().split()
n=input()
a.sort()
s=0
f=len(a)-1
m=(f+s)//2
while s<=f:
    if n>a[m]:
        s=m+1
    elif n<a[m]:
        f=m-1
    else:
        print(m)
        break
    m=(f+s)//2
else:
    print("No")
