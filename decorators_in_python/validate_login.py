# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 13:44:07 2021

@author: matam
"""

def validate(param):
    def nested(*args,**kwrgs):
        if(len(args[1])<8):
           print("password should be greaater than 8 characters")
           print("bye! please try again")
        else:
            param(*args)
            print("logged in successfully")
    return nested
    

@validate    
def login(username,password):
    print("welcome",username)
    
login("king","123")
