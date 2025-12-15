def check(a,b):
    c=[]
    for i in range(len(a)):
        c.append(a[i]-b[i])
    return c

a=[]
b=[]
n=int(input())
for i in range(n):
    a.append(int(input()))
for i in range(n):
    b.append(int(input()))
print(check(a,b))