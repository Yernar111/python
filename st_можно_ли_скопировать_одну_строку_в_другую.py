s=str(input())
t=str(input())
i=0
check = True
if len(s)%len(t)!=0:
    print("No")
    exit()
while i<len(s):
    j=0
    while j<len(t):
        if s[i]==t[j]:
            i+=1
        else:
            check = False
            break
        j+=1
    if not check:
        print("No")
        break
else:
    print("Yes")