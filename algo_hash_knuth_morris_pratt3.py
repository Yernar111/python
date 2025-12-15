# Knuth-Morris-Pratt алгоритм.
# lps[i]=k первые k символов одинаковые с последними k символами s[0...k+1]=s[k...n] 
def prefix_f(s):
    lps = [0] * len(s)

    for i in range(1,len(s)):
        j=lps[i-1]

        while j>0 and s[i]!=s[j]:
            j=lps[j-1]
        if s[i]==s[j]:
            j+=1
        lps[i]=j

    return lps


def kmp(text, pattern):
    m=len(pattern)
    s=pattern+"#"+text
    n=len(s)
    lps = prefix_f(s)
    for i in range(m+1,n):
        if lps[i]==m:
            print(i-2*m, end=" ")

text=input()
pattern=input()
kmp(text, pattern)
