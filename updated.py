import tkinter as tk
from tkinter import messagebox
import re
master = tk.Tk()
master.title("Form")
master.geometry("400x300")
def msg():
    EMAIL_REGEX = re.compile(r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$") 
    namep=e1.get()
    mobp=e2.get()
    emp=e3.get()

    print("Name :",namep)
    if(len(mobp)==10 and mobp.isnumeric() ): 
        print("mobile.no :",mobp)
    else:
        messagebox.showinfo("Error", "Enter number properly")      
    if not EMAIL_REGEX.match(emp):

         messagebox.showinfo("Error", "Enter email properly") 
    else:
        print("Email :",emp)

def stop():
    master.destroy()


tk.Label(master, text="Name:-") .grid(row=0)
tk.Label(master, text="Mob No:-").grid(row=1)
tk.Label(master, text="Email:-").grid(row=2)
tk.Button(master,text="Submit",command=msg).grid(row=5,column=0)
tk.Button(master,text="Quit",command=stop).grid(row=5,column=1)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2,column=1)
master.mainloop()