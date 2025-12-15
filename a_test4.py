def bfs(v,m):
    if a[v][m]:
        return 1
    visited=[False]*(len(a))
    queue=[v]
    visited[v]=True
    distance=[-1]*(len(a))
    distance[v]=0
    while queue:
        node=queue.pop(0)
        for i in range(n):
            if a[node][i] and (not visited[i]):
                visited[i]=True
                distance[i]=distance[node]+1
                queue.append(i)
                if visited[m]:
                    return distance[m]
    return -1


n=int(input())
a=[] 
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)

k,m=map(int, input().split())
t=bfs(k-1,m-1)
if t!=-1:
    print(t)
else:
    print(-1)