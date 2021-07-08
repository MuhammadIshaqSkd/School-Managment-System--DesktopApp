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


#_______Creating Window_________

win = Tk()
win.geometry("1199x600+100+50")
win.resizable(False,False)

img = ImageTk.PhotoImage(Image.open("images\\signup.png"))
panel = Label(win, image = img)
panel.place(x = 0,y = 0)


signup_frame = Frame(win, bg ="white")
signup_frame.place(x=300,y=40,height=500,width=550)

dsc =Label(signup_frame,text="\t\tRegistration From",font=("Goudy old style ",15,"bold"),fg = "#0D0B0B",bg="white").place(x=30,y=10)


#-------Set Title---------

win.title('GUI')


lbl1 =Label(signup_frame,text="Enter Your Name",font=("Goudy old style ",10,"bold"),fg = "#0D0B0B",bg="white").place(x=70,y=60)

name_var = tk.StringVar()
name_entrybox =Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable = name_var)
name_entrybox.place(x=210,y=60,width=200,height=35)
name_entrybox.focus()

email_var = tk.StringVar()
lbl2 =Label(signup_frame,text="Enter Your Email",font=("Goudy old style ",10,"bold"),fg = "#0D0B0B",bg="white").place(x=70,y=105)
email_entrybox =Entry(signup_frame,font=("times new roman",15),bg="lightgray", textvariable = email_var)
email_entrybox.place(x=210,y=100,width=200,height=35)

lbl3 =Label(signup_frame,text="Enter Your Age",font=("Goudy old style ",10,"bold"),fg = "#0D0B0B",bg="white").place(x=70,y=147)
age_var = tk.StringVar()
age_entrybox =Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable = age_var)
age_entrybox.place(x=210,y=140,width=200,height=35)

lbl4 =Label(signup_frame,text="Select Your Gender",font=("Goudy old style ",10,"bold"),fg = "#0D0B0B",bg="white").place(x=60,y=190)

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(signup_frame,width = 13, textvariable = gender_var, state = 'readonly')
gender_combobox['values'] = ('Male','Femal','Other')
gender_combobox.place(x=210,y=190,width=195,height=35)
gender_combobox.current(0)

lbl6 =Label(signup_frame,text="Your Departnment",font=("Goudy old style ",10,"bold"),fg = "#0D0B0B",bg="white").place(x=60,y=290)
dept_entrybox =Entry(signup_frame,font=("times new roman",15),bg="lightgray")
dept_entrybox.place(x=210,y=290,width=200,height=35)

lbl7 =Label(signup_frame,text="Enter Password ",font=("Goudy old style ",10,"bold"),fg = "#0D0B0B",bg="white").place(x=60,y=350)
pas_entrybox =Entry(signup_frame,font=("times new roman",15),bg="red")
pas_entrybox.place(x=210,y=350,width=200,height=35)
checkbtn_var = tk.IntVar()

checkbtn = ttk.Checkbutton(signup_frame, text= 'Are You Regular ?',variable = checkbtn_var)
checkbtn.place(x=120,y=400,width=300,height=35)



def action():

    username = name_var.get()
    userage = age_var.get()
    useremail = email_var.get()
    user_gender = gender_var.get()
    userdep=  dept_entrybox.get()
    passs = pas_entrybox.get()

    if email_entrybox.get() == '':
        m_box.showerror('Error','Please Enter Your Email')
    if pas_entrybox.get() == '':
        m_box.showerror('Error','Please Enter Your Password')

    if username == ''or type(username)!=str:
        m_box.showerror('School','Please Enter Your Name')
    elif userage == '':
        m_box.showerror('School','Please Enter Your Age')

    elif user_gender == '':
        m_box.showerror('School','Please Select Your Gender')

    try:
        userage = int(userage)
    except ValueError:
        m_box.showerror('Error','Please Enter Your Age in Numbers')

    if userage > 100:
        m_box.showerror('Error', 'The age is Over')

    

    else:

        if checkbtn_var.get() == 0:
                subcribe = 'No'
        else:
            subcribe = 'Yes'

        sql = "SELECT email FROM student WHERE email='%s'"%email_var.get()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if not myresult:
            sql = "INSERT INTO teacher (name, age,email,gender,Department,regular,pass) VALUES (%s,%s, %s,%s,%s,%s,%s)"
            val =  (username,userage, useremail,user_gender,userdep,subcribe,passs)
                
            mycursor.execute(sql, val)
            mydb.commit()
                
            name_entrybox.delete(0,tk.END)
            email_entrybox.delete(0, tk.END)
            age_entrybox.delete(0, tk.END)
            dept_entrybox.delete(0, tk.END)
        else:
            m_box.showerror('Error','This Record is already exist in Student ')              

def exits():

    
    win.destroy()
    import admin
   


#---------Button 1--------------

ttk.Style().configure("TButton", padding=6, relief="flat",background="#d25d17")

l_btn1 = ttk.Button(win,text = "Submite",command = action)
l_btn1.place(x=600,y=520,width=190,height=35)

l_btn2 = ttk.Button(win,text = "Back to Admin Pannel",command = exits)
l_btn2.place(x=360,y=520,width=190,height=35)

win.mainloop()
