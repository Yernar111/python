s=str(input())
i=0
a=[]
while i<len(s):
    m=0
    while i<len(s) and s[i]!=" ":
        m+=1
        i+=1
    i+=1
    a.append(m)
a.sort()
print(a[len(a)-1])