import pyodbc
import os
cwd = os.getcwd()

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ='+cwd+'\TaxiTripsDatabase.accdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()
sql_string = "SELECT Count(*) AS CountOfFare " \
          + "FROM Taxi_Trips"
crsr.execute(sql_string)
rows = crsr.fetchall()
for row in rows:
    print(row.CountOfFare)

