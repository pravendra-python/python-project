expenses = []

while True:
    print("\n=====Expense Tracker=====")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Delete Expense")
    print("4.Show Total")
    print("5.Exit")

    choice = input("Enter your choice:")



    if choice =="1":
       amount = float(input("Enter expense amount:"))
       expenses.append(amount)
       print("Expense Added Successfully!")

        
    elif choice =="2":
        print("Expenses:")
        for expense in expenses:
            print(expense)



    elif choice =="4":
        total = sum(expenses)
        print("Total Expense =", total)


    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break
