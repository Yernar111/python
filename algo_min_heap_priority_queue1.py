# Priority queue, Optimal Merge pattern. Стоимость слияния двух элементов массива является x+y, при слиянии два элемента становятся одним(то есть суммируются и вставляются в массив). Необходимо делать слияние пока не останется один элемент и найти минимальную стоимость после всех операции
def insert(x):
    heap.append(x)
    i=len(heap)-1 

    while i>0: 
        parent = (i-1)//2 
        if heap[parent]>heap[i]:
            heap[parent],heap[i]=heap[i],heap[parent]
            i=parent 
        else:
            break 

def extract_min(): 
    if not heap:
        return 0
    if len(heap)==1:
        return heap.pop()
    a=heap[0] 
    heap[0]=heap.pop()
    i=0
    while True:
        smallest=i 
        left = 2*i+1
        right = 2*i+2

        if left<len(heap) and heap[left]<heap[smallest]:
            smallest = left
        if right<len(heap) and heap[right]<heap[smallest]:
            smallest=right
        if smallest==i:
            break
        heap[i],heap[smallest]=heap[smallest],heap[i] 
        i=smallest 
    return a 


heap=[]
n=int(input())
a=list(map(int,input().split()))
for i in a:
    insert(i)
t=0
while len(heap)>1: # Если длина равна единице, значит больше не осталось пар элементов с которыми можно сделать слияние(длина не может быть меньше 1)
    x=extract_min()
    y=extract_min()
    t+=(x+y) # Суммируем два минимальных элемента массива и добавляем к общей сумме
    insert(x+y) # Вставляем в массив сумму двух удаленных элементов
print(t)


