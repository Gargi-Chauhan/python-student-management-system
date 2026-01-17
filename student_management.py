import sqlite3

# Database connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll TEXT
)
""")
conn.commit()

# add student func
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    cursor.execute(
        "INSERT INTO students (name, roll) VALUES (?, ?)",
        (name, roll)
    )
    conn.commit()
    print("✅ Student added successfully")
# view student func 
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if not records:
        print("No students found")
    else:
        for r in records:
            print(r)
# menu driven loop
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program")
            break
        else:
            print("Invalid choice")

main()
