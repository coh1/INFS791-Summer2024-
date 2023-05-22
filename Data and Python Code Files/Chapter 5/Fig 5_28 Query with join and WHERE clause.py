import pyodbc
import os
cwd = os.getcwd()

# Specify connection information
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ='+cwd+'\TaxiTripsDatabase.accdb;'
    )

cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

# SQL string that joins tables
sql_string = "SELECT Communities.Community_Name, Taxi_Trips.Fare " \
         + "FROM Communities INNER JOIN Taxi_Trips ON " \
         + "Communities.Community_Num = Taxi_Trips.Pickup_Community_Area " \
         + "WHERE Communities.Community_Name='Lake View'"

crsr.execute(sql_string)
rows = crsr.fetchall()
for row in rows:
    print(row.Community_Name, row.Fare)

