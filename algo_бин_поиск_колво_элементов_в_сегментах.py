# Дается отсортированный массив чисел и M пар сегментов значении (l1,r1) и (l2,r2). Надо найти количество элементов в массиве лежащих между значениями сегментов. Гарантируется что значения сегментов есть в самом массиве  min(a)<=l<=a[i]<=r<=max(a)
def binary_search(a,m):
    s=0; f=len(a)-1
    while s<=f:
        mid = (s+f)//2
        if a[mid]>m:
            f = mid-1
        elif a[mid]<m:
            s=mid+1
        else:
            return mid


n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in range(m):
    l1,r1,l2,r2 = map(int, input().split()) # Ищем индексы сегментов с помощью бинарного поиска
    L1 = binary_search(a,l1)
    R1 = binary_search(a,r1)
    t1 = R1-L1+1 # Количество элементов между L1 и R1 (сегментами l1 и r1)

    L2 = binary_search(a,l2)
    R2 = binary_search(a,r2)
    t2 = R2-L2+1 # Количество элементов между L2 и R2 (сегментами l2 и r2)

    L=max(l1,l2) 
    R=min(r1,r2)
    t3 = 0
    if L<=R: # Если отрезки пересекаются
        li = binary_search(a,L) # Находим индексы сегментов  
        ri = binary_search(a,R)
        t3 = ri-li+1 # Количество элементов между ri и li
    print(t1+t2-t3) # Если сегменты не пересекаются то отнимаем 0, иначе отнимаем количество элементов между li и ri
    

