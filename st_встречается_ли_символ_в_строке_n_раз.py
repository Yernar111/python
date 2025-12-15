s=str(input()) # String
t=str(input()) # Char
n=int(input()) # The number of chars
k=0
for i in s:
    if i==t:
        k+=1
if k==n:
    print("Yes")
else:
    print("No")

