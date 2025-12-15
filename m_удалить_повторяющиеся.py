n=int(input())
a=[]
b=[]
for i in range(n):
    t=input()
    a.append(t)
for i in a:
    if not i in b:
        b.append(i)
print(b)


