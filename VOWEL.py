# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:12:38 2020

@author: Account
"""
name = input("Enter the Name :").lower()

VowelFound = ['','','','','']
count=0

if 'a' in name :
    VowelFound[count]='a'
    count=count+1
    
if 'e' in name :
    VowelFound[count]='e'
    count=count+1
    
if 'i' in name :
    VowelFound[count]='i'
    count=count+1
    
if 'o' in name :
    VowelFound[count]='o'
    count=count+1
    
if 'u' in name :
    VowelFound[count]='u'
    count=count+1     
print("The Vowels in the the name "+ name + " are " + str(VowelFound))
