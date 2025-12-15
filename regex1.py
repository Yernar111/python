import re
a="Abcd efgh"
b="efg pqr"
c="afg tra yra"
d="abcd efgh pqr"
print(re.search("efgh", a)) # Первое вхождение паттерна в строку
print(re.match("efg ", b)) # Проверка соответствует ли начало строки паттерну
print(re.findall("ra", c)) # Список всех паттернов в строке
print(re.split(" ", d)) # Список строк разделенных паттерном

print()
e="Lorem ipsum is simply its dummy text of the printing and type#setting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book"
f="ebcd tyud rrrd dtr rt"
print(re.search("^Lorem", e)) # Начинается ли строка паттерном
print(re.search("ok$", e)) # Заканчивается ли строка паттерном
print(re.findall(".e", e)) # . означает количество символов идущих до или после паттерна, в зависимости от количества и расположения точки
print(re.findall("m|r", e)) # | означает вхождение либо первого либо второго паттерна
print(re.findall("r[eiyu]", e)) # Символы которые начинаются или заканчиваются определенным паттерном, а между концом и началом одна из символов в квадратных скобках 
print(re.findall(r"\bL.", e)) # \b слова начинающиеся паттерном
print(re.findall("i.+m", e)) # Строка начинающаяся символом i и состоящее из максимально длинной последовательности(+) 1 или более символов таких что, в конце этой последовательности будем символ m. То есть выражение . повторяется 1 или больше раз(максимально возомжно)
print(re.findall("i.?s", e)) # Строка начинающаяся символом i и состоящее из минимально длинной последовательности(?) 0 или 1 символов заканчивающихся на s. То есть выражение . повторяется 0 или 1 раз(либо два символа идут подряд, либо между ними лишь 1 символ)
print(re.findall(r"\bi.+?[.| ]", e)) # Все возможные минимальные и не пересекающиеся строки начинающиеся i заканчивающиеся s
print(re.findall("\S+m", e)) # Строки в которых нету whitespace(то есть таб, пробел и т.д.)


