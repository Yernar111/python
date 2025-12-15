n,k,m=1,-1,1
while n!=0:
    n=int(input())
    if n>k:
        m=1
        k=n
    elif n==k:
        m+=1
print(m)
