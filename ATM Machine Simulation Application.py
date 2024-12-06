# Define account information
# Diffirent accounts

from datetime import datetime, timedelta
accounts = [
    {"account_type": "Savings", "pin": "1234", "balance": 1000, "transaction_history": []},
    {"account_type": "Checking", "pin": "5678", "balance": 500, "transaction_history": []},
    {"account_type": "Business", "pin": "9123", "balance": 20000, "transaction_history)":[]},
]

# Function to authenticate the user pin
def authenticate(accounts):
    pin = input("Enter your PIN: ")
    for acc in accounts:
        if acc["pin"] == pin:
            return acc
    return None

# Main loop for interacting with the cash machine
while True:
    user = input('''-----------------------ATM------------------------
            Wolcome to your SMH bank
                \nPlease Enter your bank details: '''
                )
    if user == "admin":
        account = authenticate(accounts)
        if account is None:
            print("Authentication failed. Exiting.")
        else:
            while True:
                print("\n1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. View Transaction History")
                print("5. Change PIN")
                print("6. Exit")
                choice = input("Choose an option: ")

                if choice == '1':
                    # Check balance
                    print(f"Your balance is: ${account['balance']}")
                elif choice == '2':
                    # Deposit money
                    print("Options:")
                    print("1: £5")
                    print("2: £10")
                    print("3: £20")
                    print("4: £50")
                    print("5: £100")
                    print("6: £500")
                    amount_options = [5, 10, 20, 50, 100, 500]
                    dipo = int(input("Select a quantity: "))
                    if 1 <= dipo <= 6:
                        amount = amount_options[dipo - 1]
                        account["balance"] += amount
                        account["transaction_history"].append(f"Deposited: £{amount}")
                        print("Deposit successful.")
                    else:
                        print("Incorrect option.")
                elif choice == '3':
                    # Withdraw money
                    print("Options:")
                    print("1: £5")
                    print("2: £10")
                    print("3: £20")
                    print("4: £50")
                    print("5: £100")
                    print("6: £500")
                    amount_options = [5, 10, 20, 50, 100, 500]
                    draw = int(input("Select a quantity: "))
                    if 1 <= draw <= 6:
                        amount = amount_options[draw - 1]
                        if amount <= account["balance"]:
                            account["balance"] -= amount
                            account["transaction_history"].append(f"Withdrew: £{amount}")
                            print("Withdrawal successful.")
                        else:
                            print("Insufficient funds.")
                    else:
                        print("Incorrect option.")
                elif choice == '4':
                    # View transaction history
                    print("Transaction History:")
                    for transaction in account["transaction_history"]:
                        print(transaction)
                elif choice == '5':
                    # Change PIN
                    new_pin = input("Enter a new PIN: ")
                    account["pin"] = new_pin
                    print("PIN changed successfully.")
                elif choice == '6':
                    # Exit
                    print("Thank you for using the cash machine. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
    else:
        print("Incorrect user details.")
