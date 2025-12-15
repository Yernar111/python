a=str(input())
for i in range(1,len(a)):
    if ord(a[i])>=ord(a[i-1]):
        continue
    print("No")
    break
else:
    print("Yes")