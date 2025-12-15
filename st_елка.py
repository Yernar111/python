n=int(input())
k=1
for i in range(1,n+1):
    s=" "*(n-i)
    t="*"*k
    k+=2
    print(s,t)