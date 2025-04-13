
menu = """\n
[1] Deposit
[2] Withdrawal
[3] Bank Statement
[0] Quit\n
=> """

balance = 0
limit = 500
bank_statement = ""
withdrawals = 0
withdrawals_limit = 3

while True:
    option = input(menu)

    if option == "1":
        try:
            amount = float(input("Deposit amount: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        if amount > 0:
            balance += amount
            bank_statement += f"Deposit: $ {amount:.2f}\n"
        else:
            print("Failed! The amount is invalid.")

    elif option == "2":
        try:
            amount = float(input("Withdrawal amount: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        exceeded_balance = amount > balance
        exceeded_limit = amount > limit
        exceeded_withdrawal = withdrawals >= withdrawals_limit

        if exceeded_balance:
            print("Failed! You do not have enough balance.")

        elif exceeded_limit:
            print("Failed! The withdrawal amount exceeds the limit.")

        elif exceeded_withdrawal:
            print("Failed! Maximum number of withdrawals exceeded.")

        elif amount > 0:
            balance -= amount
            bank_statement += f"Withdrawal: $ {amount:.2f}\n"
            withdrawals += 1
        else:
            print("Failed! The value entered is invalid.")

    elif option == "3":
        print("\n====== BANK STATEMENT ======")
        print("No transactions were made." if not bank_statement else bank_statement)
        print(f"\nBalance: $ {balance:.2f}")
        print("=============================")

    elif option == "0":
        print("Thank you for using our system. Goodbye!")
        break

    else:
        print("Invalid operation, please select the desired operation again.")
