def check(n):
    k=1
    for i in range(1,n+1):
        s=" "*(n-i)
        t="*"*k
        k+=2
        print(s,t)

    
        
n=int(input())
check(n)