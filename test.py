# create a login system for the user to login and logout
# create a database for the user to store their information
# prompt the user to enter their information
user = input("Enter your username: ")
password = input("Enter your password: ")
# create a database for the user to store their information
import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
# create a table for the user to store their information
c.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password TEXT
)
""")
# prompt the user to enter a string
# encode it using shaSum
# print the string


string = input("Enter a string: ")
import hashlib
string = hashlib.sha256(string.encode()).hexdigest()

# store this string along with the username and password
c.execute("""
INSERT INTO users(username, password)
VALUES (?, ?)
""", (user, string))
conn.commit()
conn.close()
# print the string
print(string)