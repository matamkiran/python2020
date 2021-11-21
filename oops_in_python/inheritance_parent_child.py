
class Parent:
    bank_bal=100000
    __gold="40kg"
    def driveCar(self):
        print("owns honda city")
    def showGold(self):
        print("my gold balance is :",self.__gold)
    
class Child(Parent):
    pocket_bal=100
    def rideBicycle(self):
        print("only bicycle i have, not a car")
    
pobj=Parent()
cobj=Child()

cobj.rideBicycle()
print(cobj.bank_bal)
cobj.driveCar()
pobj.showGold()

