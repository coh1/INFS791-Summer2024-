import pyodbc
import os
cwd = os.getcwd()

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ='+cwd+'\TaxiTripsDatabase.accdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

# Create SQL query string with count function also used as criteria
sql_string = "SELECT Communities.Community_Name, " \
          + "   COUNT(Taxi_Trips.Fare) AS CountOfFare " \
          + "FROM Communities " \
          + "INNER JOIN Taxi_Trips " \
          + "ON Communities.Community_Num = " \
          + "   Taxi_Trips.Pickup_Community_Area " \
          + "GROUP BY Communities.Community_Name " \
          + "HAVING COUNT(Taxi_Trips.Fare)>5"
crsr.execute(sql_string)
rows = crsr.fetchall()
for row in rows:
    print(row.Community_Name, row.CountOfFare)

