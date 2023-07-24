import mysql.connector
from tabulate import tabulate  # Import tabulate to display data in tabular format

# Establishing connection
con = mysql.connector.connect(host="localhost", user="root", password="varshu0409", database="py_db")
if con:
    print("Connected")
else:
    print("Connection error")


def insert(ID, NAME, AGE, CITY):
    res = con.cursor()
    sql = "INSERT INTO employees (ID, NAME, AGE, CITY) VALUES (%s, %s, %s, %s)"
    user = (ID, NAME, AGE, CITY)
    res.execute(sql, user)
    con.commit()
    print("Data Inserted Successfully")

def update(UP_ID, ID, NAME, AGE, CITY):
    res = con.cursor()
    sql = "UPDATE employees SET ID=%s, NAME=%s, AGE=%s, CITY=%s WHERE ID=%s"  
    user = (ID, NAME, AGE, CITY, UP_ID)
    res.execute(sql, user)
    con.commit()
    print("Data Updated Successfully")

def select():
    res = con.cursor()
    sql = "SELECT ID, NAME, AGE, CITY FROM employees"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "AGE", "CITY"]))

def delete(ID):
    res = con.cursor()
    sql = "DELETE FROM employees WHERE ID=%s"
    user = (ID,)
    res.execute(sql, user)
    con.commit()
    print("Data Deleted Successfully")

def bulk_insert(records):
    res = con.cursor()
    sql = "INSERT INTO employees (ID, NAME, AGE, CITY) VALUES (%s, %s, %s, %s)"
    res.executemany(sql, records)
    con.commit()
    print("Bulk Insert Successful")

while True:
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Select Data")
    print("4. Delete Data")
    print("5. Bulk Insert Data")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        ID = input("Enter your ID: ")
        NAME = input("Enter your Name: ")
        AGE = int(input("Enter your Age: "))
        CITY = input("Enter your College City: ")
        insert(ID, NAME, AGE, CITY)

    elif choice == 2:
        UP_ID = input("Enter your ID: ")
        ID = input("Enter your new id: ")
        NAME = input("Enter your Name: ")
        AGE = int(input("Enter your Age: "))
        CITY = input("Enter your City: ")
        update(UP_ID, ID, NAME, AGE, CITY)

    elif choice == 3:
        select()

    elif choice == 4:
        Id = int(input("Enter the ID to delete: "))
        delete(Id)

    elif choice == 5:
        records = []
        num_records = int(input("Enter the number of records to insert: "))
        for i in range(num_records):
            ID = input(f"Enter ID {i + 1}: ")
            NAME = input(f"Enter Name {i + 1}: ")
            AGE = int(input(f"Enter Age {i + 1}: "))
            CITY = input(f"Enter City Name {i + 1}: ")  
            records.append((ID, NAME, AGE, CITY))
        bulk_insert(records)

    elif choice == 6:
        quit()
    else:
        print("Invalid selection...!")
