# Счастливый билет - билет с таким номером, что сумма цифр делится на последнюю цифру
s=str(input())
k=0
for i in s:
    k+=int(i)
if k%int(s[len(s)-1])==0:
    print("Yes")
else:
    print("No")
