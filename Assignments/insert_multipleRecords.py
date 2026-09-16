
import mysql.connector as mydbconnection
from mysql.connector import Error

try:
    conn = mydbconnection.connect(database='usersdb', user='root',password='password', port ='3306', use_pure=True)

    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES (%s, %s, %s, %s) """

    records_to_insert = [(4, 'HP Pavilion Power', 1999, '2019-01-11'),
                         (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
                         (6, 'Microsoft Surface', 2330, '2019-07-23')]
    cursor = conn.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    conn.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")

except Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
