
n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i**0.5==int(i**0.5) and i!=1:
        print("YES")
    else:
        print("NO")