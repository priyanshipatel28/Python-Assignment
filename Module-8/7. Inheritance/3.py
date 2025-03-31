# #multiple
# A class Bank has an attribute bank_name and a method show_bank_name().
# A class Customer has an attribute customer_name and a method show_customer_name().
# A class Account inherits from both Bank and Customer and has an attribute account_number with a method show_account_details() to display the account details.

class Bank:
    def __init__(self,bank_name):
        self.bank_name = bank_name
    def show_bank_name(self):
        return f"the bank name is {self.bank_name}"

class customer:
    def __init__(self,customer_name):
        self.customer_name = customer_name
    def show_customer_name(self):
        return f"the cuatoemr name is {self.customer_name}"
    
class Account(Bank,customer):
    def __init__(self, bank_name,customer_name,account_number):
        Bank.__init__(self,bank_name)
        customer.__init__(self,customer_name)
        self.account_number = account_number

    def show_account_details(self):
        print(self.show_bank_name())
        print(self.show_customer_name())

a = Account("BOI","Diya patel",13456123)
a.show_account_details()