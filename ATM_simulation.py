from datetime import datetime

current_balance = 0
transactions_history = []

def check_balance():
    print("Checking balance...")
    print(f"Current balance: {current_balance}")

def deposit():
    global current_balance
    try:
        user_deposit = input("Enter the amount to deposit: ")
        amount = float(user_deposit)
        if amount <= 0:
            print("Please enter a positive number")
            return
        current_balance += amount
        print(f"Current balance: {current_balance}")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"Deposited ${amount} on {now}"
        transactions_history.append(log_message)

    except ValueError:
        print("Invalid input. PLease try again")

def withdraw():
    global current_balance
    try:
        user_withdraw = input("Enter the amount to withdraw: ")
        amount = float(user_withdraw)
        if amount > current_balance:
            print("insufficient funds")
            return

        elif amount <= 0:
            print("Please enter a positive number.")
            return

        current_balance -= amount
        print(f"Current balance: {current_balance}")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"Withdrew  ${amount} on {now}"
        transactions_history.append(log_message)

    except ValueError:
        print("Invalid input. PLease try again")

def view_transactions():
    global transactions_history
    print("\nTransactions History:")
    if not transactions_history:
        print("No transactions yet")
    for transaction in transactions_history:
        print(transaction)


menu = {
    "1": check_balance,
    "2": deposit,
    "3": withdraw,
    "4": view_transactions,
    "5": exit
}

while True:
    print("Welcome to the Miku Bank ATM")
    print("1) Check Balance")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) View Transactions")
    print("5) Exit")
    user_choice = input("Please choose an option: ")

    if user_choice in menu:
        if user_choice == "5":
            print("Thank you for using ATM")
        menu[user_choice]()
    else:
        print("Invalid input. PLease try again 1 - 5")
