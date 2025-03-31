import sqlite3

# Connect to the database
def connect_db():
    conn = sqlite3.connect("db_tract")
    return conn

# start it and create Tables
# cursor is the object used to interct with the database!! we connection is established then we create cursor to excute our query!!!
# def init_db():
def table_create():
    
    conn = connect_db()
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS manager (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        pharmacy_name TEXT NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS medicine (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        qty INTEGER NOT NULL,
        price REAL NOT NULL,
        added_by INTEGER NOT NULL,
        added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (added_by) REFERENCES manager(id) ON DELETE CASCADE
    );
    """)
    
    conn.commit()
    conn.close()

# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ===> it will take current time and date
# autoincrement==> it will automatically increse by 1
# query paramter===> the sql query that i will write in file
# params()==> the element to add in quey will be inserted with the help of tuple. onece created no need to changed!



# In exceute_query i have usen try-exccept too make sure that it doesn't cause any error will running!!!!
def execute_db(query, params=()):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# to fetch data from the databse to show in the form of table
def fetch_db(query, params=()):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results
