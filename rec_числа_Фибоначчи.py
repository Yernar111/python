def check(n):
    if n<=2:
        return 1
    return check(n-1)+check(n-2)

n=int(input())
print(check(n))
    