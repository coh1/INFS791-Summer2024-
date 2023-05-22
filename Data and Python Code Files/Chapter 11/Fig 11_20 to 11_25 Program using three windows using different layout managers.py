import tkinter as tk

def trip_data_button():
        fare_var_float = float(fare_var.get())
        tip_var_float = float(tip_var.get())        
        create_result_window(fare_var_float, tip_var_float)

def create_trip_data_window():
    windowname="Taxi trip data"
    window2 = tk.Toplevel(main_window)
    window2.geometry("600x500")
    for col_no in range(0, 2):
        window2.columnconfigure(col_no, minsize=80)
    for row_no in range(0, 2):
        window2.rowconfigure(row_no, minsize=80)
    window2.title(windowname)
    infolabel=tk.Label(window2, \
        text="Please enter Taxi trip information below"). \
        grid(column=1, row=0)

    global fare_var
    fare_var = tk.StringVar()

    global tip_var
    tip_var = tk.StringVar()

    fare_label = tk.Label(window2, \
      text="Fare:").grid(column=0, row=1)
    fare_entry = tk.Entry(window2, \
      textvariable = fare_var). \
      grid(column=1, row=1)
    tip_label = tk.Label(window2, \
      text="Tip:").grid(column=2, row=1)
    tip_entry = tk.Entry(window2, \
      textvariable = tip_var). \
      grid(column=3, row=1)
    button2 = tk.Button(window2, \
      text="Calculate Total Fare", \
      command=trip_data_button, \
      width=20, height=2). \
      grid(column=2, row = 2)
    cancel = tk.Button(window2, \
       text="Cancel", command=window2.destroy, \
       width=20, height=2). \
       grid(column=2, row = 4)


def create_result_window(fare_var, tip_var):
    windowname="Calculated total taxi fare"
    window3 = tk.Toplevel(main_window)
    window3.geometry("400x300")
    window3.title(windowname)
    total_fare = fare_var+tip_var
    
    window3.infolabel=tk.Label(window3, \
        text="The Calculated total fare is: " + \
             "\nFare: " + str(fare_var) + 
             "\nTip:  " + str(tip_var) +
             "\nTotal Fare: " + str(total_fare), \
             justify="right").place(x=50, y=50)
    window3.cancel = tk.Button(window3, \
       text="Cancel", command=window3.destroy)
    window3.cancel.place(x=100, y = 150)

main_window = tk.Tk()
main_window.geometry("600x500")
main_window.title("Main window")

welcome_label = tk.Label(main_window, \
   text="Welcome to the Taxi Trip Fare calculator application",\
   font=("Helvetica",16)).pack()

button1 = tk.Button(main_window, \
   text="Enter Taxi trip data", command=create_trip_data_window,\
   width=20, height=2).pack()

cancel = tk.Button(main_window, \
   text="Cancel", command=main_window.destroy, \
   width=20, height=2).pack()

main_window.mainloop()

