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
        sql = "SELECT email FROM teacher WHERE email='%s'"%email_entrybox.get()  
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if not myresult:
                  m_box.showerror(f'Error','You Entered Wrong Email')
        else:
            sql = "SELECT pass FROM teacher WHERE pass='%s'"%pass_entrybox.get() 
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if not myresult:
                  m_box.showerror(f'Error','You Entered Wrong Password')
            else:
                l.destroy()
def reg():
      
      l.destroy()
      import signup      

def exit():
      mydb.close()
      l.destroy()

ttk.Style().configure("TButton", padding=6, relief="flat",background="#d25d17")

l_btn1 = ttk.Button(l,text = "Login",command = login)
l_btn1.place(x=330,y=445,width=190,height=35)

l_btn2 = ttk.Button(l,text = 'sign up',command = reg)
l_btn2.place(x=330,y=492,width=190,height=35)

l_btn3 = ttk.Button(l,text = 'Exit',command = exit)
l_btn3.place(x=330,y=540,width=190,height=35)

def closeing_wn():
      mydb.close()
      l.destroy()

l.protocol('WM_DELETE_WINDOW',closeing_wn)
l.mainloop()

#_____________________END Window 1____________________

# #_______Creating Window 2_________

win = Tk()
win.geometry("1199x600+100+50")
win.resizable(False,False)
win.title("Student Portal")


img = ImageTk.PhotoImage(Image.open("images\\signup.png"))
panel = Label(win, image = img)
panel.place(x = 0,y = 0)

sql = "select name from teacher where pass = %s"%q.get()
mycursor.execute(sql)
myresult = mycursor.fetchone()

la2=Label(win,text="Teacher ",font=("Goudy old style ",15),fg = "#0D0B0B",bg="#d9d7d4")
la2.place(x=40,y=60)

la=Label(win,text="",font=("Goudy old style ",15),fg = "#0D0B0B",bg="#d9d7d4")
la.place(x=120,y=60)
for i in myresult:
    la.config(text=i)


img1 = ImageTk.PhotoImage(Image.open("images\\s_f.png"))
panel2 = Label(win, image = img1)
panel2.place(x =510,y = 60)


def results():

    win.withdraw()
    rs = tk.Tk()
    rs.title("Result")
    rs.geometry("700x700+100+50")
    rs.resizable(False,False)

    login_frame = Frame(rs, bg ="white")
    login_frame.place(x=70,y=60,height=600,width=500)

    
    title =Label(login_frame,text="Annual Exmination Result ",font=("Goudy old style ",19,"bold"),fg = "#0D0B0B",bg="white").place(x=40,y=50)

    lbl1 =Label(login_frame,text="Enter Subject Name ",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=40,y=120)
    subj_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
    subj_entrybox.place(x=270,y=120,width=200,height=35)

    lbl2 =Label(login_frame,text="Enter Rollno Of Student",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=40,y=170)
    roll_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
    roll_entrybox.place(x=270,y=170,width=200,height=35)

    lbl3 =Label(login_frame,text="Assignments Marks",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=40,y=220)
    am_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
    am_entrybox.place(x=270,y=220,width=200,height=35)

    lbl4 =Label(login_frame,text="Quizs Marks",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=40,y=270)
    qm_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
    qm_entrybox.place(x=270,y=270,width=200,height=35)

    lbl5 =Label(login_frame,text="Grade",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=40,y=320)
    g_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
    g_entrybox.place(x=270,y=320,width=200,height=35)

    lbl6 =Label(login_frame,text="Attendance % ",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=40,y=370)
    ad_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
    ad_entrybox.place(x=270,y=370,width=200,height=35)

    def submits():

        std_amm = am_entrybox.get()
        std_qmm = qm_entrybox.get()
        std_add = ad_entrybox.get()

        if subj_entrybox.get() == ''or type(subj_entrybox.get())!=str:
            m_box.showerror('Error','Please Enter Subject Name')
        
        elif subj_entrybox.get() == '':
                     
            m_box.showerror('Error','Please Enter Roll Number')
        elif am_entrybox.get() == '':
            m_box.showerror('Error','Please Enter Assignment Marks')


        elif qm_entrybox.get() == '':            
            m_box.showerror('Error','Please Enter Quize Marks')
        
        elif g_entrybox.get() == '' or type(qm_entrybox.get())!=str:            
            m_box.showerror('Error','Please Enter Grades')

        elif ad_entrybox.get() == '':
                m_box.showerror('Error','Please Enter Attendance')

        try:
            std_amm = int(std_amm)
        except ValueError:
            m_box.showerror('Error','Please Enter Assigmnent Marks in Numbers')  

        try:
            std_qmm = int(std_qmm)
        except ValueError:
            m_box.showerror('Error','Please Enter Quiz Marks in Numbers')
        try:
            std_add = int(std_add)
        except ValueError:
            m_box.showerror('Error','Please Enter Attendance Marks in Numbers')

        else:
            std_subj = subj_entrybox.get()
            std_roll = roll_entrybox.get()
            std_am = am_entrybox.get()
            std_qm = qm_entrybox.get()
            std_g = g_entrybox.get()
            std_ad = ad_entrybox.get()

            sql = "SELECT subjname FROM result WHERE subjname='%s'"%subj_entrybox.get()
        
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if not myresult:

                sql = "INSERT INTO result (subjname, rollno,AM,QM,Grade,attd) VALUES (%s,%s,%s,%s,%s,%s)"
                val =  (std_subj,std_roll, std_am,std_qm,std_g,std_ad)
                    

                mycursor.execute(sql, val)

                mydb.commit()
                subj_entrybox.delete(0,tk.END)
                roll_entrybox.delete(0, tk.END)
                am_entrybox.delete(0, tk.END)
                qm_entrybox.delete(0, tk.END)
                g_entrybox.delete(0, tk.END)
                ad_entrybox.delete(0, tk.END)

                print(mycursor.rowcount, "Data Is Suessfully Saved")
                sb ="Data Is suessfully Saved " 

                lbl7 =Label(login_frame,text="Data Is suessfully Saved ",font=("Goudy old style ",20),fg = "#0D0B0B",bg="white").place(x=40,y=550)

            else:
                m_box.showwarning('Error','This Subject Result is aleady Submited')



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

def logout():
    win.destroy()
    import Login
    


l_btn1 = ttk.Button(win,text = "Enter Result",command=results)
l_btn1.place(x=500,y=300,width=210,height=55)

l_btn2 = ttk.Button(win,text = "Log out",command=logout)
l_btn2.place(x=500,y=400,width=210,height=55)


win.mainloop()