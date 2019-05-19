# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 19:08:25 2017

@author: dell
"""
from database import accountlist as items
def accounting():    
    amount=0
    while 1: 
        entry = int(input("Enter the account number (1 for entire list,0 to exit) : "))
        if entry==0:
                break
        elif entry==1:
             for key in items.keys():
                 print (' {}   {}   {}'.format(key,items[key][0],items[key][1]))
        elif entry in items.keys() :
             print ('Name: {}   Balance : {} '.format(items[entry][0],items[entry][1]))
             withdrawal=int(input("\n Enter amount to be withdrawn : "))
             if withdrawal<=items[entry][1]:
                 items[entry][1]=items[entry][1]-withdrawal
                 amount+=items[entry][1]
                 break
             else:
                 print("Amount Available is only  = ",items[entry][1])
        else:
             print(' account does not exists ')
    print ("\n\n Your remaining balance is : ",amount)                 