import pyodbc
import os
cwd = os.getcwd()

pickup_area = input("Please enter a pickup community area between 1 and 77: ")

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ='+cwd+'\TaxiTripsDatabase.accdb;'
    )

cnxn=pyodbc.connect(conn_str)
crsr=cnxn.cursor()

sql_string = "SELECT COUNT(*) AS CountOfPickups " \
          + "FROM Taxi_Trips " \
          + "GROUP BY Taxi_Trips.Pickup_Community_Area " \
          + "HAVING Taxi_Trips.Pickup_Community_Area=" + pickup_area
crsr.execute(sql_string)
row = crsr.fetchone()

print(f"The number of pickups from area {pickup_area} was {row.CountOfPickups}")

