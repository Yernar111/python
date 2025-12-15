# Knuth-Morris-Pratt алгоритм.
def compute_lps(pattern): # Функция LPS(longest prefix suffix). Эта функция находит самый длинный префикс строки i-тому элементу, который также является суффиксом строки 
    lps = [0] * len(pattern) # Массив LPS - i-тый элемент массива равен максимальной длине префикса k в pattern[0...k] который равен суффиксу pattern[n-k-1...n]. То есть, max(k) при котором pattern[0...k]=pattern[n-k...n]
    length = 0  # Длина, и вместе с этим индекс текущего совпадающего префикса суффикса
    i = 1 # Начинаем с индекса 1, так как по умолчанию lps[0]=0

    while i < len(pattern):
        if pattern[i] == pattern[length]: # Если символы совпали, то lps[i] равен текущей длине+1. Увеличиваем length и i, в таком случае интервал между ними сохраняется, то есть на следующей итерации мы сравниваем соседние элементы.
            length += 1
            lps[i] = length 
            i += 1
        else: # Если символы не совпали(i-тый элемент не является префиксом суффиксом)
            if length != 0: # Если длина текущего совпадающего префикса суффикса не равен 0, то 
                length = lps[length - 1] # Приравниваем индекс к длине предыдыдущего префикса суффикса
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)

    i = j = 0  # индексы для text и pattern
    result = []

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:  # Нашли полное совпадение
            result.append(i - j) 
            j = lps[j - 1] 

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1] # Передвигаем индекс j на позицию предыдущего префикса суффикса, так как индекс равный lps[j-1] является 
            else:
                i += 1

    return result


# Пример
# text = "ababcabcabababd"
# pattern = "ababd"
text=input()
pattern=input()
print(kmp_search(text, pattern))
