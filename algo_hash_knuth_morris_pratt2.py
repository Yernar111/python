# Knuth-Morris-Pratt алгоритм.
# lps[i]=k первые k символов одинаковые с последними k символами s[0...k+1]=s[k...n] 
def compute_lps(pattern):
    lps = [0] * len(pattern)

    for i in range(1,len(pattern)):
        j=lps[i-1]

        while j>0 and pattern[i]!=pattern[j]:
            j=lps[j-1]
        if pattern[i]==pattern[j]:
            j+=1
        lps[i]=j

    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)

    i = j = 0
    result = []

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            result.append(i - j) 
            j = lps[j - 1] 

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result

text=input()
pattern=input()
print(kmp_search(text, pattern))
