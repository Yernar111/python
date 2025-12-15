# Этот файл содержит в себе функцию load_config которая читает данные с database.ini
# Этот файл предназначен для загрузки параметров конфигурации из файла database.ini извлекая настройки из секции postgresql
from configparser import ConfigParser # Этот класс позволяет читать и записывать файлы конфигурации в формате ini, который часто используется для хранения настроек приложений.
def load_config(filename='postgresql/database.ini', section='postgresql'): # Имя файла конфигурации и секции которую нужно загрузить из файла.
    parser = ConfigParser() 
    parser.read(filename)
    # get section, default to postgresql
    config = {}
    if parser.has_section(section): # Проверка существует ли секция в файле
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1] # Задает значения key-value созданному словарю
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return config # Возвращает словарь
if __name__ == '__main__':
    config = load_config()
    print(config)