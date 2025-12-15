# DFS через стэк для графа представленного в виде матрицы смежности
def dfs(k,n): 
    res=[]
    stack=[k]
    while stack:
        m=stack.pop()
        if not visited[m]:
            visited[m]=True
            res.append(m+1)
            for i in range(n):
                if a[m][i] and (not visited[i]):
                    stack.append(i)
    return res



n=int(input())
a=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    b=list(map(int,input(f"Вершины соседние с {i+1}: ").split()))
    for j in b:
        a[i][j-1]=1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()

visited=[False]*n
k=int(input())
print(dfs(k-1,n))


