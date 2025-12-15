# Topological sort через алгоритм Кана(с использованием BFS)
def topo_sort(n):
    q = []
    for i in range(1,n+1):
        if indeg[i] == 0: # Ищем вершину у которой indegree=0(источник), чтобы начать с нее исследование графа
            q.append(i)
    
    result = []
    while q:
        node = q.pop(0)
        result.append(node)

        for i in a[node]: # Обходим соседние вершины такие что: node->v
            indeg[i] -= 1 # Мысленно удаляем текущий источник, тем самым уменьшаем indegree у всех соседних с ней вершин на 1, и если вершина становится равной нулю то можно сказать что она стала новым источником. Если нет, то граф имеет цикл(сортировка невозможна)
            if indeg[i] == 0:
                q.append(i)

    if len(result) != n:
        return "Graph has cycle"

    return result  # Если длина массива с топологической сортировкой равна количеству элементов графа, значит сортировка успешно выполнилась для всех вершин.


n=int(input())
indeg=[0]*(n+1)
a=dict()
for i in range(1,n+1):
    b=list(map(int,input().split()))
    for j in b:
        indeg[j]+=1 # Считаем indegree каждой вершины
    a[i]=b


print(topo_sort(len(a)))