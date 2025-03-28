#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:43:35 2025

@author: ashcash

You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you, the user, will say whether it is too high, 
too low, or your number. At the end of this exchange, your program 
should print out how many guesses it took to get your number.
"""

user_numer=int(input("Choose a number: "))
import random as r
num = r.randint(0,100)
print(num)
user=input("Is this the correct number?")
c=0
while user == 'No':
    c+=1
    level=input("Is the number too high or too low?")
    if level == 'Too High':
        num=r.randint(0,num-1)
        print(num)
        user=input("Is this the correct number?")
    elif level == 'Too Low':
        num=r.randint(num+1,100)
        print(num)
        user=input("Is this the correct number?")
if user == 'Yes':
    print("Game Finished" + " Number of Guesses: "+ str(c))