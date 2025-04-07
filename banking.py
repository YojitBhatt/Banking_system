import json
import os

DATA_FILE = 'bank_accounts.json'

class BankAccount:
    def __init__(self, account_number, name, password, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.balance}")

    def display_balance(self):
        print(f"Account Balance: {self.balance}")

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'name': self.name,
            'password': self.password,
            'balance': self.balance
        }

    @staticmethod
    def from_dict(data):
        return BankAccount(
            data['account_number'],
            data['name'],
            data['password'],
            data['balance']
        )

def load_accounts():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        return {acc_no: BankAccount.from_dict(acc) for acc_no, acc in data.items()}

def save_accounts(accounts):
    with open(DATA_FILE, 'w') as f:
        json.dump({acc_no: acc.to_dict() for acc_no, acc in accounts.items()}, f, indent=4)

def authenticate(accounts, acc_no, password):
    account = accounts.get(acc_no)
    if account and account.password == password:
        return account
    print("Authentication failed.")
    return None

accounts = load_accounts()

def main():
    while True:
        print("\n===== Secure Bank System =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Account Details")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            acc_no = input("Enter Account Number: ")
            name = input("Enter Account Holder Name: ")
            password = input("Set a Password: ")
            if acc_no in accounts:
                print("Account already exists.")
            else:
                accounts[acc_no] = BankAccount(acc_no, name, password)
                save_accounts(accounts)
                print("Account created successfully.")

        elif choice in ['2', '3', '4', '5']:
            acc_no = input("Enter Account Number: ")
            password = input("Enter Password: ")
            account = authenticate(accounts, acc_no, password)

            if account:
                if choice == '2':
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)

                elif choice == '3':
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)

                elif choice == '4':
                    account.display_balance()

                elif choice == '5':
                    account.display_account_details()

                save_accounts(accounts)

        elif choice == '6':
            print("Thank you for using Secure Bank System.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
