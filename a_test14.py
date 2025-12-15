t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
        
    i=k=0
    j=1
    while i+j<n:
        if a[i]>a[i+j]:
            k+=1
            j+=1
        else:
            i+=j
            j=1
    print(k)


