import tkinter
from tkinter import *
from subprocess import call
import pyodbc
from tkinter import ttk

# conn = pyodbc.connect(
#     "Driver={SQL Server Native Client 11.0};"
#     "Server=(LocalDb)\MSSQLLocalDB;"
#     "Database=HMS;"
#     "Trusted_Connection=yes;"
# )

window = Tk()

window.geometry("1280x720")
window.iconbitmap("C:/Users/thans/Desktop/TRIAL/hospital.ico")
window.title("ADMIN")
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

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background="silver",foreground="black",rowheight=25,fieldbackground="#D3D3D3")
style.map('Treeview',background=[('selected','#BB4C4C')])

class Callpy(object):
    
    def __init__(self,path):
        self.path = path

    def CallFile(self):
        call(["Python3","{}".format(self.path)])

def close():
    window.destroy()

def btn_back():
    window.destroy()
    caller = Callpy("C:/Users/thans/Desktop/TRIAL/LOGIN.py")
    caller.CallFile()

tree = ttk.Treeview(window)
tree['columns'] = ("UserName","Password","Designation")

#column format
tree.column("#0",width = 0,stretch=NO)
tree.column("UserName",anchor=W,width = 80,minwidth=25)
tree.column("Password",anchor=W,width = 120,minwidth=25)
tree.column("Designation",anchor=W,width = 60,minwidth=25)

#headings
tree.heading("#0",text="",anchor=W)
tree.heading("UserName",text="UserName",anchor=W)
tree.heading("Password",text="Password",anchor=W)
tree.heading("Designation",text="Designation",anchor=W)
tree.place(x=374,y=90,width=530,height=315)

cursor = conn.cursor()
count=0
for i in cursor.execute("select * from PassData"):

    tree.insert(parent='',index='end',iid= count ,text="parent",values=(i[0],i[1],i[2]))
    count +=1
conn.commit()

background_img = PhotoImage(file = f"bgadmin.png")
background = canvas.create_image(
    583.5, 217.0,
    image=background_img)

img0 = PhotoImage(file = f"img9.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = close,
    relief = "flat")

b0.place(
    x = 673, y = 482,
    width = 78,
    height = 24)

img1 = PhotoImage(file = f"img12.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_back,
    relief = "flat")

b1.place(
    x = 528, y = 482,
    width = 78,
    height = 24)

window.resizable(False, False)
window.mainloop()
