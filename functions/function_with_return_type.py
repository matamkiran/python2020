# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 07:39:49 2021

@author: matam
"""

balance=10000
account_id=12345

amount=int(input("Enter your amount to withdraw"))


def withdrawAmount(amount):
    if(amount>balance):
        return "sorry you cant withdraw"
    else:
        bal=(balance-amount)
        return "Success! your balance left is :" + str(bal)

print(withdrawAmount(amount))