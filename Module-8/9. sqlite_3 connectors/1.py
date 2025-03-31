# Write a Python program to create a database and a table using 
# SQLite3. 22) Write a Python program to insert data into an SQLite3 database and fetch it.

import sqlite3 #it is standard library in python to work with database!

def create_table():
    # 1. establish a connection
    conn = sqlite3.connect('employee.db')
    # 2. to execute commands
    c = conn.cursor()
    # 3. to create table
    c.execute("""CREATE TABLE IF NOT EXISTS employee(
              id INTEGER PRIMARY KEY, 
              firstname TEXT, 
              lastname TEXT, 
              salary INTEGER
              )""")
    
    conn.commit() #to save changes
    conn.close()
    print("Table created successfully!")

def insert_data():
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    
    id = int(input("Enter employee ID: "))
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    salary = int(input("Enter salary: "))
    
    c.execute("INSERT INTO employee VALUES (?, ?, ?, ?)", 
              (id, firstname, lastname, salary))
    
    conn.commit()
    conn.close()
    print("Data inserted successfully!")

def fetch_data():
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM employee")
    rows = c.fetchall()
    
    print("\nEmployee Data:")
    print("ID\tFirst Name\tLast Name\tSalary")
    print("-"*40)
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
    
    conn.close()

def update_data():
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    
    emp_id = int(input("Enter employee ID to update: "))
    
    # Check if employee exists
    c.execute("SELECT id FROM employee WHERE id = ?", (emp_id,))
    result = c.fetchone()
    
    if result is None:
        print(f"Employee with ID {emp_id} not found!")
        conn.close()
        return  # Return to main menu
    
    # If employee exists, ask for new salary
    new_salary = int(input("Enter new salary: "))
    c.execute("UPDATE employee SET salary = ? WHERE id = ?", (new_salary, emp_id))
    
    conn.commit()
    conn.close()
    print("Data updated successfully!")

start = True
while start:
    print("\n1. Create table")
    print("2. Insert data")
    print("3. Fetch data")
    print("4. Update data")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        create_table()
    elif choice == 2:
        insert_data()
    elif choice == 3:
        fetch_data()
    elif choice == 4:
        update_data()
    elif choice == 5:
        start = False
        print("Exiting program...")
    else:
        print("Invalid choice! Please try again.")