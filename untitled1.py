# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:09:33 2020

@author: Account
"""

Imfo = {"Shreyas": "sxjo0909" , 
        "Giriraj" : "gkj150906" , 
        "Prafullata":"pgj433"}

userName= input("Enter Username :")
password= input("Enter Password :")

if userName== Imfo.keys():
    
    if password== Imfo[userName]:
        print("Correct")
    else:
        print("Invalid Password")
        
else:
    print("Invalid Username")
