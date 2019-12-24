import  pymysql
from tkinter import *
from tkinter import ttk

conn=pymysql.connect(host="localhost",user="connectpj",password="connectpj")
cur = conn.cursor()
def create_db():
    cur.execute("CREATE DATABASE IF NOT EXISTS hospital_manager ")
    cur.execute("USE hospital_manager") 
    cur.execute("CREATE TABLE IF NOT EXISTS patient(p_id int PRIMARY KEY auto_increment ,p_name varchar(40),p_address varchar(300),p_diagnos varchar(300))")
    cur.execute("CREATE TABLE IF NOT EXISTS hospital(h_id int PRIMARY KEY auto_increment ,h_name varchar(40),h_city varchar(300),h_address varchar(300))")
    cur.execute("CREATE TABLE IF NOT EXISTS doctor(d_id int PRIMARY KEY auto_increment ,d_name varchar(40),d_salary numeric,d_qualification varchar(300)) ")
    cur.execute("CREATE TABLE IF NOT EXISTS medical(m_id int PRIMARY KEY auto_increment ,m_date_of_examine date,m_problem varchar(300))")
    cur.execute("CREATE TABLE IF NOT EXISTS parking(parking_id int PRIMARY KEY auto_increment ,vehical_no varchar(10))")
    print("done")

window=Tk()
window.title("HOSPITAL MANAGEMANT")
window.geometry("800x600")
def patient_d():
    create_db()
    p_name=p_ne.get()
    p_add=p_adde.get('1.0',END)
    p_dai=p_daie.get()
    cur.execute("USE hospital_manager") 
    cur.execute("INSERT INTO patient(p_name,p_address,p_diagnos) VALUES('%s','%s','%s')"%(p_name,p_add,p_dai))
    conn.commit()

def dr_details():
    create_db()
    p_name=d_ne.get()
    p_add=d_sale.get()
    p_dai=d_qule.get()
    cur.execute("USE hospital_manager") 
    cur.execute("INSERT INTO doctor(d_name,d_salary,d_qualification) VALUES('%s','%s','%s')"%(p_name,p_add,p_dai))
    conn.commit()

def hospital_d():
    create_db()
    p_name=h_ne.get()
    p_add=p_adde.get('1.0',END)
    p_dai=p_daie.get()
    cur.execute("USE hospital_manager") 
    cur.execute("INSERT INTO hospital(h_name,h_city,h_address) VALUES('%s','%s','%s')"%(p_name,p_add,p_dai))
    conn.commit()

pat=Label(window,text="Patient interface",height=1,width=20,justify="center")
pat.grid(row=0,column=0,columnspan=2)

#patiEnt
p_namel=Label(window,text="Name :-")
p_namel.grid(row=2,column=0)
p_ne=Entry(window,width=15)
p_ne.grid(row=2,column=2)

p_addl=Label(window,text="Address :-")
p_addl.grid(row=3,column=0)
p_adde=Text(window,width=15,height=5)
p_adde.grid(row=3,column=2)

p_diagl=Label(window,text="Diagnosis :-")
p_diagl.grid(row=4,column=0)
p_daie=Entry(window,width=15)
p_daie.grid(row=4,column=2)


p_insert=Button(window,text="Submit",command=patient_d)
p_insert.grid(row=5,column=2)

#dr
pat=Label(window,text="Doctor INTERFACE",height=1,width=20,justify="center")
pat.grid(row=0,column=5,columnspan=2)


d_namel=Label(window,text="Name :-")
d_namel.grid(row=2,column=5)
d_ne=Entry(window,width=15)
d_ne.grid(row=2,column=6)

d_sall=Label(window,text="Salary :-")
d_sall.grid(row=3,column=5)
d_sale=Entry(window,width=15)
d_sale.grid(row=3,column=6)

d_qull=Label(window,text="Qulification :-")
d_qull.grid(row=4,column=5)
d_qule=Entry(window,width=15)
d_qule.grid(row=4,column=6)


d_insert=Button(window,text="Submit",command=dr_details)
d_insert.grid(row=5,column=6)

#hospital
pat=Label(window,text="HOSPITAL",height=1,width=20,justify="center")
pat.grid(row=0,column=7,columnspan=2)


h_namel=Label(window,text="Name :-")
h_namel.grid(row=2,column=7)
h_ne=Entry(window,width=15)
h_ne.grid(row=2,column=8)

h_ctl=Label(window,text="City :-")
h_ctl.grid(row=3,column=7)
h_cte=Entry(window,width=15)
h_cte.grid(row=3,column=8)

h_addl=Label(window,text="Address :-")
h_addl.grid(row=4,column=7)
h_adde=Text(window,width=15,height=5)
h_adde.grid(row=4,column=8)




p_insert=Button(window,text="Submit",command=hospital_d)
p_insert.grid(row=5,column=8)


window.mainloop()