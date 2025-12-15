s=str(input())
a=[0]*int(1e3)
for i in range(len(s)):
    a[int(s[i])]+=1
for i in range(0,len(s)-1):
    if a[i]==a[i+1] or a[i]==0 or a[i+1]==0:
        continue
    print("No")
    break
else:
    print("Yes")
    