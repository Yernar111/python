def check(s):
    k=0
    t=1
    for i in range(len(s)):
        k+=ord(s[i])*t
        t*=29
    return k

t=1
while t:
    t=int(input())
    a=list()
    for i in range(t):
        s=input()
        a.append(s)
    s=input()
    for i in range(t):
        m=len(a[i])
        k=check(s[:m])
        
print(a)


