expense = []
while True:
    print("\n ------ Welcome to Expense Tracker ------")
    print("1. Add Expense")
    print("2. View total expenses")
    print("3. View all expenses")
    print("4. Exit")

    choice = input("Enter the user choice (1-4): ")

    if choice == "1":
        name = ("Enter the expense name: ")
        amount = ("Enter the amount: ")
        expense.append(amount)
        print("Expense added successfully!")

    elif choice == "2":
        print("All expenses", sum(expense))
    
    elif choice == "3":
            print("All Expenses:")
            for i in expense:
                print(i)
    
    elif choice == "4":
        print("Exiting Expense Tracker. Bye!")
        break

    else: 
        print("Invalid Choice!")