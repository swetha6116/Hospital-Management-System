from tkinter import *
from tkinter import messagebox
from subprocess import call
import tkinter
import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=(LocalDb)\MSSQLLocalDB;"
    "Database=HMS;"
    "Trusted_Connection=yes;"
)

window = Tk()

window.geometry("1280x720")
window.title("HMS LOGIN")
window.iconbitmap("C:/Users/thans/Desktop/TRIAL/hospital.ico")
window.configure(bg = "#666d84")
canvas = Canvas(
    window,
    bg = "#666d84",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

#TEMP
class Callpy(object):
    
    def __init__(self,path):
        self.path = path

    def CallFile(self):
        call(["Python3","{}".format(self.path)])

input1 = tkinter.StringVar()
input2 = tkinter.StringVar()
input3 = tkinter.StringVar()

def submit():
    username = input1.get()
    password = input2.get()
    designation = input3.get()

    c = conn.cursor()
    c.execute("Select password from PassData where username = (?)",(username))
    for i in c:
        if(i[0] == password):
            d = conn.cursor()
            d.execute("Select designation from PassData where username = (?)",(username))
            for j in d:
                if(j[0] == designation):
                    if designation == "Admin":
                        window.destroy()
                        caller = Callpy("C:/Users/thans/Desktop/TRIAL/ADMIN.py")
                        caller.CallFile()
                    elif designation == "Doctor":
                        window.destroy()
                        caller = Callpy("C:/Users/thans/Desktop/TRIAL/DOCTOR.py")
                        caller.CallFile()
                    elif designation == "Receptionist":
                        window.destroy()
                        caller = Callpy("C:/Users/thans/Desktop/TRIAL/RECEPTIONIST.py")
                        caller.CallFile()
                else:
                    messagebox.showwarning("Warning","Invalid designation")
        else:
            messagebox.showwarning("Warning","Invalid password or username")

    conn.commit()

def close():
    window.destroy()

background_img = PhotoImage(file = f"background0.png")
background = canvas.create_image(
    631.0, 284.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = close,
    relief = "flat")

b0.place(
    x = 727, y = 573,
    width = 63,
    height = 20)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = submit,
    relief = "flat")

b1.place(
    x = 490, y = 519,
    width = 300,
    height = 45)

entry0 = Entry(
    bd = 0,
    bg = "#666d84",
    font=("Montserrat",14),
    fg = "#ffffff",
    textvariable=input1,
    highlightthickness = 0)

entry0.place(
    x = 527, y = 296,
    width = 260,
    height = 35)

entry1 = Entry(
    bd = 0,
    bg = "#666d84",
    font=("Montserrat",14),
    fg = "#ffffff",
    show="*",
    textvariable=input2,
    highlightthickness = 0)

entry1.place(
    x = 527, y = 370,
    width = 260,
    height = 35)

entry2 = Entry(
    bd = 0,
    bg = "#666d84",
    font=("Montserrat",14),
    fg = "#ffffff",
    textvariable=input3,
    highlightthickness = 0)

entry2.place(
    x = 527, y = 443,
    width = 260,
    height = 35)

window.resizable(False, False)
window.mainloop()