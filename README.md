# Banking_system

Overview
This is a console-based banking application in Python that allows users to:
Create bank accounts with a password
Deposit and withdraw money
Check balance and account details
Save all data in a JSON file for persistence

Program Flow
1. File-Based Storage Setup
The file bank_accounts.json stores all accounts.
load_accounts() loads this data when the program starts.
save_accounts() writes updated data back to the file after any operation.
This allows the banking system to remember all accounts even after closing the program.

2. BankAccount Class
The BankAccount class represents each user's account and has:
account_number – unique ID for the account
name – account holder name
password – for login
balance – money in account

Methods included:
deposit(amount)
withdraw(amount)
display_balance()
display_account_details()
to_dict() – for saving data to JSON
from_dict() – for loading data from JSON

3. Creating an Account
When a user selects option 1, they are asked to enter:
Account number
Name
Password
The program checks if the account already exists. If not, it creates a new one and saves it in bank_accounts.json.

4. Authentication
Before doing anything with an account (deposit, withdraw, etc.), the user is asked to:
Enter account number
Enter password
The system checks if the password is correct using the authenticate() function.

5. Deposit / Withdraw / Balance Check / Details
Deposit: Adds money to the account.
Withdraw: Checks if balance is sufficient, then subtracts amount.
Check Balance: Displays current balance.
Account Details: Shows account number, name, and balance.
Each action saves updated data to the file.

6. Exit
Choosing option 6 stops the program with a goodbye message.

🔐 Security
Passwords are required to access an account.

Passwords are stored as plain text in JSON, which is simple but not very secure. (We can improve this later using hashing.)
