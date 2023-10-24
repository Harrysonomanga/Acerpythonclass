import sqlite3

conn = sqlite3.connect('acer.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEE(
ID INT PRIMARY KEY NOT NULL, 
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHARACTER(50),
SALARY REAL);''')
print("Table created successfully")
conn.close()
