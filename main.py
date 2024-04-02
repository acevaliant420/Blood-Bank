from tkinter import *
from tkinter import messagebox
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\College\2. Second Year\SEM 4\2. Labs\CS262 (DBMS Lab)\Project\Blood-Bank\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
import mysql.connector

passd = "user123!"

#Creating a Database
try:
    db = mysql.connector.connect(host="localhost", user="root", passwd=passd)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE blood_bank")
except:
    print("Following Database already exists.")

#Creating Tables
try:
    db = mysql.connector.connect(host="localhost", user="root", passwd=passd, database="blood_bank")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE DonorInfo(AadharNo CHAR(12) PRIMARY KEY, Name VARCHAR(20), BloodGroup VARCHAR(5), Amount INT)")
    cursor.execute("CREATE TABLE PatientsInfo(AadharNo CHAR(12) PRIMARY KEY, Name VARCHAR(20), BloodGroup VARCHAR(5), Amount INT, Disease VARCHAR(20))")
    cursor.execute("CREATE TABLE OrderInfo(OrderId INT PRIMARY KEY, AadharNo CHAR(12), Status CHAR(1), ProductId INT)")
    cursor.execute("CREATE TABLE BloodInfo(ProductId INT PRIMARY KEY, BloodGroup VARCHAR(5), NetAmount INT)")
except:
    print("Tables Already Created")

# Inserting pre recorded information
try:
    db = mysql.connector.connect(host="localhost", user="root", passwd=passd, database="blood_bank")
    cursor = db.cursor()

    cursor.execute("INSERT INTO BloodInfo VALUES(1, 'A+', 0)")
    cursor.execute("INSERT INTO BloodInfo VALUES(2, 'A-', 0)")
    cursor.execute("INSERT INTO BloodInfo VALUES(3, 'B+', 0)")
    cursor.execute("INSERT INTO BloodInfo VALUES(4, 'B-', 0)")
    cursor.execute("INSERT INTO BloodInfo VALUES(5, 'AB+', 0)")
    cursor.execute("INSERT INTO BloodInfo VALUES(6, 'AB-', 0)")
    cursor.execute("INSERT INTO BloodInfo VALUES(7, 'O+', 0)")
    cursor.execute("INSERT INTO BloodInfo VALUES(8, 'O-', 0)")
    db.commit()
except:
    print("Values Already Present")



window = Tk()

icon = PhotoImage(file="icon.png")
bg = PhotoImage(file="background.png")

window.iconphoto(False, icon)
window.title("Blood Bank System")
window.geometry("1280x800")
window.configure(bg = "#FFFFFF")


def donorinfo():

    donor_details = Toplevel()


    def submit():
        db = mysql.connector.connect(host="localhost", user="root", passwd="user123!", database="blood_bank")
        cursor = db.cursor()

        aadhar = e_aadhar.get()
        name = e_name.get()
        blood = e_blood.get()
        amount = int(e_amount.get())

        cursor.execute("SELECT BloodGroup, NetAmount from BloodInfo where BloodGroup = '{0}'".format(blood))
        rec = cursor.fetchone()
        l = []
        l.append(rec[0])
        l.append(rec[1])
        l[1] += amount

        cursor.execute("INSERT INTO DonorInfo VALUES('{0}','{1}', '{2}', {3})".format(aadhar, name, blood, amount))
        cursor.execute("UPDATE BloodInfo set NetAmount = {0} WHERE BloodGroup = '{1}'".format(l[1], blood))
        db.commit()

        e_aadhar.delete(0, END)
        e_name.delete(0, END)
        e_blood.delete(0, END)
        e_amount.delete(0, END)

        messagebox.showinfo(title='Blood Donation', message='Blood Donated Successfully')

        donor_details.destroy()



    def clear():
        e_aadhar.delete(0, END)
        e_name.delete(0, END)
        e_blood.delete(0, END)
        e_amount.delete(0, END)

    donor_details.iconphoto(False, icon)
    donor_details.title("Blood Donation")
    donor_details.geometry("468x265")
    donor_details.configure(background="#780e19")

    e_aadhar = Entry(donor_details, font=('Verdana', 17), bg='#f7dcdf')
    e_aadhar.place(x=160, y=0)
    b_aadhar = Label(donor_details, text='Aadhar No.: ', font=('Verdana', 16), bg='#e0a49f')
    b_aadhar.place(x=2, y=0)

    e_name = Entry(donor_details, font=('Verdana', 17), width=24, bg='#f7dcdf')
    e_name.place(x=100, y=50)
    b_name = Label(donor_details, text='Name: ', font=('Verdana', 16), bg='#e0a49f')
    b_name.place(x=2, y=50)

    e_blood = Entry(donor_details, font=('Verdana', 17), width=20, bg='#f7dcdf')
    e_blood.place(x=160, y=100)
    b_blood = Label(donor_details, text='Blood Group: ', font=('Verdana', 16), bg='#e0a49f')
    b_blood.place(x=2, y=100)

    e_amount = Entry(donor_details, font=('Verdana', 17), width=19, bg='#f7dcdf')
    e_amount.place(x=175, y=150)
    b_amount = Label(donor_details, text='Amount (mL): ', font=('Verdana', 16), bg='#e0a49f')
    b_amount.place(x=2, y=150)

    b_submit = Button(donor_details, text='Submit', font=('Verdana', 16), bg='#e0a49f', width=10, command=submit)
    b_submit.place(x=60, y=220)

    b_clear = Button(donor_details, text='Clear', font=('Verdana', 16), bg='#e0a49f', width=10, command=clear)
    b_clear.place(x=270, y=220)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    400.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=donorinfo,
    relief="flat"
)
button_1.place(
    x=66.0,
    y=619.0,
    width=261.0,
    height=63.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1022.0,
    y=80.0,
    width=202.0,
    height=44.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=571.0,
    y=84.0,
    width=91.0,
    height=37.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=688.0,
    y=84.0,
    width=106.0,
    height=42.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=820.0,
    y=84.0,
    width=91.0,
    height=37.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=917.0,
    y=84.0,
    width=91.0,
    height=37.0
)
window.resizable(False, False)
window.mainloop()






