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

    def submit():
        db = mysql.connector.connect(host="localhost", user="root", passwd="user123!", database="blood_bank")
        cursor = db.cursor()

        name = e_name.get()
        blood = e_blood.get()
        try:
            aadhar = int(e_aadhar.get())
            amount = int(e_amount.get())
            mobile = int(e_mobile.get())
        except:
            messagebox.showerror(title='Blood Donation', message='Empty Form/wrong Entry')
            newwindow.destroy()
            return
        city = e_city.get()
        prod = productID(blood)

        d_aa = len(str(aadhar))
        d_mob = len(str(mobile))

        if (d_aa != 12):
            messagebox.showerror(title='Aadhar Error', message='Aadhar No. should be of 12 digits')
            newwindow.destroy()
            return
        if (d_mob != 10):
            messagebox.showerror(title='Aadhar Error', message='Mobile No. should be of 10 digits')
            newwindow.destroy()
            return

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

def about_us():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(
        r"E:\College\2. Second Year\SEM 4\2. Labs\CS262 (DBMS Lab)\Project\Blood-Bank\assets\frame5")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    newwindow = Toplevel(window)
    newwindow.title("About Us")
    newwindow.geometry("800x800")
    newwindow.configure(bg="#FFFFFF")

    canvas = Canvas(
        newwindow,
        bg="#FFFFFF",
        height=800,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        400.0,
        image=image_image_1
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


        name = e_name.get()
        blood = e_blood.get()
        try:
            aadhar = int(e_aadhar.get())
            amount = int(e_amount.get())
            mobile = int(e_mobile.get())
        except:
            messagebox.showerror(title='Blood Donation', message='Empty Form/wrong Entry')
            newwindow.destroy()
            return
        city = e_city.get()
        prod = productID(blood)

        d_aa = len(str(aadhar))
        d_mob = len(str(mobile))

        if(d_aa!=12):
            messagebox.showerror(title='Aadhar Error', message='Aadhar No. should be of 12 digits')
            newwindow.destroy()
            return
        if (d_mob!=10):
            messagebox.showerror(title='Aadhar Error', message='Mobile No. should be of 10 digits')
            newwindow.destroy()
            return


        if(prod >=1 and prod<=8):
            print("good")
        else:
            messagebox.showerror(title='Wrong Blood Group', message='Wrong Blood Group Entered')
            newwindow.destroy()
            return



        try:
            cursor.execute("INSERT INTO DonorInfo (AadharNo, Name, BloodGroup, Amount, MobileNo, City) VALUES('{0}','{1}', '{2}', {3}, {4}, '{5}')".format(aadhar, name, blood, amount, mobile, city))
            db.commit()
        except:
            print("Checking if user is already entered")
            try:
                cursor.execute("SELECT Amount from DonorInfo where AadharNo = '{0}';".format(aadhar))
                rec = cursor.fetchone()
                l = []
                l.append(rec[0])
                cursor.execute("UPDATE DonorInfo SET Amount = Amount + {0} WHERE AadharNo = {1};".format(l[0], aadhar))
                db.commit()

            except:
                messagebox.showerror(title='Blood Donation', message='Blood could not be donated')
                newwindow.destroy()
                return



        try:
            cursor.execute("SELECT BloodGroup, NetAmount from BloodInfo where productid = '{0}';".format(prod))
            rec = cursor.fetchone()
            l = []
            l.append(rec[0])
            l.append(rec[1])
            amount += l[1]
            print(amount)
            cursor.execute("UPDATE BloodInfo set NetAmount = {0} WHERE productid = '{1}';".format(amount, prod))
            db.commit()


            e_aadhar.delete(0, END)
            e_name.delete(0, END)
            e_blood.delete(0, END)
            e_amount.delete(0, END)
            e_mobile.delete(0, END)
            e_city.delete(0, END)

            messagebox.showinfo(title='Blood Donation', message='Blood Donated Successfully')
            newwindow.destroy()
        except:
            messagebox.showerror(title='Blood Donation', message='Could Not Update Blood Group Amount')
            db.rollback()
            newwindow.destroy()
            return

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


def top_donors():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(
        r"E:\College\2. Second Year\SEM 4\2. Labs\CS262 (DBMS Lab)\Project\Blood-Bank\assets\frame4")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    newwindow = Toplevel(window)
    newwindow.title("Top Donors")

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

    db = mysql.connector.connect(host="localhost", user="root", passwd="user123!", database="blood_bank")
    cursor = db.cursor()

    try:
        cursor.execute("CREATE VIEW top_donor AS select Name, BloodGroup, Amount, City from donorinfo order by amount desc limit 6;")
    except:
        print("View Already Created")

    cursor.execute("select * from top_donor")
    rec = cursor.fetchall()
    l = []

    l.append(rec[0])
    l.append(rec[1])
    l.append(rec[2])
    l.append(rec[3])
    l.append(rec[4])
    l.append(rec[5])




    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        newwindow,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=newwindow.destroy,
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
        224.0,
        177.5,
        image=entry_image_1
    )
    entry_1 = Label(
        newwindow,
        text=l[0][0],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=107.0,
        y=161.0,
        width=234.0,
        height=31.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        224.0,
        239.5,
        image=entry_image_2
    )
    entry_2 = Label(
        newwindow,
        text=l[1][0],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=107.0,
        y=223.0,
        width=234.0,
        height=31.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        224.0,
        301.5,
        image=entry_image_3
    )
    entry_3 = Label(
        newwindow,
        text=l[2][0],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=107.0,
        y=285.0,
        width=234.0,
        height=31.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        441.0,
        177.5,
        image=entry_image_4
    )
    entry_4 = Label(
        newwindow,
        text=l[0][1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=389.0,
        y=161.0,
        width=104.0,
        height=31.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        441.0,
        239.5,
        image=entry_image_5
    )
    entry_5 = Label(
        newwindow,
        text=l[1][1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=389.0,
        y=223.0,
        width=104.0,
        height=31.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        441.0,
        301.5,
        image=entry_image_6
    )
    entry_6 = Label(
        newwindow,
        text=l[2][1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=389.0,
        y=285.0,
        width=104.0,
        height=31.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        593.0,
        177.5,
        image=entry_image_7
    )
    entry_7 = Label(
        newwindow,
        text=l[0][2],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=541.0,
        y=161.0,
        width=104.0,
        height=31.0
    )

    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        593.0,
        239.5,
        image=entry_image_8
    )
    entry_8 = Label(
        newwindow,
        text=l[1][2],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_8.place(
        x=541.0,
        y=223.0,
        width=104.0,
        height=31.0
    )

    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        593.0,
        301.5,
        image=entry_image_9
    )
    entry_9 = Label(
        newwindow,
        text=l[2][2],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_9.place(
        x=541.0,
        y=285.0,
        width=104.0,
        height=31.0
    )

    entry_image_10 = PhotoImage(
        file=relative_to_assets("entry_10.png"))
    entry_bg_10 = canvas.create_image(
        760.5,
        177.5,
        image=entry_image_10
    )
    entry_10 = Label(
        newwindow,
        text=l[0][3],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_10.place(
        x=693.0,
        y=161.0,
        width=135.0,
        height=31.0
    )

    entry_image_11 = PhotoImage(
        file=relative_to_assets("entry_11.png"))
    entry_bg_11 = canvas.create_image(
        760.5,
        239.5,
        image=entry_image_11
    )
    entry_11 = Label(
        newwindow,
        text=l[1][3],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_11.place(
        x=693.0,
        y=223.0,
        width=135.0,
        height=31.0
    )

    entry_image_12 = PhotoImage(
        file=relative_to_assets("entry_12.png"))
    entry_bg_12 = canvas.create_image(
        760.5,
        301.5,
        image=entry_image_12
    )
    entry_12 = Label(
        newwindow,
        text=l[2][3],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_12.place(
        x=693.0,
        y=285.0,
        width=135.0,
        height=31.0
    )

    entry_image_13 = PhotoImage(
        file=relative_to_assets("entry_13.png"))
    entry_bg_13 = canvas.create_image(
        224.0,
        363.5,
        image=entry_image_13
    )
    entry_13 = Label(
        newwindow,
        text=l[3][0],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_13.place(
        x=107.0,
        y=347.0,
        width=234.0,
        height=31.0
    )

    entry_image_14 = PhotoImage(
        file=relative_to_assets("entry_14.png"))
    entry_bg_14 = canvas.create_image(
        441.0,
        363.5,
        image=entry_image_14
    )
    entry_14 = Label(
        newwindow,
        text=l[3][1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_14.place(
        x=389.0,
        y=347.0,
        width=104.0,
        height=31.0
    )

    entry_image_15 = PhotoImage(
        file=relative_to_assets("entry_15.png"))
    entry_bg_15 = canvas.create_image(
        593.0,
        363.5,
        image=entry_image_15
    )
    entry_15 = Label(
        newwindow,
        text=l[3][2],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_15.place(
        x=541.0,
        y=347.0,
        width=104.0,
        height=31.0
    )

    entry_image_16 = PhotoImage(
        file=relative_to_assets("entry_16.png"))
    entry_bg_16 = canvas.create_image(
        760.5,
        363.5,
        image=entry_image_16
    )
    entry_16 = Label(
        newwindow,
        text=l[3][3],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_16.place(
        x=693.0,
        y=347.0,
        width=135.0,
        height=31.0
    )

    entry_image_17 = PhotoImage(
        file=relative_to_assets("entry_17.png"))
    entry_bg_17 = canvas.create_image(
        224.0,
        425.5,
        image=entry_image_17
    )
    entry_17 = Label(
        newwindow,
        text=l[4][0],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_17.place(
        x=107.0,
        y=409.0,
        width=234.0,
        height=31.0
    )

    entry_image_18 = PhotoImage(
        file=relative_to_assets("entry_18.png"))
    entry_bg_18 = canvas.create_image(
        441.0,
        425.5,
        image=entry_image_18
    )
    entry_18 = Label(
        newwindow,
        text=l[4][1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_18.place(
        x=389.0,
        y=409.0,
        width=104.0,
        height=31.0
    )

    entry_image_19 = PhotoImage(
        file=relative_to_assets("entry_19.png"))
    entry_bg_19 = canvas.create_image(
        593.0,
        425.5,
        image=entry_image_19
    )
    entry_19 = Label(
        newwindow,
        text=l[4][2],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_19.place(
        x=541.0,
        y=409.0,
        width=104.0,
        height=31.0
    )

    entry_image_20 = PhotoImage(
        file=relative_to_assets("entry_20.png"))
    entry_bg_20 = canvas.create_image(
        760.5,
        425.5,
        image=entry_image_20
    )
    entry_20 = Label(
        newwindow,
        text=l[4][3],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_20.place(
        x=693.0,
        y=409.0,
        width=135.0,
        height=31.0
    )

    entry_image_21 = PhotoImage(
        file=relative_to_assets("entry_21.png"))
    entry_bg_21 = canvas.create_image(
        224.0,
        487.5,
        image=entry_image_21
    )
    entry_21 = Label(
        newwindow,
        text=l[5][0],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_21.place(
        x=107.0,
        y=471.0,
        width=234.0,
        height=31.0
    )

    entry_image_22 = PhotoImage(
        file=relative_to_assets("entry_22.png"))
    entry_bg_22 = canvas.create_image(
        441.0,
        487.5,
        image=entry_image_22
    )
    entry_22 = Label(
        newwindow,
        text=l[5][1],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_22.place(
        x=389.0,
        y=471.0,
        width=104.0,
        height=31.0
    )

    entry_image_23 = PhotoImage(
        file=relative_to_assets("entry_23.png"))
    entry_bg_23 = canvas.create_image(
        593.0,
        487.5,
        image=entry_image_23
    )
    entry_23 = Label(
        newwindow,
        text=l[5][2],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_23.place(
        x=541.0,
        y=471.0,
        width=104.0,
        height=31.0
    )

    entry_image_24 = PhotoImage(
        file=relative_to_assets("entry_24.png"))
    entry_bg_24 = canvas.create_image(
        760.5,
        487.5,
        image=entry_image_24
    )
    entry_24 = Label(
        newwindow,
        text=l[5][3],
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_24.place(
        x=693.0,
        y=471.0,
        width=135.0,
        height=31.0
    )
    newwindow.resizable(False, False)
    newwindow.mainloop()
    db.commit()


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

    db = mysql.connector.connect(host="localhost", user="root", passwd="user123!", database="blood_bank")
    cursor = db.cursor()

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

    """    button_image_3 = PhotoImage(
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
    )"""

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=about_us,
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
        command=top_donors,
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




