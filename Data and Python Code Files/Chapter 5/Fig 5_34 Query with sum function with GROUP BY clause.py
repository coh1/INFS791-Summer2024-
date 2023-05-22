import pyodbc
import os
cwd = os.getcwd()

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ='+cwd+'\TaxiTripsDatabase.accdb;'
    )

cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

sql_string = "SELECT Communities.Community_Name, " \
          + "   SUM(Taxi_Trips.Fare) AS Sum_of_Fares " \
          + "FROM Communities " \
          + "INNER JOIN Taxi_Trips " \
          + "ON Communities.Community_Num = " \
          + "   Taxi_Trips.Pickup_Community_Area " \
          + "GROUP BY Communities.Community_Name"

crsr.execute(sql_string)
rows = crsr.fetchall()
for row in rows:
    print(row.Community_Name, round(row.Sum_of_Fares,2))

