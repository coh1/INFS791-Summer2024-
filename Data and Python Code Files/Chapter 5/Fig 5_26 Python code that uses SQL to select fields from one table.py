import pyodbc
import os
cwd = os.getcwd()

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ='+cwd+'\TaxiTripsDatabase.accdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()
crsr.execute("SELECT Community_Num, Community_Name FROM Communities")
rows = crsr.fetchall()
for row in rows:
    print(row.Community_Num, row.Community_Name)

