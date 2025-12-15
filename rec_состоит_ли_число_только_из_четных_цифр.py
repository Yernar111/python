def check(n):
    if n==0:
        return True
    if n%10%2==1:
        return False
    return check(n//10)

n=int(input())
print("Yes") if check(n) else print("No")