# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 07:43:07 2021

@author: matam
"""

class Bank:
    accountNum=91123456443
    
    def __locker(self):
        print("placed all your valuble things")
    #mangling
    def showMyBankDetails(self):
        self.__locker()
        
bank=Bank()

bank.showMyBankDetails()

    
    
