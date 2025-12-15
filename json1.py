import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": True,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x)) # json.dumps преобразует обьект python в строку json

# Файл в формате json можно создать и вручную сохраняя с расширением .json. Далее можно будет добавлять данные внутрь этого файла. Ниже показано как создать такой файл с помощью операции с файлами
with open("json_data", "w") as abcd: # Создание и последующее открытие файла с названием "json_data" в режиме "w" для записи 
    json.dump(x, abcd) # json.dump преобразует(записывает) обьект python в файл в формате json