menu = """

[d] Deposit
[w] Withdraw
[s] Statement
[x] Exit

=> """

balance = 0
limit = 500
statement = ""
number_withdraw = 0
LIMIT_WITHDRAW = 3

while True:

    option = input(menu)

    if option == "d":
        value = float(input("Please, inform the de of your deposit:"))

        if value > 0:
            balance += value
            statement += f"Deposit: $ {value:.2f}\n"

        else: 
            print("This operation has failed. The informed value is invalid.")

    
    elif option == "w":
        value = float(input("Please, inform the value of your withdraw:"))

        exceeded_balance = value > balance
        exceeded_limit = value > limit
        exceeded_withdraw = number_withdraw >= LIMIT_WITHDRAW

        if exceeded_balance:
            print("This operantion has failed. You do not have enough balance.")

        elif exceeded_limit:
            print("This operantion has failed. You do not have enough limit.")

        elif exceeded_withdraw:
            print("This operation has failed. You have reached the maximum number of withdrawals.")

        elif value > 0:
            balance -= value
            statement += (f"Withdraw: $ {balance:.2f}\n")
            number_withdraw += 1

        else:
            print("This operation has failed. The value informed is invalid.")


    elif option == "s":
        print("/n============================== Statement ==============================")
        print("No transactions were made." if not statement else statement)
        print(f"\Balance: $ {balance:.2f}")
        print("=========================================================================")

    elif option == "x":
        break

    else:
        print("Invalid option. Please, try again:")