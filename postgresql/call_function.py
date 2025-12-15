import psycopg2
from config import load_config
def get_parts(vendor_id):
    """ Get parts provided by a vendor specified by the vendor_id """
    parts = []
    # read database configuration
    params = load_config()
    try:
        # connect to the PostgreSQL database
        with  psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # create a cursor object for execution
                cur = conn.cursor()
                cur.callproc('get_parts_by_vendor', (vendor_id,)) # callproc('funcion', (parameters)) метод который используется для вызова функции который находится в текущей базе данных. Первый аргумент хранит в себе название функции, второй параметры функции
                # process the result set
                row = cur.fetchone() # Функция возвращает значение в курсор, поэтому необходимо выполнить эту операцию. Так как функция возвращает значение, то ее лучше использовать с SELECT
                while row is not None:
                    parts.append(row)
                    row = cur.fetchone()
                #cur.execute('call function(%s,%s,...)', (parameters)) используется для вызова процедуры, который в отличии от функции не возвращает значение.
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return parts
if __name__ == '__main__':
    parts = get_parts(1)
    print(parts)