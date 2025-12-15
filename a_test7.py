n=int(input())
a=list(map(int,input().split()))
t=0
print(chr(97+a[0]), end="")
for i in range(1,n):
    t=a[i]-a[i-1]
    k=(97*(2**i)+t)//(2**i)
    print(chr(k), end="")