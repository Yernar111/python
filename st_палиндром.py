s=str(input())
check = False
for i in range(len(s)//2):
    if (s[i]!=s[len(s)-1-i]):
        print("No")
        break
else:
    print("Yes")