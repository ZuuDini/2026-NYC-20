import mysql.connector as mydbconnection
from mysql.connector import Error
def insert_varibles_into_table(id, name, price, purchase_date):
    try:
        conn = mydbconnection.connect(database='usersdb', user='root',password='password', port ='3306', use_pure = True)
        cursor = conn.cursor()
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)VALUES (%s, %s, %s, %s) """                  

        record = (id, name, price, purchase_date)
        cursor.execute(mySql_insert_query, record)
        conn.commit()
        print("Record inserted successfully into Laptop table")

    except Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")


insert_varibles_into_table(2, 'Area 51M', 6999, '2019-04-14')
insert_varibles_into_table(3, 'MacBook Pro', 2499, '2019-06-20')
