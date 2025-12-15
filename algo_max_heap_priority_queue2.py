# Есть множество камней которые имеют вес a[i]. Берется две самых тяжелых камня x<=y и соединяются по следующему принципу: если они одинаковы то уничтожают друг друга, иначе вместо них становится остается камень вес которой равен y-x
def insert(x):
    heap.append(x)
    i=len(heap)-1 

    while i>0: 
        parent = (i-1)//2 
        if heap[parent]<=heap[i]:
            heap[parent],heap[i]=heap[i],heap[parent]
            i=parent 
        else:
            break

def extract_max():
    if not heap:
        return -1
    if len(heap)==1:
        return heap.pop()
    a=heap[0] 
    heap[0]=heap.pop()
    i=0
    while True:
        biggest=i 
        left = 2*i+1
        right = 2*i+2

        if left<len(heap) and heap[left]>heap[biggest]:
            biggest = left
        if right<len(heap) and heap[right]>heap[biggest]:
            biggest = right
        if biggest==i:
            break
        heap[i],heap[biggest]=heap[biggest],heap[i] 
        i=biggest
    return a


heap=[]
n=int(input())
a=list(map(int,input().split()))
for i in a:
    insert(i)
while len(heap)>1:
    y=extract_max()
    x=extract_max()
    if y!=x:
        insert(y-x)
if len(heap):
    print(heap[0])
else:
    print(0)

