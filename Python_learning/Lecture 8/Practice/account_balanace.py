class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amt):
        
        self.balance-=amt
        print("Debited Successfully.")

    def credit(self,amt):
        
        self.balance+=amt
        print("Credited Successfully.")

    def val(self):
        print("Balance is",self.balance)

a1=Account(8000,90)
a1.val()
a1.credit(5000)
a1.val()
a1.debit(4500)
a1.val()
