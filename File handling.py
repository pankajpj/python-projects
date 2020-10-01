from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from csv import DictWriter
import os
from csv import DictReader
from fpdf import FPDF

#window creation
master = Tk()
master.title("FLoginForm")
master.geometry("800x600")


#global declaration
nm=''
lm=''
mob=''
email=''
sp=''
cb=''
def getvar():
    global nm
    global lm
    global mob
    global email
    global x7
    global x8
    nm=e1.get()
    lm=e2.get()
    email=e3.get()
    mob=e4.get()
    x7=sp.get()
    x8=cb.get()

#validation
def msg():
    #echeck ="@gmail.com"
    EMAIL_REGEX = re.compile(r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
    
    getvar()

    print("FirstName :",nm)
    print("LastName :",lm)

    if(len(mob)==10 and mob.isdigit() ): 
        print("mobile.no :",mob)
    else:
        messagebox.showinfo("Error", "Enter number properly")      
   

    if not EMAIL_REGEX.match(email):
        messagebox.showinfo("Error", "Enter email properly") 
    else:
        print("Email :",email)

def pdf_file():

    document=FPDF()
    document.add_page()
    document.set_font("Arial", size=15)
    document.cell(200, 10, txt="First name:\t", ln=1, align="L")
    document.cell(200, 10,nm, ln=1, align="R")
    document.cell(200, 10, txt="Last name:\t", ln=2, align="L")
    document.cell(200, 10,lm, ln=2, align="R")
    document.cell(200, 10, txt="Mobile No:", ln=3, align="L")
    document.cell(200, 10,mob, ln=3, align="R")
    document.cell(200, 10, txt="Email:\t", ln=4, align="L")
    document.cell(200, 10,email, ln=4, align="R")
    document.cell(200, 10, txt="Age:\t", ln=5, align="L")
    document.cell(200, 10,x7, ln=5, align="R")
    document.cell(200, 10, txt="Gender\t", ln=6, align="L")
    document.cell(200, 10,x8, ln=6, align="R")
    document.output("pdf_file.pdf")
    document=FPDF(orientation='P', unit='mm', format='A3')
    print("pdf has been created successfully....")


#writing csv file

def csv():
    vm=msg()
    if os.path.exists("cvdem.csv"):
        file =open('csdem.csv','a')
        if(vm=='mtrue'):
            csw_write=csv.writer(file)
            csw_write.writerow([nm,lm,email,mob,x7,x8])
        else:
            messagebox.showinfo("Error","something is wrong")
    else:
        file =open('csdem.csv','a')
        dict_write=DictWriter(file,fieldnames=['Firstname','Lastname','Email','Mobile No','Age','Gender'])
        dict_write.writeheader()
        dict_write.writerow({'Firstname':nm,'Lastname':lm,'Email':email,'Mobile No':mob,'Age':x7,'Gender':x8})
     
  
   

#writing  txt file
def file():
    getvar()
    f=open("records.txt","w")
    f.write("First Name:\t")
    f.write(nm)
    f.write("\n")
    f.write("Last Name:\t")
    f.write(lm)
    f.write("\n")
    f.write("mobile.no:\t")
    f.write(mob)
    f.write("\n")
    f.write("Email:\t")
    f.write(email)
    f.write("\n")
    f.write("Age:\t")
    f.write(x7)
    f.write("\n")
    f.write("Gender:\t")
    f.write(x8)
    f.write("\n")
#append to a text file
def appen():
 
    
    getvar()
    msg()
    csv()
    if os.path.exists("records.txt"):
        f=open("records.txt","a")
        f.write("First Name:\t")
        f.write(nm)
        f.write("\n")
        f.write("Last Name:\t")
        f.write(lm)
        f.write("\n")
        f.write("mobile.no:\t")
        f.write(mob)
        f.write("\n")
        f.write("Email:\t")
        f.write(email)
        f.write("\n")
        f.write("Age:\t")
        f.write(x7)
        f.write("\n")
        f.write("Gender:\t")
        f.write(x8)
        f.write("\n")

    else:

        file()   

    


#read txt file function
def read_data():
    w=Text(master,wrap=WORD,width='20',height='10',bd=5)
    scr=Scrollbar(master, orient=VERTICAL, command=w.yview)
    
    f=open("records.txt","r")
    w.insert(INSERT,f.read())
    w.grid(row=15,column=1)
    scr.grid(row=15, column=2, rowspan=15, columnspan=1, sticky=NS)
    
    btn = Button(master, text='Delete', command=lambda: w.delete(1.0,END))
    btn.grid(row=10,column=1)

#read csv function:
def read_csv():
   
    f=open('csdem.csv','r')
    read=DictReader(f)
    for row in read:

        print("Firstname:",row['Firstname'])
        print("Lastname:",row['Lastname'])
        print("Email:",row['Email'])
        print("Mobile.No:",row['Mobile No'])
        print("Age:",row['Age'])
        print("Gender:",row['Gender'])

#widgets
radio=IntVar()
check=IntVar()
sp=IntVar()
c1=["Male","Female"]
enm=Label(master,text="First Name:-").grid(row=0)
elm=Label(master,text="Last Name:-").grid(row=1)
em=Label(master, text="Mob No:-").grid(row=2)
email=Label(master,text="Email:-").grid(row=3)
ag=Label(master,text="Age:-").grid(row=4)
c=Label(master,text="Select Gender")
c.grid(row=5)
cb=ttk.Combobox(master,values=c1,width=16)
cb.grid(row=5,column=1)
cb.current(0)
gen=Radiobutton(master,text="Eligible",variable=radio,value=1).grid(row=6,column=0)
gen1=Radiobutton(master,text="Not Eligible",variable=radio,value=2).grid(row=6,column=1)
sp=Spinbox(master,from_=0,to = 25,width=16,bd=1)
sp.grid(row=4,column=1)
term=Checkbutton(master,text="Agree Terms And Conditions",variable=check,onvalue=1,offvalue=0).grid(row=7,column=1) 

#buttons
b1=Button(master,text="Submit",command=appen).grid(row=8,column=0)
b3=Button(master,text="quit",command=master.destroy).grid(row=8,column=1)
b4=Button(master,text="Get txt",command=read_data).grid(row=9,column=0)
b5=Button(master,text="Get csv",command=read_csv).grid(row=9,column=1)
b6=Button(master,text="Get pdf",command=pdf_file).grid(row=9,column=2)

#entry Widget
e1=Entry(master,bd=1,width=18)
e2=Entry(master,bd=1,width=18)
e3=Entry(master,bd=1,width=18)
e4=Entry(master,bd=1,width=18)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=3,column=1)
e4.grid(row=2,column=1)
master.mainloop()