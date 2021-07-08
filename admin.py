from tkinter import *
import tkinter as tk

from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox as m_box

import os


#__________________DataBase_________________

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="school"
)
mycursor = mydb.cursor()
#____________Login Window______________________

l = Tk()
l.title("Login")
l.geometry("1199x600+100+50")
l.resizable(False,False)

l.wm_iconbitmap('icon.ico')

img = ImageTk.PhotoImage(Image.open("images\\new2.png"))
panel = Label(l, image = img)
panel.place(x = 0,y = 0)

#========login frame=======

login_frame = Frame(l, bg ="white")
login_frame.place(x=200,y=50,height=500,width=500)

login_frame2 = Frame(l, bg ="#ede8ed")
login_frame2.place(x=800,y=80,height=230,width=300)

#___________Lables Entry Box and Title On Frame 1____________________

Label(login_frame,text="Login Here",font=("Impact",35,"bold"),fg = "#0D0B0B",bg="white").place(x=120,y=20)
Label(login_frame,text="School Managment System \nLogin Area",font=("Goudy old style ",15,"bold"),fg = "#d25d17",bg="white").place(x=100,y=100)


Label(login_frame,text="User Email",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=60,y=190)

Label(login_frame,text="User Password",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=60,y=250)
ee = tk.StringVar()
email_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray",textvariable = ee)
email_entrybox.place(x=250,y=190,width=200,height=35)

q = tk.StringVar()
pass_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray",textvariable = q)
pass_entrybox.place(x=250,y=250,width=200,height=35)

#____________________Lables Entry Box and Title On Frame 2____________________________

title2 =Label(login_frame2,text="About Us",font=("Impact",20,"italic"),fg = "#0D0B0B",bg="#ede8ed").place(x=55,y=20)

dsc =Label(login_frame2,text=" This app is developed for manage schools and\ncollege records and provide online interface \nto the students, teacher and Admin for their \ndifferent quries. \n\n Created By @Muhammad Ishaq",font=("Goudy old style ",10,"bold"),fg = "#0D0B0B",bg="#ede8ed",borderwidth=0)
dsc.place(x=0,y=65)



def login():
    
    if email_entrybox.get() == ''or type(email_entrybox.get())!=str:
        m_box.showerror('Error','Please Enter Your Email')

    else:                     
        sql = "SELECT email FROM admins WHERE email='%s'"%email_entrybox.get()  
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if not myresult:
                  m_box.showerror(f'Error','You Entered Wrong Email')
        else:
            sql = "SELECT pass FROM admins WHERE pass='%s'"%pass_entrybox.get() 
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if not myresult:
                  m_box.showerror(f'Error','You Entered Wrong Password')
            else:
                l.destroy()     

def exit():
      mydb.close()
      l.destroy()

ttk.Style().configure("TButton", padding=6, relief="flat",background="#d25d17")

l_btn1 = ttk.Button(l,text = "Login",command = login)
l_btn1.place(x=330,y=445,width=190,height=35)

l_btn3 = ttk.Button(l,text = 'Exit',command = exit)
l_btn3.place(x=330,y=492,width=190,height=35)

def closeing_wn():
      mydb.close()
      l.destroy()

l.protocol('WM_DELETE_WINDOW',closeing_wn)
l.mainloop()

#_____________________END Window 1____________________


#_____________________________Window 2______________________

win = Tk()
win.geometry("1199x600+100+50")
win.resizable(False,False)
win.title("Student Portal")


img = ImageTk.PhotoImage(Image.open("images\\admin back2.jpg"))
panel = Label(win, image = img)
panel.place(x = 0,y = 0)

sql = "select name from admins where pass = %s"%q.get()
mycursor.execute(sql)
myresult = mycursor.fetchone()

la2=Label(win,text="Admin ",font=("Goudy old style ",15),fg = "#0D0B0B",bg="#d9d7d4")
la2.place(x=40,y=60)

la=Label(win,text="",font=("Goudy old style ",15),fg = "#0D0B0B",bg="#d9d7d4")
la.place(x=120,y=60)
for i in myresult:
    la.config(text=i)

img1 = ImageTk.PhotoImage(Image.open("images\\admin1.png"))
panel2 = Label(win, image = img1)
panel2.place(x =500,y = 40)

def fees():
    win.withdraw()
    rs = tk.Tk()
    rs.title("Fees")
    rs.geometry("700x700+100+50")

    login_frame = Frame(rs, bg ="white")
    login_frame.place(x=70,y=60,height=500,width=500)

    
    title =Label(login_frame,text="Annual Semseter Fees ",font=("Goudy old style ",19,"bold"),fg = "#0D0B0B",bg="white").place(x=40,y=50)

    lbl1 =Label(login_frame,text="Semseter of Student ",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=40,y=120)
    sm_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
    sm_entrybox.place(x=270,y=120,width=200,height=35)

    lbl2 =Label(login_frame,text="Enter Rollno of Student",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=40,y=170)
    roll_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
    roll_entrybox.place(x=270,y=170,width=200,height=35)

    lbl3 =Label(login_frame,text="Late Fee",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=40,y=220)
    lf_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
    lf_entrybox.place(x=270,y=220,width=200,height=35)

    lbl4 =Label(login_frame,text="Fine",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=40,y=270)
    f_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
    f_entrybox.place(x=270,y=270,width=200,height=35)

    lbl5 =Label(login_frame,text="Total Fee",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=40,y=320)
    tl_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
    tl_entrybox.place(x=270,y=320,width=200,height=35)

    def submits():
    
        std_sm = sm_entrybox.get()
        std_roll = roll_entrybox.get()
        std_lf = lf_entrybox.get()
        std_f = f_entrybox.get()
        std_tl = tl_entrybox.get()


        sql = "INSERT INTO fees (semseter, rollno,latefees,fine,total) VALUES (%s,%s,%s,%s,%s)"
        val =  (std_sm,std_roll, std_lf,std_f,std_tl)
                
        mycursor.execute(sql, val)
        mydb.commit()
        sm_entrybox.delete(0,tk.END)
        roll_entrybox.delete(0, tk.END)
        lf_entrybox.delete(0, tk.END)
        f_entrybox.delete(0, tk.END)
        tl_entrybox.delete(0, tk.END)
        print(mycursor.rowcount, "Data Is Suessfully Saved")




    def back():
        win.deiconify()
        rs.destroy()
        

    l_btn1 = ttk.Button(login_frame,text = "Submit",command=submits)
    l_btn1.place(x=270,y=430,width=210,height=55)

    l_btn2 = ttk.Button(login_frame,text = "Back",command=back)
    l_btn2.place(x=40,y=430,width=210,height=55)

    def on_closing():
        m_box.showinfo("Exit","You Need to logout First")

    rs.protocol("WM_DELETE_WINDOW",on_closing)
    rs.mainloop()

def errors():
    s = tk.Tk()
    win.withdraw()
    s.title("Error")


    s.geometry("400x400+100+50")
    s.resizable(False,False)


    sql = "SELECT * FROM error"   
    mycursor.execute(sql)
    myresult = mycursor.fetchall()


    tv = ttk.Treeview(s,columns =(1),show='headings',height='5')
    tv.pack(padx=0,pady=50)

    tv.heading(1,text='Error Reports',anchor = W)



    for i in myresult:
        tv.insert('','end',values=i)

    def backs():
        win.deiconify()
        s.destroy()

    back2_button = ttk.Button(s, text = ' Back ',command=backs)
    back2_button.place(x=100,y=200,width=190,height=35)

    def on_closing():
        m_box.showinfo("Exit","You Need to logout First")

    s.protocol("WM_DELETE_WINDOW",on_closing)

    s.mainloop()

def upadtes():
    
    win.withdraw()
    root = Tk()
    wraper1 = LabelFrame(root,text = "\n \nRecords")
    wraper2 = LabelFrame(root,text="\n \nSearch ")

    
    wraper1.pack(fill = "both",expand="yes",padx=20,pady=10)
    wraper2.pack(fill = "both",expand="yes",padx=20,pady=10)

#__________________________Functions____________________________

    def upadtess(myresult):
        tv.delete(*tv.get_children())
        for i in myresult:
            tv.insert('','end',values=i)


    def search():

        if type_combobox.get() == 'Student':      
            sql = "SELECT * FROM student WHERE name='%s'"%ent.get()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            upadtess(myresult)
        else:
            sql = "SELECT * FROM teacher WHERE name='%s'"%ent.get()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            upadtess(myresult)

    def all_rec():

        if type_combobox.get() == 'Student':
            sql = "SELECT * FROM student"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            upadtess(myresult)
        else:
            sql = "SELECT * FROM teacher"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            upadtess(myresult)

    def back_admin():
        root.destroy()
        win.deiconify()

#___________________Function END________________________________

#_______________________Tree View _____________________________

    tv = ttk.Treeview(wraper1,columns =(1,2,3,4,5,6),show='headings',height='5')
    tv.pack()
    tv.heading(1,text='Name',anchor = W)
    tv.heading(2,text='Age',anchor = W)
    tv.heading(3,text='Email',anchor = W)
    tv.heading(4,text='Gender',anchor = CENTER)
    tv.heading(5,text='Department',anchor = W)
    tv.heading(6,text='Regular',anchor = W)
    sql = "SELECT * FROM student"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    upadtess(myresult)
#____________________________END_______________________________

#_________________Wraper 1______________________________________
    btn1 = ttk.Button(wraper1,text = " VIEW ALL Records ",command=all_rec)
    btn1.place(x=400,y=190,width=200,height = 35)

    btn2 = ttk.Button(wraper1,text = " Back To Admin Pannel",command=back_admin)
    btn2.place(x=400,y=250,width=200,height = 35)

#__________________END_________________________________________

#________________Wraper 2______________________________________

    ent = Entry(wraper2)
    ent.place(x=420,y=10,width=190,height=30)


    type_combobox = ttk.Combobox(wraper2,width = 13, state = 'readonly')
    type_combobox['values'] = ('Teacher','Student')
    type_combobox.place(x=420,y=50,width=190,height=30)
    type_combobox.current(0)
    btn = ttk.Button(wraper2, text="Search",command = search)
    btn.place(x=420,y=100,width=190,height=35)

#__________________________END______________________________   
    root.title("Records")
    root.geometry("1200x700+150+0")

    def on_closing():
        m_box.showinfo("Exit","You Need to logout First")

    root.protocol("WM_DELETE_WINDOW",on_closing)
    
    root.mainloop()


def add_new():
    win.destroy()
    import signupteacher

def add_student():
    win.destroy()
    import signup

def delete_re():
    win.withdraw()
    de = Tk()
    de.geometry("800x700+100+50")


    df = Frame(de, bg ="white")
    df.place(x=70,y=60,height=600,width=660)

    def upadtess(myresult):
        tv.delete(*tv.get_children())
        for i in myresult:
            tv.insert('','end',values=i)       
        btn3= ttk.Button(df,text="Confrim Delete",command=condele)
        btn3.place(x=160,y=410,width=190,height=30)

    def condele():
        query = "DELETE  FROM student WHERE email='%s'"%entr.get() 
        mycursor.execute(query)
        mydb.commit()
        lblc = Label(df,text="This Record Has Been Deleted",font=("Goudy old style ",15,"bold"),fg = "#0D0B0B",bg="white")
        lblc.place(x=40,y=530)

    def deler():
        if type_combobox.get() == 'Student':      
            sql = "SELECT * FROM student WHERE email='%s'"%entr.get()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if not myresult:
                m_box.showinfo("Not Found","This Record is not found in Student Record")
            else:
                upadtess(myresult)
        else:
            sql = "SELECT * FROM teacher WHERE email='%s'"%entr.get()
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if not myresult:
                m_box.showinfo("Not Found","This Record is not found in Student Record")
            else:
                upadtess(myresult)

    def back():
        de.destroy()
        win.deiconify()

    btn = ttk.Button(df,text="Delete",command=deler)
    btn.place(x=160,y=240,width=190,height=30)

    btn2 = ttk.Button(df,text="Back To Admin Pannel",command=back)
    btn2.place(x=160,y=480,width=190,height=30)

    type_combobox = ttk.Combobox(df,width = 13, state = 'readonly')
    type_combobox['values'] = ('Teacher','Student')
    type_combobox.place(x=160,y=190,width=190,height=30)
    type_combobox.current(0)

    lbl =Label(df,text="Enter The Email that you want to Delete",font=("Goudy old style ",15,"bold"),fg = "#0D0B0B",bg="white")
    lbl.place(x=60,y=30)

    lbl2 =Label(df,text="Enter email in this format i.e abc.gmail.com",font=("Goudy old style ",10),fg = "#0D0B0B",bg="white")
    lbl2.place(x=140,y=100)

    entr = ttk.Entry(df)
    entr.place(x=160,y=150,width=190,height=30)

    tv = ttk.Treeview(df,columns =(1,2,3),show='headings',height='5')
    tv.place(x=10,y=290,width=640,height=90)
    tv.heading(1,text='Name',anchor = W)
    tv.heading(2,text='Age',anchor = W)
    tv.heading(3,text='Email',anchor = W)

    def on_closing():
        m_box.showinfo("Exit","You Need to logout First")

    de.protocol("WM_DELETE_WINDOW",on_closing)

    de.mainloop()

def log():
    win.destroy()

l_btn1 = ttk.Button(win,text = "Errors Reports",command=errors)
l_btn1.place(x=900,y=330,width=200,height=50)

l_btn2 = ttk.Button(win,text = "Records ",command=upadtes)
l_btn2.place(x=650,y=330,width=200,height=50)

l_btn3 = ttk.Button(win,text = "Fees",command=fees)
l_btn3.place(x=390,y=330,width=200,height=50)

l_btn4 = ttk.Button(win,text = "Add New Teacher",command=add_new)
l_btn4.place(x=150,y=330,width=200,height=50)

l_btn5 = ttk.Button(win,text = "Update Record",command=log)
l_btn5.place(x=330,y=520,width=200,height=50)

l_btn8 = ttk.Button(win,text = "Add New Student",command=add_student)
l_btn8.place(x=100,y=520,width=200,height=50)

l_btn6 = ttk.Button(win,text = "Delete Record",command=delete_re)
l_btn6.place(x=550,y=520,width=200,height=50)

l_btn7 = ttk.Button(win,text = "Log Out",command=log)
l_btn7.place(x=800,y=520,width=200,height=50)

win.mainloop()