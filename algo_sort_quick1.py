# Quick sort (hoare partition). 
def partition_hoare(arr, low, high):
    pivot = arr[(low + high) // 2]  # опорный элемент (medoid). Можно использовать рандомную опору.
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot: # двигаем i вправо, пока arr[i] < pivot. То есть когда элемент под индексом становится больше pivot останавливаемся на текущем индексе 
            i += 1
        j -= 1
        while arr[j] > pivot: # двигаем j влево, пока arr[j] > pivot. То есть когда элемент под индексом становится меньше pivot останавливаемся на текущем индексе 
            j -= 1
        if i >= j:
            return j # Возвращаем индекс который служит границой(местонахождением текущего pivot) (надо отсортировать все что до и после этого индекса)
        arr[i], arr[j] = arr[j], arr[i] # Меняем местами те элементы что больше и меньше pivot. Таким образом, к концу цикла все элементы меньше pivot будут слева, а те что больше - справа(не факт что отсортированы). 


def quicksort(arr, low, high):
    if low < high:
        p = partition_hoare(arr, low, high) # Граница между левой и правой частью которую мы собираемся отсортировать
        quicksort(arr, low, p)
        quicksort(arr, p + 1, high)


a=list(map(int,input().split()))
quick_sort(a,0,len(a)-1)
print(a)
