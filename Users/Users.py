class User:
    def  __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance+=amount
    def make_withdrawal(self,amount):
        self.account_balance-=amount
    def make_transfer(self,user,amount):
        self.make_withdrawal(amount)
        user.make_deposit(amount)

karam=User("Karam Taha","karam@gmail.com")
malik=User("Malik Mohanna","malik@gmail.com")
ahmad=User("Ahmad Taha","ahmad@gmail.com")

karam.make_deposit(150)
karam.make_deposit(1500)
karam.make_deposit(120)
karam.make_withdrawal(1000)
malik.make_deposit(2320)
malik.make_deposit(420)
malik.make_withdrawal(500)
malik.make_withdrawal(670)
ahmad.make_deposit(1330)
ahmad.make_withdrawal(124)
ahmad.make_withdrawal(325)
ahmad.make_withdrawal(345)
malik.make_transfer(karam,300)

print(karam.name,karam.account_balance)
print(malik.name,malik.account_balance)
print(ahmad.name,ahmad.account_balance)
