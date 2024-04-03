from tkinter import *
from tkinter import messagebox
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label

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
    cursor.execute("CREATE TABLE DonorInfo(AadharNo VARCHAR(12) PRIMARY KEY, Name VARCHAR(40), BloodGroup VARCHAR(5), Amount INT, MobileNo VARCHAR(10), City VARCHAR(20))")
    cursor.execute("CREATE TABLE PatientsInfo(AadharNo VARCHAR(12) PRIMARY KEY, Name VARCHAR(40), BloodGroup VARCHAR(5), Amount INT, Disease VARCHAR(20))")
    cursor.execute("CREATE TABLE OrderInfo(OrderId INT PRIMARY KEY, AadharNo CHAR(12), Status CHAR(1), ProductId INT)")
    cursor.execute("CREATE TABLE BloodInfo(ProductId INT PRIMARY KEY, BloodGroup VARCHAR(5), NetAmount INT)")
    db.commit()
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

def productID(st):
    if(st == 'A+'):
        return 1
    elif(st== 'A-'):
        return 2
    elif (st == 'B+'):
        return 3
    elif (st == 'B-'):
        return 4
    elif (st == 'AB+'):
        return 5
    elif (st == 'AB-'):
        return 6
    elif (st == 'O+'):
        return 7
    elif (st == 'O-'):
        return 8



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\College\2. Second Year\SEM 4\2. Labs\CS262 (DBMS Lab)\Project\Blood-Bank\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
window = Tk()

def patientsinfo():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"E:\College\2. Second Year\SEM 4\2. Labs\CS262 (DBMS Lab)\Project\Blood-Bank\assets\frame3")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    newwindow = Toplevel(window)
    newwindow.title("Get Blood")
    newwindow.geometry("917x622")
    newwindow.configure(bg="#FFFFFF")

    canvas = Canvas(
        newwindow,
        bg="#FFFFFF",
        height=622,
        width=917,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        458.0,
        311.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        newwindow,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=349.0,
        y=548.0,
        width=217.0,
        height=54.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        630.0,
        139.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=459.0,
        y=123.0,
        width=342.0,
        height=31.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        630.0,
        192.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=459.0,
        y=176.0,
        width=342.0,
        height=31.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        630.0,
        244.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=459.0,
        y=228.0,
        width=342.0,
        height=31.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        630.0,
        296.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=459.0,
        y=280.0,
        width=342.0,
        height=31.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        630.0,
        352.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=459.0,
        y=336.0,
        width=342.0,
        height=31.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        630.0,
        409.5,
        image=entry_image_6
    )
    entry_6 = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=459.0,
        y=393.0,
        width=342.0,
        height=31.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        630.0,
        480.5,
        image=entry_image_7
    )
    entry_7 = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=459.0,
        y=444.0,
        width=342.0,
        height=71.0
    )
    newwindow.resizable(False, False)
    newwindow.mainloop()


def donorinfo():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"E:\College\2. Second Year\SEM 4\2. Labs\CS262 (DBMS Lab)\Project\Blood-Bank\assets\frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    newwindow = Toplevel(window)
    newwindow.title("Donate Blood Now")
    newwindow.geometry("917x622")
    newwindow.configure(bg="#FFFFFF")

    new_canva = Canvas(
        newwindow,
        bg="#FFFFFF",
        height=622,
        width=917,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    def newsubmit():
        db = mysql.connector.connect(host="localhost", user="root", passwd="user123!", database="blood_bank")
        cursor = db.cursor()

        aadhar = e_aadhar.get()
        name = e_name.get()
        blood = e_blood.get()
        amount = int(e_amount.get())
        mobile = int(e_mobile.get())
        city = e_city.get()
        prod = productID(blood)
        cursor.execute("SELECT BloodGroup, NetAmount from BloodInfo where productid = '{0}'".format(prod))
        rec = cursor.fetchone()
        l = []
        l.append(rec[0])
        l.append(rec[1])
        l[1] += amount
        print(prod)
        cursor.execute("UPDATE BloodInfo set NetAmount = {0} WHERE productid = '{1}'".format(l[1], prod))
        db.commit()
        cursor.execute("INSERT INTO DonorInfo (AadharNo, Name, BloodGroup, Amount, MobileNo, City) VALUES('{0}','{1}', '{2}', {3}, {4}, '{5}')".format(aadhar, name, blood, amount, mobile, city))
        db.commit()
        print("doing")
        db.commit()
        print("done")
        e_aadhar.delete(0, END)
        e_name.delete(0, END)
        e_blood.delete(0, END)
        e_amount.delete(0, END)
        e_mobile.delete(0, END)
        e_city.delete(0, END)

        messagebox.showinfo(title='Blood Donation', message='Blood Donated Successfully')
        newwindow.destroy()


    new_canva.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = new_canva.create_image(
        458.0,
        311.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        newwindow,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=newsubmit,
        relief="flat"
    )
    button_1.place(
        x=349.0,
        y=548.0,
        width=217.0,
        height=54.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = new_canva.create_image(
        629.0,
        117.5,
        image=entry_image_1
    )
    e_aadhar = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    e_aadhar.place(
        x=458.0,
        y=101.0,
        width=342.0,
        height=31.0
    )


    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = new_canva.create_image(
        629.0,
        182.5,
        image=entry_image_2
    )
    e_name = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    e_name.place(
        x=458.0,
        y=166.0,
        width=342.0,
        height=31.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = new_canva.create_image(
        629.0,
        254.5,
        image=entry_image_3
    )
    e_blood = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    e_blood.place(
        x=458.0,
        y=238.0,
        width=342.0,
        height=31.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = new_canva.create_image(
        629.0,
        320.5,
        image=entry_image_4
    )
    e_amount = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    e_amount.place(
        x=458.0,
        y=304.0,
        width=342.0,
        height=31.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = new_canva.create_image(
        629.0,
        394.5,
        image=entry_image_5
    )
    e_mobile = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    e_mobile.place(
        x=458.0,
        y=378.0,
        width=342.0,
        height=31.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = new_canva.create_image(
        629.0,
        461.5,
        image=entry_image_6
    )
    e_city = Entry(
        newwindow,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    e_city.place(
        x=458.0,
        y=445.0,
        width=342.0,
        height=31.0
    )
    newwindow.resizable(False, False)
    newwindow.mainloop()


def check_availability():

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"E:\College\2. Second Year\SEM 4\2. Labs\CS262 (DBMS Lab)\Project\Blood-Bank\assets\frame2")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    newwindow = Toplevel(window)
    newwindow.title("Blood Availability")


    newwindow.geometry("1000x500")
    newwindow.configure(bg="#FFFFFF")

    canvas = Canvas(
        newwindow,
        bg="#FFFFFF",
        height=500,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        500.0,
        250.0,
        image=image_image_1
    )

    cursor.execute("SELECT BloodGroup, NetAmount from BloodInfo where productid = 1")
    rec = cursor.fetchone()
    l1 = []
    l1.append(rec[0])
    l1.append(rec[1])

    cursor.execute("SELECT BloodGroup, NetAmount from BloodInfo where productid =  2")
    rec = cursor.fetchone()
    l2 = []
    l2.append(rec[0])
    l2.append(rec[1])
    print(l2[1])

    cursor.execute("SELECT BloodGroup, NetAmount from BloodInfo where productid =  3")
    rec = cursor.fetchone()
    l3 = []
    l3.append(rec[0])
    l3.append(rec[1])

    cursor.execute("SELECT BloodGroup, NetAmount from BloodInfo where productid =  4")
    rec = cursor.fetchone()
    l4 = []
    l4.append(rec[0])
    l4.append(rec[1])

    cursor.execute("SELECT BloodGroup, NetAmount from BloodInfo where productid =  5")
    rec = cursor.fetchone()
    l5 = []
    l5.append(rec[0])
    l5.append(rec[1])

    cursor.execute("SELECT BloodGroup, NetAmount from BloodInfo where productid =  6")
    rec = cursor.fetchone()
    l6 = []
    l6.append(rec[0])
    l6.append(rec[1])

    cursor.execute("SELECT BloodGroup, NetAmount from BloodInfo where productid =  7")
    rec = cursor.fetchone()
    l7 = []
    l7.append(rec[0])
    l7.append(rec[1])

    cursor.execute("SELECT BloodGroup, NetAmount from BloodInfo where productid =  8")
    rec = cursor.fetchone()
    l8 = []
    l8.append(rec[0])
    l8.append(rec[1])
    db.commit()
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        195.5,
        190.0,
        image=entry_image_1
    )
    entry_1 = Label(
        newwindow,
        text=l1[1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=163.0,
        y=165.0,
        width=65.0,
        height=48.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        195.5,
        380.0,
        image=entry_image_2
    )
    entry_2 = Label(
        newwindow,
        text=l5[1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=163.0,
        y=355.0,
        width=65.0,
        height=48.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        421.5,
        380.0,
        image=entry_image_3
    )
    entry_3 = Label(
        newwindow,
        text=l6[1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=389.0,
        y=355.0,
        width=65.0,
        height=48.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        647.5,
        380.0,
        image=entry_image_4
    )
    entry_4 = Label(
        newwindow,
        text=l7[1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=615.0,
        y=355.0,
        width=65.0,
        height=48.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        873.5,
        380.0,
        image=entry_image_5
    )
    entry_5 = Label(
        newwindow,
        text=l8[1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=841.0,
        y=355.0,
        width=65.0,
        height=48.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        421.5,
        190.0,
        image=entry_image_6
    )
    entry_6 = Label(
        newwindow,
        text=l2[1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=389.0,
        y=165.0,
        width=65.0,
        height=48.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        647.5,
        190.0,
        image=entry_image_7
    )
    entry_7 = Label(
        newwindow,
        text=l3[1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=615.0,
        y=165.0,
        width=65.0,
        height=48.0
    )

    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        873.5,
        190.0,
        image=entry_image_8
    )
    entry_8 = Label(
        newwindow,
        text=l4[1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_8.place(
        x=841.0,
        y=165.0,
        width=65.0,
        height=48.0
    )
    newwindow.resizable(False, False)
    newwindow.mainloop()


def main_window():

    icon = PhotoImage(file="icon.png")
    bg = PhotoImage(file="background.png")

    window.iconphoto(False, icon)
    window.title("Blood Bank System")
    window.geometry("1280x800")
    window.configure(bg="#FFFFFF")




    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=800,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
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
        command=check_availability,
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
        command=patientsinfo,
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

main_window()




