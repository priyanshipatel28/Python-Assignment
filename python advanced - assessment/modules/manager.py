from database_pharmacy import execute_db, fetch_db

# Manager Registration
def register_manager(name, pharmacy_name, password):
    try:
        query = "INSERT INTO manager (name, pharmacy_name, password) VALUES (?, ?, ?)"
        execute_db(query, (name, pharmacy_name, password))
        print(f"Manager '{name}' registered successfully!")
    except Exception as e:
        print(f"Error registering manager: {e}")

# Manager Login
def login_manager(name, password):
    try:
        query = "SELECT * FROM manager WHERE name = ? AND password = ?"
        result = fetch_db(query, (name, password))

        if result:
            print(f"Login successful for manager: {name}")
            return result  
        else:
            print("Invalid manager credentials.")
            return []      
    except Exception as e:
        print(f"Error during manager login: {e}")
        return []
    
# Add Medicine
def add_medicine(name, qty, price, manager_id):
    try:
        query = "INSERT INTO medicine (name, qty, price, added_by) VALUES (?, ?, ?, ?)"
        execute_db(query, (name, qty, price, manager_id))
        print(f"Medicine '{name}' added successfully!")
    except Exception as e:
        print(f"Error adding medicine: {e}")

# Delete Medicine
def delete_medicine(medicine_id):
    try:
        query = "DELETE FROM medicine WHERE id = ?"
        execute_db(query, (medicine_id,))
        print(f"Medicine ID {medicine_id} deleted successfully!")
    except Exception as e:
        print(f"Error deleting medicine: {e}")

# View Medicines
def view_medicines():
    try:
        query = "SELECT * FROM medicine"
        medicines = fetch_db(query)

        if medicines:
            print("\nMedicines List:")
            for m in medicines:
                print(f"ID: {m[0]}| Name: {m[1]}| Qty: {m[2]}| Price: {m[3]}")
        else:
            print("No medicines found.")
    
    except Exception as e:
        print(f"Error fetching medicines: {e}")
