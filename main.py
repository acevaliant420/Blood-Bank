from tkinter import *
from tkinter import messagebox

import mysql.connector

passd = ""

#Creating a Database
try:
    db = mysql.connector.connect(host="localhost", user="root", passwd=passd)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE blood_bank")
except:
    print("Following Database already exists.")
