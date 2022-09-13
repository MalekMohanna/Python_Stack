class User:
    def  __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance+=amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance-=amount
        return self
    def make_transfer(self,user,amount):
        self.make_withdrawal(amount)
        user.make_deposit(amount)
        return self
    def print_info(self):
        print(self.name,self.account_balance)
        return self

karam=User("Karam Taha","karam@gmail.com")
malik=User("Malik Mohanna","malik@gmail.com")
ahmad=User("Ahmad Taha","ahmad@gmail.com")

malik.make_deposit(2320).make_deposit(420).make_withdrawal(500).make_withdrawal(670).make_transfer(karam,600).print_info()
karam.make_deposit(150).make_deposit(1500).make_deposit(120).make_withdrawal(1000).print_info()
ahmad.make_deposit(1330).make_withdrawal(124).make_withdrawal(325).make_withdrawal(345).print_info()

