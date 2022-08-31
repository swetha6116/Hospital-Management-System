from tkinter import *
from subprocess import call
import tkinter
from typing import Counter
import pyodbc
from tkinter import ttk
from tkinter.messagebox import askyesno

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=(LocalDb)\MSSQLLocalDB;"
    "Database=HMS;"
    "Trusted_Connection=yes;"
)

window = Tk()

window.geometry("1280x720")
window.iconbitmap("C:/Users/thans/Desktop/TRIAL/hospital.ico")
window.title("DOCTOR")
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

#Table1
tree1 = ttk.Treeview(window)
tree1['columns'] = ("Doctor_ID","Doctor_Name","Department","Patient_ID","Disease","Treatment")

#column format
tree1.column("#0",width = 0)
tree1.column("Doctor_ID",anchor=W,width = 40,minwidth=40)
tree1.column("Doctor_Name",anchor=W,width = 100,minwidth=100)
tree1.column("Department",anchor=W,width = 100,minwidth=100)
tree1.column("Patient_ID",anchor=CENTER,width = 40,minwidth=40)
tree1.column("Disease",anchor=CENTER,width = 120,minwidth=120)
tree1.column("Treatment",anchor=CENTER,width = 120,minwidth=120)

#headings
tree1.heading("#0",text="",anchor=W)
tree1.heading("Doctor_ID",text="Doctor_ID",anchor=W)
tree1.heading("Doctor_Name",text="Doctor_Name",anchor=W)
tree1.heading("Department",text="Department",anchor=W)
tree1.heading("Patient_ID",text="Patient_ID",anchor=CENTER)
tree1.heading("Disease",text="Disease",anchor=CENTER)
tree1.heading("Treatment",text="Treatment",anchor=CENTER)
tree1.place(x=532,y=65,width=697,height=378)

#Parent
x = conn.cursor()
count=0
for i in x.execute("select * from DoctorTable"):
    tree1.insert(parent='',index='end',iid= count ,text="",values=(i[0],i[1],i[2]))
    count +=1
conn.commit()
x.close()

#Child

l1=l2=l3=l4=l5=[]

#Doctor 1
y1 = conn.cursor()
y1.execute("select * from TreatmentTable where Patient_ID in(select Patient_ID from Patients_Table where Doctor_ID =100)")
for i in y1:
    l1.append(i)
if len(l1)>0:
    count1 = 0
    itr = 100
    for j in range(len(l1)):
        tree1.insert(parent='0',index='end',iid=itr,text='',values=("","","",l1[j][0],l1[j][1],l1[j][2]))
        itr +=1
        count1 +=1

y1.close()

#Doctor 2
y2 = conn.cursor()
y2.execute("select * from TreatmentTable where Patient_ID in(select Patient_ID from Patients_Table where Doctor_ID =101)")
for i in y2:
    l2.append(i)
if len(l2)>0:
    count2 = 0
    itr = 200
    for j in range(len(l2)):
        tree1.insert(parent='1',index='end',iid=itr,text='',values=("","","",l2[j][0],l2[j][1],l2[j][2]))
        itr +=1
        count2 +=1
for k in range(count1):
    tree1.delete(k+200)

y2.close()

#Doctor 3
y3 = conn.cursor()
y3.execute("select * from TreatmentTable where Patient_ID in(select Patient_ID from Patients_Table where Doctor_ID =102)")
for i in y3:
    l3.append(i)
if len(l3)>0:
    count3 = 0
    itr = 300
    for j in range(len(l3)):
        tree1.insert(parent='2',index='end',iid=itr,text='',values=("","","",l3[j][0],l3[j][1],l3[j][2]))
        itr +=1
        count3 +=1

for k in range(count2):
    tree1.delete(k+300)

y3.close()

#Doctor 4
y4 = conn.cursor()
y4.execute("select * from TreatmentTable where Patient_ID in(select Patient_ID from Patients_Table where Doctor_ID =103)")
for i in y4:
    l4.append(i)
if len(l4)>0:
    count4 = 0
    itr = 400
    for j in range(len(l4)):
        tree1.insert(parent='3',index='end',iid=itr,text='',values=("","","",l4[j][0],l4[j][1],l4[j][2]))
        itr +=1
        count4 +=1

for k in range(count3):
    tree1.delete(k+400)

conn.commit()
y4.close()

#Doctor 5
y5 = conn.cursor()
y5.execute("select * from TreatmentTable where Patient_ID in(select Patient_ID from Patients_Table where Doctor_ID =104)")
for i in y5:
    l5.append(i)
if len(l5)>0:
    itr = 500
    for j in range(len(l5)):
        tree1.insert(parent='4',index='end',iid=itr,text='',values=("","","",l5[j][0],l5[j][1],l5[j][2]))
        itr +=1

for k in range(count4):
    tree1.delete(k+500)

conn.commit()
y5.close()


Tree7 = ttk.Treeview(window)
Tree7['columns'] = ("Patient_ID","Doctor_ID")

#select Patient_ID,Doctor_ID from Patients_Table where Patient_ID not in (select Patient_ID from TreatmentTable)

#column format
Tree7.column("#0",width = 0,stretch=NO)
Tree7.column("Patient_ID",anchor=CENTER,width = 80,minwidth=25)
Tree7.column("Doctor_ID",anchor=CENTER,width = 80,minwidth=25)
#headings
Tree7.heading("#0",text="",anchor=W)
Tree7.heading("Patient_ID",text="Patient_ID",anchor=CENTER)
Tree7.heading("Doctor_ID",text="Doctor_ID",anchor=CENTER)
Tree7.place(x=749,y=477,width=240,height=150)

cursor = conn.cursor()
count=0
for i in cursor.execute("select Patient_ID,Doctor_ID from Patients_Table where Patient_ID not in (select Patient_ID from TreatmentTable)"):

    Tree7.insert(parent='',index='end',iid= count ,text="parent",values=(i[0],i[1]))
    count +=1
conn.commit()
cursor.close()

class Callpy(object):
    
    def __init__(self,path):
        self.path = path

    def CallFile(self):
        call(["Python3","{}".format(self.path)])

def btn_clear():
    entry0.delete(0,END)
    entry1.delete(0,END)
    entry2.delete(0,END)
 
def btn_insert():
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to Insert?')
    if answer:
        patientId = input1.get()
        disease = input2.get()
        treatment = input3.get()
        cursor = conn.cursor()
        cursor.execute(
            "Insert into TreatmentTable(Patient_ID,Disease,Treatment) values (?,?,?);", (patientId, disease, treatment))
        conn.commit()
        entry0.delete(0,END)
        entry1.delete(0,END)
        entry2.delete(0,END)
        cursor.close()


def close():
    window.destroy()

def btn_refresh():
    window.destroy()
    caller = Callpy("C:/Users/thans/Desktop/TRIAL/DOCTOR.py")
    caller.CallFile()
    

def btn_back():
    window.destroy()
    caller = Callpy("C:/Users/thans/Desktop/TRIAL/LOGIN.py")
    caller.CallFile()

input1 = tkinter.StringVar()
input2 = tkinter.StringVar()
input3 = tkinter.StringVar()
#bgdoctor
background_img = PhotoImage(file = f"backgroundnew.png")
background = canvas.create_image(
    622.5, 229.0,
    image=background_img)

entry0 = Entry(
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input2,
    highlightthickness = 0)

entry0.place(
    x = 272, y = 172,
    width = 206,
    height = 32)

entry1 = Entry(
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input3,
    highlightthickness = 0)

entry1.place(
    x = 272, y = 221,
    width = 206,
    height = 32)

entry2 = Entry(
    bd = 3,
    font=("Montserrat",14),
    bg = "#c4c4c4",
    textvariable=input1,
    highlightthickness = 0)

entry2.place(
    x = 272, y = 123,
    width = 206,
    height = 32)

img0 = PhotoImage(file = f"img9.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = close,
    relief = "flat")

b0.place(
    x = 418, y = 360,
    width = 78,
    height = 24)

img1 = PhotoImage(file = f"img10.png")
b1 = Button(
    image = img1,
    borderwidth = 0, 
    highlightthickness = 0,
    command = btn_clear,
    relief = "flat")

b1.place(
    x = 288, y = 360,
    width = 78,
    height = 24)

img2 = PhotoImage(file = f"img11.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_insert,
    relief = "flat")

b2.place(
    x = 158, y = 360,
    width = 84,
    height = 24)

img3 = PhotoImage(file = f"img12.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_back,
    relief = "flat")

b3.place(
    x = 48, y = 360,
    width = 78,
    height = 24)
    
img4 = PhotoImage(file = f"img15.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_refresh,
    relief = "flat")

b4.place(
    x = 233, y = 435,
    width = 82,
    height = 24)

window.resizable(False, False)
window.mainloop()