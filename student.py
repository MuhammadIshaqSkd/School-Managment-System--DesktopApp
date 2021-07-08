from tkinter import *

import tkinter as tk
from tkinter import *

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
e = tk.StringVar()
email_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray",textvariable = e)
email_entrybox.place(x=250,y=190,width=200,height=35)

# q = tk.StringVar()
pass_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
pass_entrybox.place(x=250,y=250,width=200,height=35)

#____________________Lables Entry Box and Title On Frame 2____________________________

title2 =Label(login_frame2,text="About Us",font=("Impact",20,"italic"),fg = "#0D0B0B",bg="#ede8ed").place(x=55,y=20)

dsc =Label(login_frame2,text=" This app is developed for manage schools and\ncollege records and provide online interface \nto the students, teacher and Admin for their \ndifferent quries. \n\n Created By @Muhammad Ishaq",font=("Goudy old style ",10,"bold"),fg = "#0D0B0B",bg="#ede8ed",borderwidth=0)
dsc.place(x=0,y=65)



def login():
    
    if email_entrybox.get() == ''or type(email_entrybox.get())!=str:
        m_box.showerror('Error','Please Enter Your Email')

    else:                     
        sql = "SELECT email FROM student WHERE email='%s'"%email_entrybox.get()  
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if not myresult:
                  m_box.showerror(f'Error','You Entered Wrong Email')
        else:
            sql = "SELECT pass FROM student WHERE pass='%s'"%pass_entrybox.get() 
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
x = 'open' 
def closeing_wn():
    mydb.close()
    l.destroy()

l.protocol('WM_DELETE_WINDOW',closeing_wn)
l.mainloop()

#_____________________END Window 1____________________

#_______Creating Window_________

win = Tk()
win.geometry("1199x600+100+50")
win.resizable(False,False)
win.title("Student Portal")


img = ImageTk.PhotoImage(Image.open("images\\signup.png"))
panel = Label(win, image = img)
panel.place(x = 0,y = 0)


Sida_pannel = Frame(win, bg ="white")
Sida_pannel.place(x=20,y=40,height=350,width=280)

sql = "select name from student WHERE email='%s'"%e.get()   
mycursor.execute(sql)
myresult = mycursor.fetchone()

#----------------- Lables On Main Screen -----------------------------------------------------

Label(win,text="Student ",font=("Goudy old style ",15),fg = "black",bg="white").place(x=40,y=60)
Label(win,text="Notifications ",font=("Goudy old style ",15),fg = "black",bg="white").place(x=40,y=140)
Label(win,text="",font=("Goudy old style ",15),fg = "black",bg="white").place(x=120,y=60)

#-----------------------------------------------------------------------------------------------

#----------------------Notification Bar--------------------------------------------------------

tex = Text(Sida_pannel,width=31,height=10)
tex.place(x=10,y=140)

#-----------------------------------------------------------------------------------------------

#------------------------- Loops ---------------------------------------------------------------

# for i in myresult:
#     la.config(text=i)
    
# sql2 = "select notis from notifications"
# mycursor.execute(sql2)
# myresult2 = mycursor.fetchall()

# output = ''
# for x in myresult2:
#     output = output+x[0]+ ''+'\n'
#     tex.insert(END,output)
    
#-----------------------------------------------------------------------------------------------

#----------------------- Back Ground Image Of main Screen --------------------------------------

img1 = ImageTk.PhotoImage(Image.open("images\\s_f.png"))
panel2 = Label(win, image = img1)
panel2.place(x =510,y = 60)

#-----------------------------------------------------------------------------------------------

#---------------------------- Functions -----------------------------------------------------

def view():
    win.withdraw()
    f2 = tk.Tk()
    f2.geometry("1300x300")
    f2.title("Your Records ")
        
    sql = "SELECT * FROM  student WHERE email='%s'"%e.get()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()          
    srm = ttk.Frame(f2)
    srm.place(x =50,y=50)

    tv = ttk.Treeview(srm,columns =(1,2,3,4,5,6,7),show='headings',height='5')
    tv.pack()

    tv.heading(1,text='Name',anchor = W)
    tv.heading(2,text='Age',anchor = W)
    tv.heading(3,text='Email',anchor = W)
    tv.heading(4,text='Gender',anchor = CENTER)
    tv.heading(5,text='Roll Number',anchor = W)
    tv.heading(6,text='Departement',anchor = W)
    tv.heading(7,text='Regular',anchor = W)

    for i in myresult:
        tv.insert('','end',values=i)

    def backs():
        win.deiconify()
        f2.destroy()
    back2_button = ttk.Button(f2, text = ' Back ',command=backs)
    back2_button.place(x=120,y=200,width=190,height=35)
    def on_closing():
        m_box.showinfo("Exit","You Need to logout First")
    f2.protocol("WM_DELETE_WINDOW",on_closing)
    f2.mainloop()
def report():

        win.withdraw()
        rp  = tk.Tk()
        
        rp.geometry("700x300")
        rp.title("Result")

        re_frame = ttk.Frame(rp)
        re_frame.place(x =50,y=50)

        err_var = StringVar()
        error_entrybox =Entry(rp,font=("times new roman",10),bg="white",textvariable = err_var)
        error_entrybox.place(x=250,y=50,width=350,height=170)


        def backss():
                win.deiconify()
                rp.destroy()
        def submit():

                err_rep = error_entrybox.get()
                sql = "INSERT INTO error (errors) VALUES (%s)"
                val =  (err_rep,)
    

                mycursor.execute(sql, val)

                mydb.commit()

                print(mycursor.rowcount, "Data Is Suessfully Saved")

        back3_button = ttk.Button(rp, text = ' Back ',command=backss)
        back3_button.place(x=90,y=250,width=190,height=35)

        back4_button = ttk.Button(rp, text = ' Submit Error ',command=submit)
        back4_button.place(x=350,y=250,width=190,height=35)
        def on_closing():
            m_box.showinfo("Exit","You Need to logout First")

        rp.protocol("WM_DELETE_WINDOW",on_closing)
        rp.mainloop()

def logout():
    win.destroy()

def cresult():
    win.withdraw()
    f3 = tk.Tk()
    f3.geometry("1300x300")
    f3.title("Your Records ")
    sql="SELECT * FROM result left JOIN student ON result.rollno = student.rollno WHERE email='%s'"%e.get()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()                                        
    srm = ttk.Frame(f3)
    srm.place(x =50,y=50)

    tv = ttk.Treeview(srm,columns =(1,2,3,4,5,6),show='headings',height='5')
    tv.pack()

    tv.heading(1,text='Subject Name',anchor = W)
    tv.heading(2,text='Roll Number',anchor = W)
    tv.heading(3,text='Assignment Marks',anchor = W)
    tv.heading(4,text='Quiz Marks',anchor = W)
    tv.heading(5,text='Grade',anchor = W)
    tv.heading(6,text='Attendence %',anchor = W)

    for i in myresult:
        tv.insert('','end',values=i)
           
    def backs():
        win.deiconify()
        f3.destroy()
                
    back2_button = ttk.Button(f3, text = ' Back ',command=backs)
    back2_button.place(x=120,y=200,width=190,height=35)
    def on_closing():
        m_box.showinfo("Exit","You Need to logout First")
        f3.protocol("WM_DELETE_WINDOW",on_closing)
    f3.mainloop()   

def fees():
    
    win.withdraw()
    stdr = tk.Tk()

    stdr.title("Fees")
    stdr.geometry("600x400+100+50")
    stdr.resizable(False,False)

   
    lbl2 =Label(stdr,text="Enter Your Roll Number ",font=("Goudy old style ",15),fg = "#0D0B0B",bg="#d9d7d4").place(x=170,y=50)

    def searchss():


        sql = "SELECT * FROM fees WHERE rollno='%s'"%search_entrybox.get()   
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        





        if not myresult:
            m_box.showerror('Error','Record is not found')
            
                    
        else:

            stdr.withdraw()
            f3 = tk.Tk()
            f3.geometry("1100x300")
            f3.title("Your Records ")
            
            srm = ttk.Frame(f3)
            srm.place(x =50,y=50)

            tv = ttk.Treeview(srm,columns =(1,2,3,4,5),show='headings',height='5')
            tv.pack()

            tv.heading(1,text='Semseter',anchor = W)
            tv.heading(2,text='Roll Number',anchor = W)
            tv.heading(3,text='Late fees',anchor = W)
            tv.heading(4,text='Fine',anchor = W)
            tv.heading(5,text='Total Fee',anchor = W)


            for i in myresult:
                tv.insert('','end',values=i)

            

            def backs():
                stdr.deiconify()
                f3.destroy()

            back2_button = ttk.Button(f3, text = ' Back ',command=backs)
            back2_button.place(x=120,y=200,width=190,height=35)
            def on_closing():
                m_box.showinfo("Exit","You Need to logout First")

            f3.protocol("WM_DELETE_WINDOW",on_closing)
            f3.mainloop()

    def backv():
        win.deiconify()
        stdr.destroy()

    l_btns = ttk.Button(stdr,text = "Search",command=searchss)
    l_btns.place(x=170,y=150,width=220,height=55)
        
    l_btns = ttk.Button(stdr,text = "Back",command=backv)
    l_btns.place(x=170,y=250,width=220,height=55)

    search_entrybox =Entry(stdr,font=("times new roman",15),bg="lightgray")
    search_entrybox.place(x=170,y=100,width=220,height=35)

    def on_closing():
        m_box.showinfo("Exit","You Need to logout First")

    stdr.protocol("WM_DELETE_WINDOW",on_closing)
    stdr.mainloop()
 
#-----------------------------------------------------------------------------------------------

#------------------------------ Buttons On main Screen -----------------------------------------

l_btn1 = ttk.Button(win,text = "View Record",command=view)
l_btn1.place(x=320,y=300,width=210,height=55)

l_btn2 = ttk.Button(win,text = "Check Result",command = cresult)
l_btn2.place(x=320,y=400,width=210,height=55)

l_btn3 = ttk.Button(win,text = "Report Error",command=report)
l_btn3.place(x=600,y=300,width=210,height=55)

l_btn4 = ttk.Button(win,text = "Fees",command=fees)
l_btn4.place(x=600,y=400,width=210,height=55)

l_btn5 = ttk.Button(win,text = "Log out",command=logout)
l_btn5.place(x=470,y=490,width=210,height=55)

#-----------------------------------------------------------------------------------------------



win.mainloop()