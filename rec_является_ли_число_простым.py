def check(k,i):
    if i>int(k**0.5+1):
        return "Yes"
    if k%i==0:
        return "No"
    return check(k,i+1)


k=int(input())
print(check(k,i=2))
    