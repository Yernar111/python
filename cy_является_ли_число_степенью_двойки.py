n=int(input())
k=0
while n!=1:
    k=n%2
    n//=2
    if k:
        print("No")
        break
else:
    print("Yes")