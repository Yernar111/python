import json

x = '{"a":1, "B":"True", "abcd":"efgh"}' # Отличие строки json от словаря(dictionary) в том что строка должна содержатся в кавычках
y=json.loads(x) # Преобразование строки json в обьект python
print(y)

with open("json_data", "r") as json_f: # Открытие ранее созданного файла с названием "json_data" в режиме "r" для чтения
    u=json.load(json_f) # json.load преобразует файл в формате json в обьект python
    print(u)
