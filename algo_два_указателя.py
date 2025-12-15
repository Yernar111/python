# Два указателя для нахождения индексов пары чисел в отсортированном массиве сумма которых равна числу target
a=list(map(int,input().split()))
target=int(input())
a.sort()
l=0; r=len(a)-1
while l<r:
    if a[l]+a[r]>target:
        r-=1
    elif a[l]+a[r]<target:
        l+=1
    else:
        print(l,r)
        break
else:
    print(-1)
