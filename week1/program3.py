"""
Build a program that simulates a basic ATM transaction.
Allow users to deposit, withdraw, and check their balance.
"""


def select_choice():
    print("1: Check available balance")
    print("2: Withdraw money")
    print("3: Deposit money")
    print("4: Exit")


def check_balance(balance):
    print(f"You have {balance: .2f} in your account.")


def withdraw_money(balance, amount):
    if 0 < amount <= balance:
        balance -= amount
        print(f"{amount: .2f} withdrawn. Remaining balance: {balance :.2f}")
    else:
        print("Unsupported")
    return balance


def deposit_money(balance, amount):
    if amount > 0:
        balance += amount
        print(f"{amount:.2f} deposited. Total balance: {balance:.2f}")
    else:
        print("Unsupported")
    return balance


def atm():
    balance = 1000
    while True:
        select_choice()
        choice = int(input("Enter choice:"))

        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            amount = float(input("Enter the amount: "))
            balance = withdraw_money(balance, amount)
        elif choice == 3:
            amount = float(input("Enter the amount: "))
            balance = deposit_money(balance, amount)
        elif choice == 4:
            print("Good Day sir/madam!!")
            break
        else:
            print("Invalid ip")


if __name__ == "__main__":
    atm()