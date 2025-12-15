n,m=map(int,input().split())
b={}
for i in range(n):
    a=list(map(int, input().split()))
    b[a]=int(sum(a))

t=dict(sorted(b.items(), key=lambda r: r[1], reverse=True))

for i,y in t.items():
    for j in i:
        print(j, end=" ")
    print()



