import pyodbc
for x in pyodbc.drivers(): 
    if x.startswith('Microsoft Access Driver'):
       print(x)

