from os import pardir
from tkinter import *
import tkinter as tk
from tkinter import ttk
from subprocess import PIPE, call
from tkinter import messagebox
from tkinter.messagebox import askyesno
import pyodbc
import tkinter

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=(LocalDb)\MSSQLLocalDB;"
    "Database=HMS;"
    "Trusted_Connection=yes;"
)

class Callpy(object):
    
    def __init__(self,path):
        self.path = path

    def CallFile(self):
        call(["Python3","{}".format(self.path)])

def btn_back():
    root.destroy()
    caller = Callpy("C:/Users/thans/Desktop/TRIAL/LOGIN.py")
    caller.CallFile()

def btn_clear():
    entry0.delete(0,END)
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)

def close():
    root.destroy()

#Main window
root = tk.Tk()
root.geometry("1280x720")
root.title("RECEPTIONIST")
root.iconbitmap("C:/Users/thans/Desktop/TRIAL/hospital.ico")

#Creating Structure for Tabs
notebook = ttk.Notebook(root)
notebook.pack()

tab1=Frame(notebook,bg = "#666d84",width=1280,height=720)
tab2=Frame(notebook,bg = "#666d84",width=1280,height=720)
tab3=Frame(notebook,bg = "#666d84",width=1280,height=720)
tab4=Frame(notebook,bg = "#666d84",width=1280,height=720)

tab1.pack(fill="both",expand=1)
tab2.pack(fill="both",expand=1)
tab3.pack(fill="both",expand=1)
tab4.pack(fill="both",expand=1)

#Adding Tabs
notebook.add(tab1,text="ADD PATIENTS")
notebook.add(tab2,text="UPDATE PATIENTS")
notebook.add(tab3,text="DISPLAY PATIENTS")
notebook.add(tab4,text="ENQUIRY")

#INSERT
canvas1 = Canvas(
    tab1,
    bg = "#666d84",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas1.place(x = 0, y = 0)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background="silver",foreground="black",rowheight=25,fieldbackground="#D3D3D3")
style.map('Treeview',background=[('selected','#BB4C4C')])

#Table1
tree1 = ttk.Treeview(tab1)
tree1['columns'] = ("Doctor_ID","Doctor_Name","Department")

#column format
tree1.column("#0",width = 0,stretch=NO)
tree1.column("Doctor_ID",anchor=W,width = 80,minwidth=80)
tree1.column("Doctor_Name",anchor=W,width = 120,minwidth=120)
tree1.column("Department",anchor=W,width = 60,minwidth=80)

#headings
tree1.heading("#0",text="",anchor=W)
tree1.heading("Doctor_ID",text="Doctor_ID",anchor=W)
tree1.heading("Doctor_Name",text="Doctor_Name",anchor=CENTER)
tree1.heading("Department",text="Department",anchor=W)
tree1.place(x=711,y=110,width=450,height=180)

cursor = conn.cursor()
count=0
for i in cursor.execute("select * from DoctorTable"):

    tree1.insert(parent='',index='end',iid= count ,text="parent",values=(i[0],i[1],i[2]))
    count +=1
conn.commit()


#Table 2
tree2 = ttk.Treeview(tab1)
tree2['columns'] = ("Patient_ID","Patient_Name","Doctor_ID")

#column format
tree2.column("#0",width = 0,stretch=NO)
tree2.column("Patient_ID",anchor=W,width = 80,minwidth=80)
tree2.column("Patient_Name",anchor=W,width = 120,minwidth=120)
tree2.column("Doctor_ID",anchor=W,width = 60,minwidth=80)

#headings
tree2.heading("#0",text="",anchor=W)
tree2.heading("Patient_ID",text="Patient_ID",anchor=W)
tree2.heading("Patient_Name",text="Patient_Name",anchor=CENTER)
tree2.heading("Doctor_ID",text="Doctor_ID",anchor=W)
tree2.place(x=711,y=310,width=450,height=180)

cursor = conn.cursor()
count=0
for i in cursor.execute("select Patient_ID,Patient_Name,Doctor_ID from Patients_Table"):
    tree2.insert(parent='',index='end',iid= count ,text="parent",values=(i[0],i[1],i[2]))
    count +=1
conn.commit()

def btn_insert():
    answer = askyesno(title='confirmation',message='Are you sure that you want to ADD?')
    if answer:
        Pname1 = input6.get()
        dob1 = input5.get()
        age1 = input4.get()
        sex1 = input3.get()
        phno1 = input2.get()
        DID1 = input1.get()
        cursor = conn.cursor()
        cursor.execute(
            "Insert into Patients_Table(Patient_Name,DOB,Age,Sex,Phone_Number,Doctor_ID) values (?,?,?,?,?,?);", (Pname1, dob1, age1,sex1,phno1,DID1))
        conn.commit()
        entry0.delete(0,END)
        entry1.delete(0,END)
        entry2.delete(0,END)
        cursor.close()
        root.destroy()
        caller = Callpy("C:/Users/thans/Desktop/TRIAL/RECEPTIONIST.py")
        caller.CallFile()


input1 = tkinter.IntVar()
input2 = tkinter.IntVar()
input3 = tkinter.StringVar()
input4 = tkinter.IntVar()
input5 = tkinter.StringVar()
input6 = tkinter.StringVar()

background_img = PhotoImage(file = f"bginsert.png")
background = canvas1.create_image(
    348.5, 289.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox1.png")
entry0_bg = canvas1.create_image(
    445.0, 372.0,
    image = entry0_img)

entry0 = Entry(
    tab1,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input1,
    highlightthickness = 0)

entry0.place(
    x = 325, y = 355,
    width = 240,
    height = 32)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas1.create_image(
    445.0, 322.0,
    image = entry1_img)

entry1 = Entry(
    tab1,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input2,
    highlightthickness = 0)

entry1.place(
    x = 325, y = 305,
    width = 240,
    height = 32)

entry2_img = PhotoImage(file = f"img_textBox1.png")
entry2_bg = canvas1.create_image(
    445.0, 272.0,
    image = entry2_img)

entry2 = Entry(
    tab1,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input3,
    highlightthickness = 0)

entry2.place(
    x = 325, y = 255,
    width = 240,
    height = 32)

entry3_img = PhotoImage(file = f"img_textBox1.png")
entry3_bg = canvas1.create_image(
    445.0, 222.0,
    image = entry3_img)

entry3 = Entry(
    tab1,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input4,
    highlightthickness = 0)

entry3.place(
    x = 325, y = 205,
    width = 240,
    height = 32)

entry4_img = PhotoImage(file = f"img_textBox1.png")
entry4_bg = canvas1.create_image(
    445.0, 172.0,
    image = entry4_img)

entry4 = Entry(
    tab1,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input5,
    highlightthickness = 0)

entry4.place(
    x = 325, y = 155,
    width = 240,
    height = 32)

entry5_img = PhotoImage(file = f"img_textBox1.png")
entry5_bg = canvas1.create_image(
    445.0, 122.0,
    image = entry5_img)

entry5 = Entry(
    tab1,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input6,
    highlightthickness = 0)

entry5.place(
    x = 325, y = 105,
    width = 240,
    height = 32)

img0 = PhotoImage(file = f"img9.png")
b0 = Button(
    tab1,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = close,
    relief = "flat")

b0.place(
    x = 500, y = 454,
    width = 78,
    height = 24)

img1 = PhotoImage(file = f"img10.png")
b1 = Button(
    tab1,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clear,
    relief = "flat")

b1.place(
    x = 370, y = 454,
    width = 78,
    height = 24)

img2 = PhotoImage(file = f"img11.png")
b2 = Button(
    tab1,
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_insert,
    relief = "flat")

b2.place(
    x = 240, y = 454,
    width = 78,
    height = 24)

img3 = PhotoImage(file = f"img12.png")
b3 = Button(
    tab1,
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_back,
    relief = "flat")

b3.place(
    x = 130, y = 454,
    width = 78,
    height = 24)

btn_clear()

#UPDATE
canvas2 = Canvas(
    tab2,
    bg = "#666d84",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas2.place(x = 0, y = 0)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background="silver",foreground="black",rowheight=25,fieldbackground="#D3D3D3")
style.map('Treeview',background=[('selected','#BB4C4C')])

#Table3
tree3 = ttk.Treeview(tab2)
tree3['columns'] = ("Patient ID","Patient Name","Date of Birth","Age","Sex","Phone Number","Doctor ID")

#column format
tree3.column("#0",width = 0,stretch=NO)
tree3.column("Patient ID",anchor=W,width = 60,minwidth=60)
tree3.column("Patient Name",anchor=W,width = 120,minwidth=120)
tree3.column("Date of Birth",anchor=CENTER,width = 100,minwidth=80)
tree3.column("Age",anchor=CENTER,width = 20,minwidth=20)
tree3.column("Sex",anchor=CENTER,width = 20,minwidth=20)
tree3.column("Phone Number",anchor=CENTER,width = 100,minwidth=80)
tree3.column("Doctor ID",anchor=W,width = 60,minwidth=60)

#headings
tree3.heading("#0",text="",anchor=W)
tree3.heading("Patient ID",text="Patient ID",anchor=W)
tree3.heading("Patient Name",text="Patient Name",anchor=CENTER)
tree3.heading("Date of Birth",text="Date of Birth",anchor=CENTER)
tree3.heading("Age",text="Age",anchor=CENTER)
tree3.heading("Sex",text="Sex",anchor=CENTER)
tree3.heading("Phone Number",text="Phone Number",anchor=CENTER)
tree3.heading("Doctor ID",text="Doctor ID",anchor=W)
tree3.place(x=617,y=56,width=629,height=523)

x = conn.cursor()
count=0
for i in x.execute("select * from Patients_Table"):
    tree3.insert(parent='',index='end',iid= count ,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    count +=1

conn.commit()
x.close()

input111 = tkinter.IntVar()
input211 = tkinter.IntVar()
input311 = tkinter.StringVar()
input411 = tkinter.IntVar()
input511 = tkinter.StringVar()
input611 = tkinter.StringVar()
input711 = tkinter.IntVar()

def btn_clear():
    entry01.delete(0,END)
    entry11.delete(0,END)
    entry21.delete(0,END)
    entry31.delete(0,END)
    entry41.delete(0,END)
    entry51.delete(0,END)
    entry61.delete(0,END)

def btn_refresh():
    root.destroy()
    caller = Callpy("C:/Users/thans/Desktop/TRIAL/RECEPTIONIST.py")
    caller.CallFile()

def btn_update():
    answer = askyesno(title='confirmation',message='Are you sure that you want to Update?')
    if answer:
        ppidd = input711.get()
        pname = input611.get()
        pdob = input511.get()
        page = input411.get()
        psex = input311.get()
        pphno = input211.get()
        pdid = input111.get()
        cursor = conn.cursor()
        cursor.execute("UPDATE Patients_Table SET Patient_Name = (?),DOB = (?),Age = (?),Sex = (?),Phone_Number = (?),Doctor_ID = (?) WHERE Patient_ID = (?)",(pname,pdob,page,psex,pphno,pdid,ppidd))
        conn.commit()
        conn.close()
        root.destroy()
        caller = Callpy("C:/Users/thans/Desktop/TRIAL/RECEPTIONIST.py")
        caller.CallFile()


def btn_select():
    selected = tree3.focus()
    values = tree3.item(selected, 'values')
    entry61.insert(0,values[0])
    entry51.insert(0,values[1])
    entry41.insert(0,values[2])
    entry31.insert(0,values[3])
    entry21.insert(0,values[4])
    entry11.insert(0,values[5])
    entry01.insert(0,values[6])




background_img1 = PhotoImage(file = f"bgupdate.png")
background1 = canvas2.create_image(
    325.0, 317.5,
    image=background_img1)

entry0_img1 = PhotoImage(file = f"img_textBox3.png")
entry0_bg1 = canvas2.create_image(
    424.0, 423.0,
    image = entry0_img1)

entry01 = Entry(
    tab2,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input111,
    highlightthickness = 0)

entry01.place(
    x = 304, y = 406,
    width = 240,
    height = 32)

entry1_img1 = PhotoImage(file = f"img_textBox3.png")
entry1_bg1 = canvas2.create_image(
    424.0, 373.0,
    image = entry1_img1)

entry11 = Entry(
    tab2,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input211,
    highlightthickness = 0)

entry11.place(
    x = 304, y = 356,
    width = 240,
    height = 32)

entry2_img1 = PhotoImage(file = f"img_textBox3.png")
entry2_bg1 = canvas2.create_image(
    424.0, 323.0,
    image = entry2_img1)

entry21 = Entry(
    tab2,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input311,
    highlightthickness = 0)

entry21.place(
    x = 304, y = 306,
    width = 240,
    height = 32)

entry3_img1 = PhotoImage(file = f"img_textBox3.png")
entry3_bg1 = canvas2.create_image(
    424.0, 273.0,
    image = entry3_img1)

entry31 = Entry(
    tab2,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input411,
    highlightthickness = 0)

entry31.place(
    x = 304, y = 256,
    width = 240,
    height = 32)

entry4_img1 = PhotoImage(file = f"img_textBox3.png")
entry4_bg1 = canvas2.create_image(
    424.0, 223.0,
    image = entry4_img1)

entry41 = Entry(
    tab2,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input511,
    highlightthickness = 0)

entry41.place(
    x = 304, y = 206,
    width = 240,
    height = 32)

entry5_img1 = PhotoImage(file = f"img_textBox3.png")
entry5_bg1 = canvas2.create_image(
    424.0, 173.0,
    image = entry5_img1)

entry51 = Entry(
    tab2,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input611,
    highlightthickness = 0)

entry51.place(
    x = 304, y = 156,
    width = 240,
    height = 32)

entry6_img1 = PhotoImage(file = f"img_textBox3.png")
entry6_bg1 = canvas2.create_image(
    424.0, 123.0,
    image = entry6_img1)

entry61 = Entry(
    tab2,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input711,
    highlightthickness = 0)

entry61.place(
    x = 304, y = 106,
    width = 240,
    height = 32)

img01 = PhotoImage(file = f"img9.png")
b01 = Button(
    tab2,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = close,
    relief = "flat")

b01.place(
    x = 461, y = 500,
    width = 78,
    height = 24)

img11 = PhotoImage(file = f"img10.png")
b11 = Button(
    tab2,
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clear,
    relief = "flat")

b11.place(
    x = 331, y = 500,
    width = 78,
    height = 24)

img21 = PhotoImage(file = f"img13.png")
b21 = Button(
    tab2,
    image = img21,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_update,
    relief = "flat")

b21.place(
    x = 201, y = 500,
    width = 78,
    height = 24)

img31 = PhotoImage(file = f"img12.png")
b31 = Button(
    tab2,
    image = img31,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_back,
    relief = "flat")

b31.place(
    x = 91, y = 500,
    width = 78,
    height = 24)

img1190 = PhotoImage(file = f"img15.png")
b119 = Button(
    tab2,
    image = img1190,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_refresh,
    relief = "flat")

b119.place(
    x = 331, y = 600,
    width = 78,
    height = 24)

img2190 = PhotoImage(file = f"img11.png")
b219 = Button(
    tab2,
    image = img2190,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_select,
    relief = "flat")

b219.place(
    x = 201, y = 600,
    width = 78,
    height = 24)

btn_clear()

#DISPLAY(VIEW/DELETE)

canvas3 = Canvas(
    tab3,
    bg = "#666d84",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas3.place(x = 0, y = 0)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background="silver",foreground="black",rowheight=25,fieldbackground="#D3D3D3")
style.map('Treeview',background=[('selected','#BB4C4C')])

#Table5
tree4 = ttk.Treeview(tab3)
tree4['columns'] = ("Patient ID","Patient Name","Date of Birth","Age","Sex","Phone Number","Doctor ID")

#column format
tree4.column("#0",width = 0,stretch=NO)
tree4.column("Patient ID",anchor=W,width = 40,minwidth=40)
tree4.column("Patient Name",anchor=W,width = 120,minwidth=120)
tree4.column("Date of Birth",anchor=W,width = 60,minwidth=80)
tree4.column("Age",anchor=CENTER,width = 20,minwidth=20)
tree4.column("Sex",anchor=CENTER,width = 20,minwidth=20)
tree4.column("Phone Number",anchor=CENTER,width = 60,minwidth=80)
tree4.column("Doctor ID",anchor=W,width = 80,minwidth=80)

#headings
tree4.heading("#0",text="",anchor=W)
tree4.heading("Patient ID",text="Patient ID",anchor=W)
tree4.heading("Patient Name",text="Patient Name",anchor=CENTER)
tree4.heading("Date of Birth",text="Date of Birth",anchor=W)
tree4.heading("Age",text="Age",anchor=CENTER)
tree4.heading("Sex",text="Sex",anchor=CENTER)
tree4.heading("Phone Number",text="Phone Number",anchor=CENTER)
tree4.heading("Doctor ID",text="Doctor ID",anchor=W)
tree4.place(x=96,y=73,width=1088,height=417)
x = conn.cursor()
count=0
for i in x.execute("select * from Patients_Table"):
    tree4.insert(parent='',index='end',iid= count ,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    count +=1

conn.commit()
x.close()

input131 = tkinter.IntVar()

def btn_clear():
    entry02.delete(0,END)

def btn_select():
    selected = tree4.focus()
    arr = tree4.item(selected, 'values')
    print(arr)
    entry02.insert(0,arr[0])


def btn_delete():
    answer = askyesno(title='confirmation',message='Are you sure that you want to Delete?\n\nChanges Made Are permanent!')
    if answer:
        x = tree4.selection()[0]
        selected =tree4.focus()
        arr = tree4.item(selected,'values')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Patients_Table where Patient_ID = (?);",(arr[0]))
        conn.commit()
        tree4.delete(x)
        root.destroy()
        caller = Callpy("C:/Users/thans/Desktop/TRIAL/RECEPTIONIST.py")
        caller.CallFile()

background_img2 = PhotoImage(file = f"bgdisplay.png")
background2 = canvas3.create_image(
    608.0, 290.0,
    image=background_img2)

img02 = PhotoImage(file = f"img9.png")
b02 = Button(
    tab3,
    image = img02,
    borderwidth = 0,
    highlightthickness = 0,
    command = close,
    relief = "flat")

b02.place(
    x = 786, y = 616,
    width = 78,
    height = 24)

img092 = PhotoImage(file = f"img11.png")
b092 = Button(
    tab3,
    image = img092,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_select,
    relief = "flat")

b092.place(
    x = 910, y = 616,
    width = 78,
    height = 24)

img12 = PhotoImage(file = f"img10.png")
b12 = Button(
    tab3,
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clear,
    relief = "flat")

b12.place(
    x = 656, y = 616,
    width = 78,
    height = 24)

img22 = PhotoImage(file = f"img14.png")
b22 = Button(
    tab3,
    image = img22,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_delete,
    relief = "flat")

b22.place(
    x = 526, y = 616,
    width = 78,
    height = 24)

img32 = PhotoImage(file = f"img12.png")
b32 = Button(
    tab3,
    image = img32,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_back,
    relief = "flat")

b32.place(
    x = 416, y = 616,
    width = 78,
    height = 24)

entry0_img2 = PhotoImage(file = f"img_textBox4.png")
entry0_bg2 = canvas3.create_image(
    724.0, 550.0,
    image = entry0_img2)

entry02 = Entry(
    tab3,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input131,
    highlightthickness = 0)

entry02.place(
    x = 604, y = 533,
    width = 240,
    height = 32)

btn_clear()
#ENQUIRY
canvas4 = Canvas(
    tab4,
    bg = "#666d84",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas4.place(x = 0, y = 0)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background="silver",foreground="black",rowheight=25,fieldbackground="#D3D3D3")
style.map('Treeview',background=[('selected','#BB4C4C')])

#Table5
tree5 = ttk.Treeview(tab4)
tree5['columns'] = ("Patient ID","Patient Name","Date of Birth","Age","Sex","Phone Number","Doctor ID")

#column format
tree5.column("#0",width = 0,stretch=NO)
tree5.column("Patient ID",anchor=W,width = 40,minwidth=40)
tree5.column("Patient Name",anchor=W,width = 120,minwidth=120)
tree5.column("Date of Birth",anchor=W,width = 60,minwidth=80)
tree5.column("Age",anchor=CENTER,width = 20,minwidth=20)
tree5.column("Sex",anchor=CENTER,width = 20,minwidth=20)
tree5.column("Phone Number",anchor=CENTER,width = 60,minwidth=80)
tree5.column("Doctor ID",anchor=W,width = 80,minwidth=80)

#headings
tree5.heading("#0",text="",anchor=W)
tree5.heading("Patient ID",text="Patient ID",anchor=W)
tree5.heading("Patient Name",text="Patient Name",anchor=CENTER)
tree5.heading("Date of Birth",text="Date of Birth",anchor=W)
tree5.heading("Age",text="Age",anchor=CENTER)
tree5.heading("Sex",text="Sex",anchor=CENTER)
tree5.heading("Phone Number",text="Phone Number",anchor=CENTER)
tree5.heading("Doctor ID",text="Doctor ID",anchor=W)
tree5.place(x=156,y=256,width=968,height=227)

def btn_view():
    pid141 = input141.get()
    x = conn.cursor()
    for i in x.execute("select * from Patients_Table where Patient_Name = (?)",(pid141)):
        if i[0] == None:
            messagebox.showinfo("ERROR","Invalid Input or Patient Doesn't exist")
        tree5.insert(parent='',index='end',iid= i ,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    conn.commit()
    x.close()
    
input141 = tkinter.StringVar()

background_img3 = PhotoImage(file = f"bgname.png")
background3 = canvas4.create_image(
    640.0, 344.5,
    image=background_img3)

entry0_img3 = PhotoImage(file = f"img_textBox0.png")
entry0_bg3 = canvas4.create_image(
    726.0, 95.0,
    image = entry0_img3)

entry03 = Entry(
    tab4,
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input141,
    highlightthickness = 0)

entry03.place(
    x = 606, y = 78,
    width = 240,
    height = 32)

img03 = PhotoImage(file = f"img9.png")
b03 = Button(
    tab4,
    image = img03,
    borderwidth = 0,
    highlightthickness = 0,
    command = close,
    relief = "flat")

b03.place(
    x = 721, y = 149,
    width = 78,
    height = 24)

img13 = PhotoImage(file = f"img7.png")
b13 = Button(
    tab4,
    image = img13,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_view,
    relief = "flat")
 
b13.place(
    x = 601, y = 149,
    width = 78,
    height = 24)

img23 = PhotoImage(file = f"img6.png")
b23 = Button(
    tab4,
    image = img23,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_back,
    relief = "flat")

b23.place(
    x = 481, y = 149,
    width = 78,
    height = 24)
root.mainloop()