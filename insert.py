import sqlite3

conn = sqlite3.connect('acer.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(10, 'Geff',28, 'Carlifonia',45000.00)")

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(20, 'Craig',33, 'Texas',15000.00)")

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(30, 'Mark',31, 'Norway',34000.00)")

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(40, 'Brenda',26, 'Kenya',5000.00)")
conn.commit()
print("Records created successfully")
conn.close()