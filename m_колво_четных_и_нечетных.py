n = int(input())
a=[]
for i in range(n):
    t=int(input())
    a.append(t)

k,m=0,0
for i in range(len(a)):
    if a[i]%2==0:
        m+=1
    else:
        k+=1
print(f"Even: {m}",f"Odd: {k}")