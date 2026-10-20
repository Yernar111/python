a=str(input())
s=0
for i in range (0,len(a)//2):
    if a[i]==a[len(a)-1-i]:
        s+=1
    else:
        break
if s==len(a)//2:
    print("palindrome")
else:
    print("not palindrome")

i=0
j=len(a)-1
while i<j:
    if a[i]!=a[j]:
        print("not palindrome")
        break
    i+=1; j-=1
else:
    print("palindrome")