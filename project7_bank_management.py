accounts = []

while True:
    print("\n=====Bank Management System=====")
    print("1. Create Account")
    print("2.View Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5.Check Balance")
    print("6. Delete Account")
    print("7. Exit")

    choice = input("Enter your choice:")


    if choice =="1":
        name = input("Enter Account Holder Name: ")
        account_no = input("Enter Account Number:")
        balance = float(input("Enter Initial Balance:"))
        account = {
            "name": name,
            "account_no": account_no,
            "balance":balance
        }

        accounts.append(account)
        print("Account Created Successfully!")

    elif choice == "2":
        print("\n=====Account List=====")

        if len(accounts) == 0:
            print("No Account Found!")

        else:
            for account in accounts:
                print("Name:", account["name"])
                print("Account Number:",account["account_no"])
                print("Balance:",account["balance"])

        print("----------------")
                      

    elif choice == "3":
        account_no = input("Enter Account Number: ")
        amount = float(input("Enter Deposit Amount: "))

        found = False

        for account in accounts:
            if account["account_no"] == account_no:
                account["balance"] += amount
                print(" Money Deposited Successfully!")
                print("New Balance:",account["balance"])
                found = True
                break

        if not found:
            print("Account Not Found!")
