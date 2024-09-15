#modified code
class Accounts():
    def __init__(self, account_number, account_firstname, account_lastname, current_balance, address, email):
        self.account_number = account_number
        self.account_firstname = account_firstname
        self.account_lastname = account_lastname
        self.current_balance = current_balance
        self.address = address
        self.email = email

    def update_address(self, address):
        self.address = new_address

    def update_email(self, new_email):
        self.email = new_email

#original code
'''
class Accounts():
    account_number = 0
    account_firstname = ""
    account_lastname = ""
    account_balance = 0.0
    address = ""
    email = ""

    def update_address(self,new_address):
        Accounts.address = new_address

    def update_email(self,new_email):
        Accounts.email = new_email
'''
