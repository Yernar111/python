import psycopg2
from config import load_config
def insert_vendor(vendor_name1, vendor_name2, vendor_name3):
    """ Insert a new vendor into the vendors table """
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;""" # %s используется для подстановки значении при выполнении метода execute()
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # При использовании обьекта курсора, позиция курсора изначально находится в первой строке, затем после каждого выполнения спускается на 1 или больше строк, в зависимости от команды
                # execute the INSERT statement
                cur.execute(sql, (vendor_name1,)) # Метод execute(sql, (c1,c2,...)) содержит в себе два параметра(второй необязательный). Первый параметр sql содержит sql команду, второй параметр содержит данные которые будут переданы в sql команду(порядок важен). 
                cur.execute(sql, (vendor_name2,))
                cur.execute(sql, (vendor_name3,))
                # get the generated id back
                conn.commit() # commit the changes to the database
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
def insert_many_vendors(vendor_list):
    """ Insert multiple vendors into the vendors table  """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING *"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, vendor_list) 
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

n=int(input())

if n == 1:
    insert_vendor("Example1","Example2","Example3")

if n == 2:
    insert_many_vendors([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])