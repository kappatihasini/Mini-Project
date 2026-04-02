students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully")

def view_students():
    for roll in students:
        print("Roll:", roll, "Name:", students[roll]["name"], "Marks:", students[roll]["marks"])

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print("Name:", students[roll]["name"], "Marks:", students[roll]["marks"])
    else:
        print("Student not found")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted")
    else:
        print("Student not found")

while True:
    print("\n1.Add Student\n2.View Students\n3.Search Student\n4.Delete Student\n5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        break
    else:
        print("Invalid choice")