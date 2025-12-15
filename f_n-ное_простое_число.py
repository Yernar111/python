def check(k):
    for i in range(2,int(k**0.5)+1):
        if k%i==0:
            return False
    return True

n=int(input())
i=0
k=1
while i<n:
    k+=1
    if(check(k)):
        i+=1
print(k)



