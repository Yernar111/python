t=int(input())
for i in range(t):
    check=False
    s=input()
    t=input()
    a=[ord(y) for y in s]
    b=[ord(y) for y in t]

    for j in range(len(s)):
        if a[j] in b:
            b.remove(a[j])
        else:
            print("Impossible")
            check=True
            break
    if check:
        continue

    b.sort()
    w=[]
    r=l=0
    while r<len(b) and l<len(a):
        if b[r]<a[l]:
            w.append(b[r])
            r+=1
        else:
            w.append(a[l])
            l+=1

    if r<len(b):
        w.extend(b[r:])
    if l<len(a):
        w.extend(a[l:])

    x=""
    for j in w:
        x+=chr(j)
    print(x)