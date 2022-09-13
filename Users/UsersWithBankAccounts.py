class User:
    def  __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = BankAccount(int_rate=.02,balance=0)
    def deposit(self,amount):
        self.account_balance.make_deposit(amount)

    def withdrawal(self,amount):
        self.account_balance.make_withdrawal(amount)

    def info(self):
        print(self.name)
        self.account_balance.display_account_info()
    def update_interes(self,int_rate):
        self.account_balance.update_the_interes(int_rate)

    

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
        return 
    def update_the_interes(self,int_rate):
        self.interest=int_rate

malek=User("malek","malek@gmail.com")
malek.update_interes(0.05)
malek.deposit(10000)
malek.withdrawal(3000)
malek.info()