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
sqlString = "SELECT * " \
          + "FROM (Taxi_Trips "\
          + "INNER JOIN Communities " \
          + "ON Taxi_Trips.Pickup_Community_Area = Communities.Community_Num) "
crsr.execute(sqlString)

# print number of records found:
rows = crsr.fetchall()
print(len(rows), " records were found")

