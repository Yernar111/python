# Этот метод сортировки работает за O(n log n). Так как мы делаем вставку n раз и извлечение n раз. O(n log n)+O(n log n) = O(n log n)
def insert(x):
    heap.append(x)
    i=len(heap)-1 
    parent = (i-1)//2
    while i>0 and heap[parent]>heap[i]:
        heap[parent],heap[i]=heap[i],heap[parent]
        i=parent 

def extract_min():
    if not heap:
        return None
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
a=list(map(int,input().split()))
for i in a:
    insert(i)

a=[]
while heap:
    a.append(extract_min())
print(a)
    
