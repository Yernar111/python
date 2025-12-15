a=int(input())
s=""
while a!=0:
    s+=str(a%2)
    a//=2
for i in range(len(s)-1,-1,-1):
    print(s[i], end="")