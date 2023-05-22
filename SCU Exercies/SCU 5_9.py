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
sqlString = "SELECT SUM(Tips), SUM(Trip_Miles), Payment_Type "\
            + "FROM Taxi_Trips"
crsr.execute(sqlString)

# print what our query returned:
rows = crsr.fetchall()
print(rows)

