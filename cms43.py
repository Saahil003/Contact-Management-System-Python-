
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import pymysql


def connection():
    conn = pymysql.connect(host='localhost',user='root', password='',db='students_db')
    return conn



def refreshTable():
    for data in A.get_children():
        A.delete(data)

    for array in read():
        A.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    A.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    A.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

x = Tk()
x.title("CONTACT MANAGEMENT SYSTEM")
x.geometry("1024x768")
A = ttk.Treeview(x)



ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()



def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def add():
    fname = str(fnameEntry.get())
    lname = str(lnameEntry.get())
    age = str(ageEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())

    if (fname == "" or fname == " ") or (lname == "" or lname == " ") or (age == "" or age == " ") or (address == "" or address == " ") or (phone == "" or phone == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students VALUES ('"+fname+"','"+lname+"','"+age+"','"+address+"','"+phone+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error")
            return


    refreshTable()
def Reset():
    ph1.set(" ")
    ph2.set(" ")
    ph3.set(" ")
    ph4.set(" ")
    ph5.set(" ")
    
    
    
def delete():
    decision = messagebox.askquestion("Warning!!", "Delete All data?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()


    

def close():
   
   x.quit()

def delet():
   
    refreshTable()

label = Label(x, text="Save Your Contacts Here!!", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)




fnameLabel = Label(x, text="FIRST NAME", font=('Arial', 15))
lnameLabel = Label(x, text="LAST NAME", font=('Arial', 15))
ageLabel = Label(x, text="AGE", font=('Arial', 15))
addressLabel = Label(x, text="Address", font=('Arial', 15))
phoneLabel = Label(x, text="Phone", font=('Arial', 15))

fnameLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
lnameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
ageLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
addressLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
phoneLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

fnameEntry = Entry(x, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
lnameEntry = Entry(x, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
ageEntry = Entry(x, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
addressEntry = Entry(x, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
phoneEntry = Entry(x, width=55, bd=5, font=('Arial', 15), textvariable = ph5)

fnameEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
lnameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
ageEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
addressEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
phoneEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)



addBtn = Button(x, text="Add", padx=65, pady=25, width=10,bd=5, font=('Arial', 15), bg="SKYBLUE", command=add)

updateBtn = Button(x, text="Delete", padx=65, pady=25, width=10,bd=5, font=('Arial', 15), bg="SKYBLUE", command=delet)

deleteBtn = Button(x, text="Reset", padx=65, pady=25, width=10,bd=5, font=('Arial', 15), bg="SKYBLUE", command=Reset)

closebtn=Button(x, text= "Exit", font=("Arial",15),bg="SKYBLUE",padx=65, pady=25, width=10,bd=5, command=close)
resetBtn = Button(x, text="Delete All Data", padx=65, pady=25, width=10,bd=5, font=('Arial', 15), bg="SKYBLUE", command=delete)





addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
closebtn.grid(row=11, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=9, column=5, columnspan=1, rowspan=2)


style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

A['columns'] = ("First Name","Last Name","Age","Address","Phone")

A.column("#0", width=0, stretch=NO)
A.column("First Name",  width=170)
A.column("Last Name",  width=150)
A.column("Age",  width=150)
A.column("Address",  width=165)
A.column("Phone",  width=150)

A.heading("First Name", text="First Name",anchor=W)
A.heading("Last Name", text="Last Name", anchor=W)
A.heading("Age", text="Age", anchor=W)
A.heading("Address", text="Address", anchor=W)
A.heading("Phone", text="Phone", anchor=W)

refreshTable()

x.mainloop()
