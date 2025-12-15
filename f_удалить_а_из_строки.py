def check(s):
    t=""
    for i in s:
        if i!="a":
            t+=i
    return t
        

s=str(input())
print(check(s))