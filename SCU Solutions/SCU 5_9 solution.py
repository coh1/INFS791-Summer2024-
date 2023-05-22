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
sqlString = "SELECT Sum(Tips), Sum(Trip_Miles), Payment_Type "\
            + "FROM Taxi_Trips "\
            + "GROUP BY Payment_Type "\
            + "HAVING Sum(Trip_Miles) > 25"
crsr.execute(sqlString)

# print what our query returned:
rows = crsr.fetchall()
print(rows)

