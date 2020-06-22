# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 09:13:21 2020

@author: Account
"""


LoginDetails={"renuka":"mypasswd12!",
              "arya":"aryapasswd58*",
              "shreyas":"shreyasRocks",
              "vedang":"vedStudious"}

username=input("Enter your UserName: ")
paswd=input("Enter Password: ")

if username in LoginDetails.keys():
    
    if LoginDetails[username]==paswd:
        print("Authenticated!!")
    else:
        print("Invalid Password!!")
        
else:
    print("Invalid Username!!")
