def check(s, i, k):
    if i==len(s):
        return k
    return check(s, i+1, k+int(s[i]))

n=str(input())
print(check(n,i=0,k=0))
    