# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 07:52:32 2021

@author: matam
"""

def password_check(func):
    def wrapper_check():
        print("check valid password")
        func()
    return wrapper_check


def check_balance(func):
    balance=5000
    def wrapper_check(*args):
        if(args[0]<balance):
            print("you cannot this action with amount less than 1000")
        else:
            func(args)
    return wrapper_check

@password_check
def withdraw():
    print("amount is withdrawn")

@check_balance
def withdraw_amount(amt):
    print(amt,"has been debited from your account")
    
@check_balance
def book_fd(amt):
    print(amt,"fd is done")


withdraw()
withdraw_amount(500)
book_fd(500)