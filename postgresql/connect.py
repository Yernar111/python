# Этот файл предназначен для подключения к серверу PostgreSQL
import psycopg2
from config import load_config
def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn: # Передача параметров подключения в виде ключевых аргументов, ** распаковывает словарь config передавая его элементы как аргументы функции
            print('Connected to the PostgreSQL server.')
            return conn # Возвращает обьект соединения
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
if __name__ == '__main__':
    config = load_config()
    connect(config)