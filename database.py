# -----------------------------------------------------------
# This file handles database related work.
#
# email -> mintu.giri1997@gmail.com
# -----------------------------------------------------------

### --- IMPORTS --- ###
import pymysql

# -----------------------------------------------------------
# This function creates the database.
# -----------------------------------------------------------
def create_db(database):
    db = pymysql.connect(user='root', password='', host='127.0.0.1')
    cursor = db.cursor()
    cursor.execute(f"DROP database IF EXISTS {database}")
    sql = "CREATE database fake_data"
    cursor.execute(sql)
    print("List of databases: ")
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())
    db.close()

# -----------------------------------------------------------
# This function creates the table into database.
# -----------------------------------------------------------
def create_table(database,table):
    db = pymysql.connect(user='root', password='', host='127.0.0.1',database=database)
    cursor = db.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table}")

    sql = f"""CREATE TABLE {table} (
    FIRST_NAME  CHAR(20) NOT NULL,
    LAST_NAME  CHAR(20),
    AGE INT,  
    SEX CHAR(1),
    INCOME FLOAT )"""

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"exp={e}")
        db.rollback()
    db.close()

# -----------------------------------------------------------
# This function insert the data into specific table 
# into database.
# -----------------------------------------------------------
def insert_data(database,table,values):
    db = pymysql.connect(user='root', password='', host='127.0.0.1',database=database)
    cursor = db.cursor()
    sql = f"""INSERT INTO {table}
    (FIRST_NAME,
    LAST_NAME,
    AGE,
    SEX,
    INCOME)
    VALUES {values}"""
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"exp={e}")
        db.rollback()
    db.close()

# -----------------------------------------------------------
# This function delete the data from specific table 
# from database.
# -----------------------------------------------------------
def delete_data(database, table, name):
    db = pymysql.connect(user='root', password='', host='127.0.0.1',database=database)
    cursor = db.cursor()
    sql = f"""DELETE FROM {table} WHERE FIRST_NAME = '{name}'"""
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"exp={e}")
        db.rollback()
    db.close()

# -----------------------------------------------------------
# This function update the data from specific table 
# into database.
# -----------------------------------------------------------
def update_data():
    # TODO
    pass

# -----------------------------------------------------------
# This function clear the data of specific table 
# from database.
# -----------------------------------------------------------
def clear_data():
    # TODO
    pass

# -----------------------------------------------------------
# This function read the data from specific table 
# from database.
# -----------------------------------------------------------
def read_data(database,table):
    data_list = []
    db = pymysql.connect(user='root', password='', host='127.0.0.1',database=database)
    cursor = db.cursor()
    sql = f"SELECT * FROM {table} WHERE 1"
    try:
        cursor.execute(sql)
        for data in cursor.fetchall():
            data_list.append(data)
    except Exception as e:
        print(f"exp={e}")
        db.rollback()
    db.close()
    return data_list