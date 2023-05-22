from tkinter import *

main_window = Tk()
main_window.title('Main window')
main_window.geometry("800x600+300+100")

for col_no in range(0, 2):
   main_window.columnconfigure(col_no, minsize=300)
for row_no in range(0, 9):   
   main_window.rowconfigure(row_no, minsize=60)
mw_title = Label(main_window,text="Title Label to Indicate Window Purpose",\
            font=("Helvetica", 16),justify=CENTER).grid(row=0, columnspan=3)
mw_directions = Label(main_window,\
                text="Label with directions to complete window entries",\
                font=("Helvetica", 14), fg="red").grid(row=1, columnspan=2, sticky=W)
mw_namelabel = Label(main_window,text="Label for User Name:",\
                font=("Helvetica", 14)).grid(row=2, column=0, sticky=E)
mw_nameentry = Entry(main_window).grid(row=2, column=1, sticky=W)

mw_listboxlabel = Label(main_window,\
                  text="Label asking user\n to make selection\n from listbox",\
                  font=("Helvetica", 14)).grid(row=3, rowspan=3, column=0)
mw_listbox = Listbox(main_window).grid(row=6, column=0, rowspan=4)

mw_framelabel = Label(main_window,\
                text="Label asking user\n to make selection\n from options below",\
                font=("Helvetica", 14)).grid(row=3, rowspan=3, column=1)
mw_frame = Frame(main_window, bg="White").grid(row=6, column=1, rowspan=4)

var1 = IntVar()

mw_rbchoice1 = Radiobutton(mw_frame,text="Choice 1", value=1, variable=var1,\
               font=("Helvetica", 14)).grid(row=6, column=1)
mw_rbchoice2 = Radiobutton(mw_frame,text="Choice 2", value=2, variable=var1,\
               font=("Helvetica", 14)).grid(row=7, column=1)
mw_rbchoice3 = Radiobutton(mw_frame,text="Choice 3", value=3, variable=var1,\
               font=("Helvetica", 14)).grid(row=8, column=1)

mw_cancelbutton = Button(main_window,text="Cancel", width=10, height=2)\
                        .grid(row=8, column=2)
mw_submitbutton = Button(main_window,text="Submit", width=10, height=2)\
                        .grid(row=9, column=2)

main_window.mainloop()

