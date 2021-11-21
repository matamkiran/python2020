class Atm:
    balance=100000
    def __init__(self,name):
        print("Hello ,",name," Welcome to PYTHONIC ATM")
        
    def withdraw(self,amount):
        print("your balance after withdraw",self.balance-amount )
        
        
obj=Atm("Chirag")

       