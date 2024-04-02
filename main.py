from tkinter import *
from tkinter import messagebox

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
