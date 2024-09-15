#modified code
import Accounts
import ATM

Account1 = Accounts.Accounts(
    account_number=123456,
    account_firstname="Royce",
    account_lastname="Chua",
    current_balance=1000,
    address="Silver Street Quezon City",
    email="roycechua123@gmail.com"
)

Account2 = Accounts.Accounts(
    account_number=654321,
    account_firstname="John",
    account_lastname="Doe",
    current_balance=2000,
    address="Gold Street Quezon City",
    email="johndoe@yahoo.com"
)
'''
print("Account 1")
print("First Name:", Account1.account_firstname)
print("Last Name:", Account1.account_lastname)
print("Balance:", Account1.current_balance)
print("Address:", Account1.address)
print("Email:", Account1.email)
print()

print("Account 2")
print("First Name:", Account2.account_firstname)
print("Last Name:", Account2.account_lastname)
print("Balance:", Account2.current_balance)
print("Address:", Account2.address)
print("Email:", Account2.email)
print()
'''

ATM1 = ATM.ATM(serial_number=919191)
ATM1.deposit(Account1, 500)
print("Account 1 balance after deposit:", Account1.current_balance)
ATM1.check_current_balance(Account1)
ATM1.withdraw(Account1, 100)
print("Account 1 balance after withdrawal:", Account1.current_balance)
ATM1.check_current_balance(Account1)
print("ATM Serial Number:", ATM1.serial_number)

print()
ATM1.view_transaction_summary()
print()






#original code
'''
Account1 = Accounts.Accounts()

print("Account 1")
Account1.account_firstname = "Royce"
Account1.account_lastname = "Chua"
Account1.current_balance = 1000
Account1.address = "Silver Street Quezon City"
Account1.email = "roycechua123@gmail.com"

print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)

print()

Account2 = Accounts.Accounts()
Account2.account_firstname = "John" 
Account2.account_lastname = "Doe"
Account2.current_balance = 2000
Account2.address = "Gold Street Quezon City"
Account2.email = "johndoe@yahoo.com"

print("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname) 
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)

ATM1 = ATM.ATM()
ATM1.deposit(Account1, 500)
ATM1.check_currentbalance(Account2)
'''
