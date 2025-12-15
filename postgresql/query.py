import psycopg2
from config import load_config
def get_vendors():
    """ Retrieve data from the vendors table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
                print("The number of parts: ", cur.rowcount)
                # При применении методов fetch, изначально позиция курсора находится в первой строке. Затем после выполнения метода fetch позиция курсора спускается вниз на 1 или больше строк(в зависимости от специфики fetch). И после того как курсор спустится на дно списка, она возвращает None
                # Но, при операциях insert/update/delete метод fetchone(или другие fetch) будут возвращать измененную строку(при этом запрос обязательно должен содержать returning "столбец1","столбец2",...)
                row = cur.fetchone() # Возвращает одну строку из результата запроса
                print(row)
                row = cur.fetchmany(size=2) # Возвращает список из n строк, позиция курсора спускается на n строк вниз.
                print(row)
                row = cur.fetchall() # Возвращает все оставшиеся строки начиная с текущей позиции курсора.
                print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
if __name__ == '__main__':
    get_vendors()