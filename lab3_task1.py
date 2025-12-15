n=int(input())
a=list(map(int, input().split()))
t={}
for i in a:
    t[i]=False
b=list(map(int, input().split()))
m=b[0]; k=b[1]
b={}; e={}
for i in range(m):
    c=list(map(int, input().split()))
    for j in range(k):
        b[c[j]]=i; e[c[j]]=j; t[c[j]]=True
    
for i in range(n):
    if t[a[i]]:
        print(b[a[i]], e[a[i]])
    else:
        print(-1)

    
