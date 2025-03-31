# Import all functions from the modules
from modules import *
from database_pharmacy import table_create

# **************************** Initialize the tables ****************************
table_create()

# **************************** Main Program Loop ****************************
while True:
    print("\n" + "=" * 50 + "\n" + " " * 20 + "Welcome to Pharmacy Management System" + "\n" + "=" * 50)

    print("\n1. Admin Register")
    print("2. Admin Login")
    print("3. Manager Register")
    print("4. Manager Login")
    print("5. Exit")

    choice = input("\nChoose an option: ").strip()

    # **************************** Admin Register ****************************
    if choice == '1':
        # Register a new admin
        print("\n" + "*" * 50 + "\n" + " " * 20 + "Admin Register" + "\n" + "*" * 50)

        name = input("Enter Admin Name: ").strip()
        password = input("Enter Admin Password: ").strip()
        register_admin(name, password)

    # **************************** Admin Login with Choices ****************************
    elif choice == '2':
        # Admin login and options
        print("\n" + "*" * 50 + "\n" + " " * 20 + "Admin Login" + "\n" + "*" * 50)

        name = input("Enter Admin Name: ").strip()
        password = input("Enter Admin Password: ").strip()

        if login_admin(name, password):
            print("\n" + "=" * 50 + "\n" + " " * 20 + "Admin login successful!" + "\n" + "=" * 50)

            # Admin options loop
            while True:
                print("\n" + "-" * 50 + "\n" + " " * 20 + "Admin Options" + "\n" + "-" * 50)

                print("1. View Managers")
                print("2. View Medicines")
                print("3. Logout")

                admin_choice = input("\nChoose an option: ").strip()

                if admin_choice == '1':
                    print("\n" + "*" * 50 + "\n" + " " * 20 + "Viewing Managers" + "\n" + "*" * 50)
                    view_managers()

                elif admin_choice == '2':
                    print("\n" + "*" * 50 + "\n" + " " * 20 + "Viewing Medicines" + "\n" + "*" * 50)
                    view_medicines()

                elif admin_choice == '3':
                    print("\n" + "-" * 50 + "\n" + " " * 20 + "Logging out as Admin..." + "\n" + "-" * 50)
                    break

                else:
                    print("\n" + "=" * 50 + "\n" + " " * 20 + "Invalid option. Try again." + "\n" + "=" * 50)
        else:
            print("\n" + "=" * 50 + "\n" + " " * 15 + "Invalid admin credentials. Please register first!" + "\n" + "=" * 50)

    # **************************** Manager Register ****************************
    elif choice == '3':
        print("\n" + "*" * 50 + "\n" + " " * 20 + "Manager Register" + "\n" + "*" * 50)

        name = input("Enter Manager Name: ").strip()
        pharmacy = input("Enter Pharmacy Name: ").strip()
        password = input("Enter Manager Password: ").strip()
        register_manager(name, pharmacy, password)

    # **************************** Manager Login with Choices ****************************
    elif choice == '4':
        print("\n" + "*" * 50 + "\n" + " " * 20 + "Manager Login" + "\n" + "*" * 50)

        name = input("Enter Manager Name: ").strip()
        password = input("Enter Manager Password: ").strip()

        existing_manager = login_manager(name, password)

        if existing_manager:
            print("\n" + "=" * 50 + "\n" + " " * 20 + "Manager login successful!" + "\n" + "=" * 50)

            # Manager options loop
            while True:
                print("\n" + "-" * 50 + "\n" + " " * 20 + "Manager Options" + "\n" + "-" * 50)

                print("1. Add Medicine")
                print("2. View Medicines")
                print("3. Delete Medicine")
                print("4. Logout")

                sub_choice = input("\nChoose an option: ").strip()

                if sub_choice == '1':
                    print("\n" + "*" * 50 + "\n" + " " * 20 + "Add Medicine" + "\n" + "*" * 50)

                    try:
                        medicine_name = input("Enter Medicine Name: ").strip()
                        qty = int(input("Enter Quantity: ").strip())
                        price = float(input("Enter Price: ").strip())
                        if existing_manager:
                            manager_id = existing_manager[0][0]  # Get manager ID safely
                            add_medicine(medicine_name, qty, price, manager_id)
                        else:
                            print("Error: Manager ID not found!")
                    except Exception as e:
                        print(f"An error occurred: {e}")

                elif sub_choice == '2':
                    print("\n" + "*" * 50 + "\n" + " " * 20 + "View Medicines" + "\n" + "*" * 50)
                    view_medicines()

                elif sub_choice == '3':
                    print("\n" + "*" * 50 + "\n" + " " * 20 + "Delete Medicine" + "\n" + "*" * 50)

                    try:
                        medicine_id = int(input("Enter Medicine ID to delete: ").strip())
                        delete_medicine(medicine_id)
                    except Exception as e:
                        print(f"An error occurred: {e}")

                elif sub_choice == '4':
                    print("\n" + "-" * 50 + "\n" + " " * 20 + "Logging out as Manager..." + "\n" + "-" * 50)
                    break

                else:
                    print("\n" + "=" * 50 + "\n" + " " * 20 + "Invalid option. Try again." + "\n" + "=" * 50)
        else:
            print("\n" + "=" * 50 + "\n" + " " * 15 + "Invalid manager credentials. Please register first!" + "\n" + "=" * 50)

    # **************************** Exit the Program ****************************
    elif choice == '5':
        print("\n" + "=" * 50 + "\n" + " " * 15 + "Don't some again!, Goodbye!" + "\n" + "=" * 50)
        break

    else:
        print("\n" + "=" * 50 + "\n" + " " * 20 + "Invalid choice. Try again." + "\n" + "=" * 50)
