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
sqlString = "SELECT * FROM Taxi_Trips"
crsr.execute(sqlString)

# this will fetch all the relevant records
# and print the number returned
rows = crsr.fetchall()
print(len(rows), " records have Fares > $10")


