n,k,m=1,0,0
while n!=0:
    n=int(input())
    if n>k:
        m=k
        k=n
    elif n>m and n<k:
        m=n
print(m)