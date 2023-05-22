import pyodbc
import os
cwd = os.getcwd()

conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ='+cwd+'\\TaxiTripsDatabase.accdb;'
        )

# sets up the database connection:
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

# finish the query in the quotes:
sqlString = "SELECT Community_Name from Communities"
crsr.execute(sqlString)

# the following fetches all the records pulled,
# and prints out the values returned:
rows = crsr.fetchall()
for row in rows:
    print(row.Community_Name)

