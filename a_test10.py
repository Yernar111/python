t=int(input())
for i in range(t):
    check=False
    s=input()
    t=input()
    a=[ord(y) for y in s]
    b=[ord(y) for y in t]
    # k=s

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
    # for k in range(len(b)):
    #     if b[k]<=a[0]:
    #         w.append(b[k])
    r=0
    if b[r]<a[0]:
        while r<len(b) and b[r]<a[0]:
            w.append(b[r])
            r+=1
    w.extend(a)
    # r+=len(a)
    # for j in w:
    #     print(chr(j),end="")
    # print()
    w.extend(b[r:])
    for j in w:
        print(chr(j),end="")
    print()




    # while s:
    #     if s[0] in t:
    #         s=s.replace(s[j],'')
    #         t=t.replace(s[j],'')
    #     else:
    #         print("Impossible")
    #         check=True
    #         break
    
    # if check:
    #     continue
    
    # c=[ord(y) for y in t]
    # c.sort()
    # d=""
    # for i in c:
    #     d+=chr(i)
    
    # w=""
    # h=0
    # while ord(d[h])<=ord(k[0]) and h<len(d):
    #     w+=d[h]
    #     h+=1
    # w+=k
    # w+=d[h:]
    # print(w)