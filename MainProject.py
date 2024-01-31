from numpy import source
import GraphandSPwithTime
from GraphandSPwithTime import G
from datetime import datetime
import csv
import hashlib
import sqlite3

def get_data():
    #User will enter the credentials
    User = input("ENTER YOUR USERNAME: ")
    Password = input("Enter your password: ") 
    Confirm = input("Confirm your password: ")

    #Password Validation in order to check if its correct or not
    while Password != Confirm:
        print("Password didnot match")
        Confirm = input("Enter your password: ")

    # Extracting the time.
    # storing the current tme in a variable
    now = datetime.now()
    ctime = now.strftime("%H:%M:%S")

    # encoding the password using shaSum for safe stroing.
    # Password = sha256.sha256(Password.encode()).hexdigest()
    Email = input("Enter your email: ")
    Phone = input("Enter your phone number: ")  
    while len(Phone) != 10:
        print("Invalid phone number! Try again")
        Phone = input()
    #Source and destination is being entered by the user
    Source = input("Enter the source: ")
    Destination = input("Enter the destination: ")

    journey = GraphandSPwithTime.sp(G, Source, Destination)

    # Convert journey to a srtring
    journey = str(journey)

    return User, Password, Email, Phone, ctime, Source, Destination, journey
# store the values returned by the function get_data()


conn = sqlite3.connect('test.db')
c = conn.cursor()

# creating a table for the user to store their information
c.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password TEXT,
    email TEXT,
    phone TEXT,
    time TEXT
)
""")


def add_column():

    # Add a feild if it doesnot exist in the user table to store the source and destination
    c.execute("""
    ALTER TABLE users ADD COLUMN source TEXT
    """)
    c.execute("""
    ALTER TABLE users ADD COLUMN destination TEXT
    """)
    # Add a feild if it doesnot exist in the user table to store the journey
    c.execute("""
    ALTER TABLE users
    ADD COLUMN journey TEXT
    """)
def addData(User, Password, Email, Phone, ctime, Source, Destination, journey):
    # storing this string along with the username and password
    c.execute("""
    INSERT INTO users(username, password, email, phone, time)
    VALUES (?, ?, ?, ?, ?)
    """, (User, Password, Email, Phone, ctime))

    #Adding the source and destination to the user table
    c.execute("""
    UPDATE users SET source = ? WHERE username = ?
    """, (Source, User))
    c.execute("""
    UPDATE users SET destination = ? WHERE username = ?
    """, (Destination, User))

    # store the journey in the user table
    c.execute("""
    UPDATE users
    SET journey = ?
    WHERE username = ?
    """, (journey, User))

    # committing the changes
    conn.commit()


# Print the user information
def printdatabase():
    data = c.execute("""
    SELECT * FROM users
    """)

    print("Username:  ", "Password: ", "Email: ", "Phone: ", "Time: ", "Source: ", "Destination: ", "Journey: ")
    # print the data in table format
    for i in data:
        print(i[0], " ", i[1], " ", i[2], " ", i[3], " ", i[4], " ", i[5], " ", i[6])


def printuserinfo():
    print("Username:  = ", User , ", Email: = ", Email, ", Phone: = ",Phone, ", Time: =  ", ctime, ", Source:  = ", Source , ", Destination:  = ", Destination,", Journey and time(hrs) : = ", journey)

# WELCOME

print("Welcome to the TABDEELI PASSAGE APP")
choice = input("Do you want to Book a ticket? (y/n)")
if choice == "y":
    User, Password, Email, Phone, ctime, Source, Destination, journey = get_data()
    addData(User, Password, Email, Phone, ctime, Source, Destination, journey)
    print("Your ticket has been booked")
    choice = input("Do you want to print your ticket? (y/n)")
    if choice == "y":
        printuserinfo()
    else:
        print("Thank you for using our app")
else:
    print("Thank you for using the TABDEELI PASSAGE APP")
    exit()