
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
    
   

c=Parent()   #object creation 
print(c.city)
print(c.gold) 

