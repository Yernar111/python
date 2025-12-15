# Если символ встречается в строке 1 раз, вывести индекс, если больше одного раза, вывести индекс первого и последнего
s=str(input())
t=str(input())
m = False
for i in range(len(s)):
    if s[i]==t:
        k=i
        break
for i in range(len(s)-1,-1,-1):
    if s[i]==t:
        if i==k:
            break
        m = True
        q=i
        break
print(k,q) if m else print(k)