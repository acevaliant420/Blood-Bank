from tkinter import *
from tkinter import messagebox
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


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
        cursor.execute("INSERT INTO DonorInfo VALUES('{0}','{1}', '{2}', {3}, {4}, '{5}')".format(aadhar, name, blood, amount, mobile, city))
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

main_window()




