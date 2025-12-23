students = []
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("✅ Student added successfully!\n")
def view_students():
    if not students:
        print("❌ No students found.\n")
        return
    print("\n--- Student List ---")
    for s in students:
        print("ID:", s["ID"])
        print("Name:", s["Name"])
        print("Age:", s["Age"])
        print("Course:", s["Course"])
        print("-------------------")
    print()
def search_student():
    search_id = input("Enter Student ID to search: ")
    for s in students:
        if s["ID"] == search_id:
            print("\n✅ Student Found")
            print("ID:", s["ID"])
            print("Name:", s["Name"])
            print("Age:", s["Age"])
            print("Course:", s["Course"])
            print()
            return
    print("❌ Student not found.\n")
while True:
    print("==== Student Management System ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("👋 Exiting program. Thank you!")
        break
    else:
        print("❌ Invalid choice. Try again.\n")