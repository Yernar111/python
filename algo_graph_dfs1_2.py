# DFS через рекурсию для графа представленного в виде матрицы смежности
def dfs(k,n): 
    visited[k]=True
    print(k+1, end=" ")
    for i in range(n):
        if (not visited[i]) and a[k][i]:
            dfs(i,n)



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
dfs(k-1,n)


