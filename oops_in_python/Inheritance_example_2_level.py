class GrandParent:
    land="100acres"
    city="bangalore"
    _gold=50
    
class Parent(GrandParent):  #inheritance
    land="50acres"
    city="mysore"           #overridden(polymorphism)
    apartment="sunrise"

class Child(Parent):
    bike="KTM"
    city="mumbai"
    gold=100
    
    def fetchTotalgold(self):
          gold=self.gold+Parent.gold
          return gold

c=Child()   #object creation 
print(c.city)
print(c.gold)

p=GrandParent()
print(p.city)

print(c.fetchTotalgold())
