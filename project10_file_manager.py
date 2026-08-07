import os

print("===== File Manager =====")

while True:
    print("\n1. View Files")
    print("2. Create Folder")
    print("3. Delete Folder")
    print("4. Create file")
    print("5.Delete file")
    print("6.Rename File")
    print("7. Exit")

    choice = input("Enter your choice: ")


    if choice =="1":
        files = os.listdir()
        print("\nFiles and  folders:")
        for file in files:
            print(file)


    elif choice =="2":
        folder_name = input("Enter Folder Name: ")
        OS.mkdir(folder_name)
        print("Folder Created Successfully!")

    elif choice =="3":
        folder_name = input("Enter Folder Name: ")
        os.rmdir(folder_name)
        print("Folder Deleted Successfully!")

    elif choice == "4":
        file_name = input ("Enter File Name: ")

        with open(file_name, "w") as file:
            file.write("")

        print("File Created Successfully!")

    elif choice == "5":
        file_name = input("Enter File Name: ")

        if os.path.exists(file_name):
            os.remove(file_name)
            print("File Deleted Successfully!")

        else:
            print("File Not Found!")

    elif choice == "6":
        old_name = input("Enter Old File Name: ")
        new_name = input("Enter new File Name: ")

        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print("File Renamed Successfully!")
        else:
            print("File Not Found!")


    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
