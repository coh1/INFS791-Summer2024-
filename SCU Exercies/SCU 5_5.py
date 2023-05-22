import pyodbc
import os
cwd = os.getcwd()

conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ='+cwd+'\TaxiTripsDatabase.accdb;'
        )

# sets up the database connection:
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

# finish the query in the quotes:
sqlString = "SELECT "
crsr.execute(sqlString)

# this will fetch all the records pulled,
# and print out the values returned:
rows = crsr.fetchall()
for row in rows:
    print(row.Community_Name)

