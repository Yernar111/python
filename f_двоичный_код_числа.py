def check(n):
    s=t=""
    while n!=0:
        s+=str(n%2)
        n//=2
    for i in range(len(s)-1,-1,-1):
        t+=s[i]
    return t
    
        
n=int(input())
print(check(n))