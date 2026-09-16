import mysql.connector as dbconnect

# FIX 1: use_pure=True uses the pure-Python driver. The default C extension
# crashes on Python 3.14 (Windows access violation, exit code 5, no error shown).
myconnection = dbconnect.connect(host='mysql-rfam-public.ebi.ac.uk', database='Rfam', user='rfamro', password='',port=4497, use_pure=True)

# Get a cursor
cursor = myconnection.cursor()
# FIX 2: The string must open and close with the same quote type ("...").
# Leave %s unquoted - the driver adds the quotes around the value itself.
SQLQuery = "SELECT * FROM author WHERE initials=%s"
initials = input("What are the initials ")
print = initials
# Execute a query
# FIX 3: Parameters must be a tuple. ('Z') is just a string; the trailing
# comma in ('Z',) makes it a one-item tuple. 'Z' fills in the %s above.
cursor.execute(SQLQuery, (initials,))

# get all records
records = cursor.fetchall()   
print("Total number of rows in table: ", cursor.rowcount)    
print("\nPrinting each row")
for row in records:
    print("order number = ", row[0],  )
    print("item counts = ", row[1])
    print("total  = ", row[2], "\n" )

# Close connection
cursor.close()
myconnection.close()
