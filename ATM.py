#modified code
class ATM:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.transactions = [] 

    def deposit(self, account, amount):
        account.current_balance += amount
        transaction = f"Deposit: ₱{amount} to Account {account.account_number}"
        self.transactions.append(transaction)
        print("Deposit Complete")

    def withdraw(self, account, amount):
        if amount > account.current_balance:
            print("Insufficient funds")
            transaction = f"Failed Withdrawal: ₱{amount} from Account {account.account_number} (Insufficient funds)"
        else:
            account.current_balance -= amount
            transaction = f"Withdrawal: ₱{amount} from Account {account.account_number}"
        self.transactions.append(transaction)
        print("Withdraw Complete")

    def check_current_balance(self, account):
        print("Current Balance:", account.current_balance)

    def view_transaction_summary(self):
        print("Transaction Summary:")
        if not self.transactions:
            print("No transactions have been made.")
        for transaction in self.transactions:
            print(transaction)

#original code
'''
class ATM():
    serial_numer = 0

    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        print("Deposit Complete")

    def withdraw(self, account, amount):
        account.current_balance = account_balance - amount
        print("Withddraw Complete")

    def check_currentbalance(self, account):
        print(account.current_balance)
'''