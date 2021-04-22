def myfunction(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    
myfunction(firstname="ajay",secondname=[10,20,20])