from tkinter import *
import tkinter as tk
import time
from PIL import ImageTk, Image

from tkinter import ttk
import os
from tkinter import messagebox as m_box




#__________________DataBase_________________


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="school"
)

mycursor = mydb.cursor()

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

title =Label(login_frame,text="Login Here",font=("Impact",35,"bold"),fg = "#0D0B0B",bg="white").place(x=120,y=20)
dsc =Label(login_frame,text="School Managment System \nLogin Area",font=("Goudy old style ",15,"bold"),fg = "#d25d17",bg="white").place(x=100,y=100)


lbl1 =Label(login_frame,text="User Email",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=60,y=190)

lbl2 =Label(login_frame,text="User Password",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=60,y=250)

lbl3 =Label(login_frame,text="Select Your Type",font=("Goudy old style ",15),fg = "#0D0B0B",bg="white").place(x=60,y=315)

type_combobox = ttk.Combobox(login_frame,width = 13, state = 'readonly')
type_combobox['values'] = ('Teacher','Student','Admin')
type_combobox.place(x=250,y=310,width=195,height=35)
type_combobox.current(0)

email_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
email_entrybox.place(x=250,y=190,width=200,height=35)

pass_entrybox =Entry(login_frame,font=("times new roman",15),bg="lightgray")
pass_entrybox.place(x=250,y=250,width=200,height=35)

#____________________Lables Entry Box and Title On Frame 2____________________________

title2 =Label(login_frame2,text="About Us",font=("Impact",20,"italic"),fg = "#0D0B0B",bg="#ede8ed").place(x=55,y=20)

dsc =Label(login_frame2,text=" This app is developed for manage schools and\ncollege records and provide online interface \nto the students, teacher and Admin for their \ndifferent quries. \n\n Created By @Muhammad Ishaq",font=("Goudy old style ",10,"bold"),fg = "#0D0B0B",bg="#ede8ed",borderwidth=0)
dsc.place(x=0,y=65)



def login():
    

      if email_entrybox.get() == ''or type(email_entrybox.get())!=str:
            m_box.showerror('Error','Please Enter Your Email')
      elif type_combobox.get()=='Teacher':

            sql = "SELECT email FROM teacher WHERE email='%s'"%email_entrybox.get()  
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if not myresult:
                  m_box.showerror(f'Error','You Entered Wrong Email')
            else:
                  my_progressbar = ttk.Progressbar(l, orient=HORIZONTAL,
                  length=400,mode = 'determinate')
                  my_progressbar.place(x=250,y=410)                 
                  for x in range(10):                    
                        my_progressbar['value'] +=10
                        l.update_idletasks()
                        time.sleep(1)
                        if x == 9:
                              l.destroy()
                              import teacher

      elif type_combobox.get()=='Student':    
                  
            sql = "SELECT email FROM student WHERE email='%s'"%email_entrybox.get()  
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if not myresult:
                  m_box.showerror(f'Error','You Entered Wrong Email')
            else:
                  my_progressbar = ttk.Progressbar(l, orient=HORIZONTAL,
                  length=400,mode = 'determinate')
                  my_progressbar.place(x=250,y=410)                 
                  for x in range(10):                    
                        my_progressbar['value'] +=10
                        l.update_idletasks()
                        time.sleep(1)
                        if x == 9:
                              l.destroy()
                              import student

      elif type_combobox.get()=='Admin':                     
            sql = "SELECT email FROM admins WHERE email='%s'"%email_entrybox.get()  
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if not myresult:
                  m_box.showerror(f'Error','You Entered Wrong Email')
            else:
                  my_progressbar = ttk.Progressbar(l, orient=HORIZONTAL,
                  length=400,mode = 'determinate')
                  my_progressbar.place(x=250,y=410)                 
                  for x in range(10):                    
                        my_progressbar['value'] +=10
                        l.update_idletasks()
                        time.sleep(1)
                        if x == 9:
                              l.destroy()
                              import admin
      else:
            m_box.showerror('Error','Select Your Type')


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