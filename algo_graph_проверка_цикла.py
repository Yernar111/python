# Проверка есть ли цикл в графе с помощью DFS
def dfs(v):
    visited[v]=1
    for i in a[v]:
        if visited[i]==0:
            dfs(i)
        elif visited[i]==1: 
            exit()
    visited[v]=2
    


n=int(input())
a=dict()
for i in range(1,n+1):
    b=list(map(int,input().split()))
    a[i]=b

visited=[0]*(n+1)
dfs(1)



