from tkinter import *
from tkinter import ttk
import time

from PIL import ImageTk, Image
from tkinter import ttk


root = Tk()

root.title("ProgressBar")
root.geometry("1199x600+100+50")

img = ImageTk.PhotoImage(Image.open("images\\mg22.jpg"))
panel = Label(root, image = img)
panel.place(x = 0,y = 0)

lbl3 =Label(root,text="Select Your Type   ",font=("Goudy old style ",15),fg = "#0D0B0B",bg="gray").place(x=500,y=250)

type_combobox = ttk.Combobox(root,width = 13, state = 'readonly')
type_combobox['values'] = ('Teacher','Student','Admin')
type_combobox.place(x=500,y=290,width=195,height=35)
type_combobox.current(0)

def start():

    if type_combobox.get()=='Student':        
        my_progressbar = ttk.Progressbar(root, orient=HORIZONTAL,
        length=400,mode = 'determinate')
        my_progressbar.place(x=420,y=390)       
        for x in range(10):
                    
            my_progressbar['value'] +=10
            root.update_idletasks()
            time.sleep(1)
            if x == 9:               
                root.destroy()
                import student
    elif type_combobox.get()=='Teacher':
        my_progressbar = ttk.Progressbar(root, orient=HORIZONTAL,
        length=400,mode = 'determinate')
        my_progressbar.place(x=420,y=390)       
        for x in range(10):                   
            my_progressbar['value'] +=10
            root.update_idletasks()
            time.sleep(1)
            if x == 9:
                root.destroy()
                import teacher

    elif type_combobox.get()=='Admin':
        my_progressbar = ttk.Progressbar(root, orient=HORIZONTAL,
        length=400,mode = 'determinate')
        my_progressbar.place(x=420,y=390)       
        for x in range(10):                   
            my_progressbar['value'] +=10
            root.update_idletasks()
            time.sleep(1)
            if x == 9:
                root.destroy()
                import admin
    else:
        print("Typ---")   

my_button2 = ttk.Button(root,text="Start App",command=start)
my_button2.place(x=500,y=350,width=190,height=35)

root.mainloop()