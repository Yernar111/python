def check(s):
    k=len(s)-1
    q=0
    for i in range(len(s)):
        q+=int(s[i])*2**k
        k-=1
    return q

n=str(input())
print(check(n))