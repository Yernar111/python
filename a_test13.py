# map(int,input().split())
# list(map(int,input().split()))
# int(input())
y=int(input())
for x in range(y):
    n=int(input())
    a=list(map(int,input().split()))
    k=a[0]%2
    for i in range(2,n,2):
        if a[i]%2!=k:
            print("NO")
            break
    else:
        print("YES")

    

    
