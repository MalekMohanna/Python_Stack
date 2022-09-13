class BankAccount:
    def __init__(self,int_rate=.02 ,balance=0):
        self.account_balance=balance
        self.interest=int_rate
    
    def make_deposit(self,amount):
        self.account_balance+=amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance-=amount
        return self

    def display_account_info(self):
        print(self.account_balance,self.interest)
        return self

    def yield_interest(self):
        if (self.account_balance*self.interest) > 0:
            self.account_balance+=(self.account_balance*self.interest)
        return self

Malek=BankAccount(.07,10000)
Ahmad=BankAccount(.04,25000)

Malek.make_deposit(200).make_deposit(300).make_deposit(500).make_withdrawal(500).yield_interest().display_account_info()
Ahmad.make_deposit(500).make_deposit(1000).make_withdrawal(250).make_withdrawal(500).make_withdrawal(250).make_withdrawal(1000).yield_interest().display_account_info()
