def check(n):
    if n==1:
        return "Yes"
    if n%2==1:
        return "No"
    return check(n//2)

n=int(input())
print(check(n))
    