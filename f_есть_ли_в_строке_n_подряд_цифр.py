# явл€етс€ ли строка таковым, что в ней содержитс€ n или больше подр€д идущих цифр
def check(s,n):
    k=0
    i=0
    while i<len(s):
        k=0
        while i<len(s) and ord(s[i])>=ord("0") and ord(s[i])<=ord("9"):
            k+=1
            i+=1
        if k>=n:
            return "Yes"
        i+=1
    return "No"
        

s=str(input())
n=int(input())
print(check(s,n))