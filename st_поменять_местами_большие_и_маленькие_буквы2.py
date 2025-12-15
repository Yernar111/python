s=input()
t=""
for i in range(len(s)):
    if s[i].isupper():
        t+=s[i].lower()
    elif s[i].islower():
        t+=s[i].upper()
print(t)
