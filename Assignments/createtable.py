import mysql.connector as mydbconnection
from mysql.connector import Error
try:
    # use_pure=True: the default C driver crashes on Python 3.14, so use the pure-Python driver
    conn = mydbconnection.connect(database='usersdb', user='root', password='password', port=3306, use_pure=True)
    cursor=conn.cursor()
    myquery2 = "CREATE TABLE `laptop` (`Id` int(11) NOT NULL,\
    `Name` varchar(250) NOT NULL,\
    `Price` float NOT NULL,\
    `Purchase_date` date NOT NULL)" 
    cursor.execute(myquery2)
    print("Table is created")
except Error as e:
    print("Failed tocreate table {}".format(e))
finally:
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")
