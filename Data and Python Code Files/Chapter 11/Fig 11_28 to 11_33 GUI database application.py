from tkinter import *
import pyodbc
from tkinter import messagebox
import os

def displaybutton():
   listindex = mw_listbox.curselection()
   listitem = mw_listbox.get(listindex)
   choice = var1.get()
   if choice == 1:
      aggr_func = "Count"
   elif choice == 2:
      aggr_func = "Sum"
   else:
      aggr_func = "Avg"

   sql_string = "SELECT Communities.Community_Name," + aggr_func + "(Taxi_Trips.Fare) " \
             + "AS AggrResult FROM Communities INNER JOIN Taxi_Trips ON " \
             + "(Communities.Community_Num = Taxi_Trips.Pickup_Community_Area) " \
             + "GROUP BY Communities.Community_Name " \
             + "HAVING Communities.Community_Name='" + listitem + "'"
   crsr.execute(sql_string)
   try:  
      row = crsr.fetchone()
      if choice == 1:
        result_message = "There were " +str(row.AggrResult) \
                      + " fares picked up from " + listitem
      elif choice == 2:
        result_message = "The total dollar amount of fares picked up \nfrom " \
                      + listitem + " was $" + str(round(row.AggrResult,2))
      else:
        result_message = "The average of the fares picked up \nfrom " \
                      + listitem + " was $" + str(round(row.AggrResult,2))
   except AttributeError:
      result_message = "No fares were picked up from this area"

   messagebox.showinfo("Information Requested", result_message)
   
main_window = Tk()
main_window.title('Main window')
main_window.geometry("800x600+300+100")

for col_no in range(0,2):
   main_window.columnconfigure(col_no, minsize=300)
for row_no in range(0,9):   
   main_window.rowconfigure(row_no, minsize=40)
mw_title = Label(main_window,text = "Taxi Fare Information Application",\
           font = ("Helvetica", 16), justify=CENTER).\
           grid(row = 0, columnspan = 3, rowspan = 2)
mw_listboxlabel = Label(main_window,\
                  text = "Please select pickup \ncommunity area \nfrom list below",\
                  font = ("Helvetica", 14)).\
                  grid(row = 2, rowspan = 3, column = 0)
listvar=StringVar()
mw_listbox = Listbox(main_window,font=("Helvetica",14))

cwd = os.getcwd()
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ='+cwd+'\TaxiTripsDatabase.accdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()
sql_string = "SELECT Communities.Community_Name " \
          + "FROM Communities " \
          + "ORDER BY Communities.Community_Name" 
crsr.execute(sql_string)
rows = crsr.fetchall()
for row in rows:
    mw_listbox.insert(END, row.Community_Name)

mw_listbox.grid(row=5, column=0,rowspan=5, columnspan=1, sticky=W, padx=40)
mw_listbox.yview_scroll(45, 'units')
mw_listbox.select_set(47)

mw_framelabel = Label(main_window,\
                text="What information \nwould you like to see \nfor that community?",\
                font=("Helvetica", 14)).grid(row=2,rowspan=3,column=1)
mw_frame = Frame(main_window).grid(row=5, column=1,rowspan=4)

var1 = IntVar()
var1.set(2)
mw_rbchoice1 = Radiobutton(mw_frame,text="Number of fares", value=1, variable=var1,\
               font=("Helvetica", 14)).grid(row=6, column=1, sticky=W)
mw_rbchoice2 = Radiobutton(mw_frame,text="Total of all fares", value=2, variable=var1,\
               font=("Helvetica", 14)).grid(row=7, column=1, sticky=W)
mw_rbchoice3 = Radiobutton(mw_frame,text="Average fare", value=3, variable=var1,\
               font=("Helvetica", 14)).grid(row=8, column=1, sticky=W)
   
mw_displaybutton = Button(main_window,\
                  text="Display Result",command=displaybutton,width=20,height=2)\
                  .grid(row=8,column=2)
mw_endbutton = Button(main_window,text="End Session",\
                  command=main_window.destroy,width=20,height=2)\
                  .grid(row=9,column=2)

main_window.mainloop()

