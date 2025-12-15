s=str(input())
k=0
m=len(s)-1
for i in s:
    k+=int(i)*2**m
    m-=1
print(k)

