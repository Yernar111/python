n = int(input())
l = int(input())
r = int(input())
a=[]
for i in range(n):
    t=int(input())
    a.append(t)

for i in range(n):
    if i==l:
        for j in range(r,l-1,-1):
            print(a[j], end=" ")
    if i<=r and i>=l:
        continue
    print(a[i],end=" ")
