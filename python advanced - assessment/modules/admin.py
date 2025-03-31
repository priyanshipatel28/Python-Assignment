from database_pharmacy import execute_db, fetch_db

# Admin Registration
def register_admin(name, password):
    try:
        query = "INSERT INTO admin (name, password) VALUES (?, ?)"
        execute_db(query, (name, password))
        print(f"Admin '{name}' registered successfully!")
    except Exception as e:
        print(f"Error registering admin: {e}")

# Admin Login
def login_admin(name, password):
    try:
        query = "SELECT * FROM admin WHERE name = ? AND password = ?"
        result = fetch_db(query, (name, password))

        if result:  #check if the raw is entered!!
            print(f"Login successful for admin: {name}")
            return True
        else:
            print("Invalid admin credentials.")
            return False

    except Exception as e:
        print(f"Error during login: {e}")
        return False

# View all Managers
def view_managers():
    try:
        query = "SELECT * FROM manager"
        managers = fetch_db(query)

        if managers:
            print("\nManagers List:")
            for m in managers:
                print(f"ID: {m[0]}, Name: {m[1]}, Pharmacy: {m[2]}, Created: {m[4]}")
        else:
            print("No managers found.")
    
    except Exception as e:
        print(f"Error fetching managers: {e}")

# View all Medicines
def view_medicines():
   
    try:
        query = "SELECT * FROM medicine"
        medicines = fetch_db(query)

        if medicines:
            print("\nMedicines List:")
            for m in medicines:
                print(f"ID: {m[0]}, Name: {m[1]}, Qty: {m[2]}, Price: {m[3]}")
        else:
            print("No medicines found.")
    
    except Exception as e:
        print(f"Error fetching medicines: {e}")
