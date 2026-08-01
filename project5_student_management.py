students = []

while True:
    print("\n=====Student Management System =====")
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Delete Student")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice =="1":
        name = input("Enter Student Name:")

        marks = float(input("Enter Marks:"))


        student = {

            "name":name,
                   "marks": marks
        }

        students.append(student)
        print("StudentAdded successfully!")



    elif choice =="2":
        print("\nStudent List:")

        for student in students:
            print("Name:",student["name"])
            print("Marks:",student["marks"])
            print("________________")


    elif choice =="3":
        search_name = input("Enter Student Name to Search:")

        Found = False

        for student in students:
            if student["name"] == search_name:
                print("Student Found!")
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                found = True
                if not found: print("Student Not Found!")



    elif choice == "4":
        delete_name = input("Enter Student Name to delete : ")
        found = False

        for student in students:
            if student["name"] == delete_name:
                students.remove(student)
                print("Student Deleted Successfully!")
                found = True
                break
        if not found:
            print("Student Not Found!")
