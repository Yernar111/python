# map(int,input().split())
# list(map(int,input().split()))
# int(input())
p=int(input())
for q in range(p):
    n=int(input())
    s=input()
    k=n-2
    b=[]; i=1; j=n
    while k>=0:
        if s[k]=="<":
            b.append(i)
            i+=1
        else:
            b.append(j)
            j-=1
        k-=1
    print(i, end=" ")
    for i in range(n-2,-1,-1):
        print(b[i], end=" ")
    print()

    
