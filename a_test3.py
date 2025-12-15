a=input()
t=0

for i in range(len(a)):
    t+=(ord(a[i])-47)*(11**i) % (10**9+7)
print(t)
