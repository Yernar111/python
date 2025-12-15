"""s = "python"
# ''.join(sorted(s))
b=sorted(s)
t=""
print(t.join(b))"""
a=list(map(int,input().split()))
b=lambda n : n+10
print(b(3))


s = "programming"
b=sorted(s)
vowels = "aeiou"

sorted_s = ''.join(sorted(b,key=lambda ch: (ch not in vowels, ch)))

print(sorted_s)"""

a={}
for i in range(5):
    a[i+1]=i
for x,y in a.items():
    print(x,y)"""
