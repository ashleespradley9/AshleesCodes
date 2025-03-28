#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:38:48 2025

@author: ashcash

Python Code for guess the number
"""

import random as rand

#print("Welcome to guess the number! ")
game = input("Do you want to play a game?: ")
rn = rand.randint(1, 9)
#print(rn)

while game == "Yes":
    user_guess = int(input("Guess the computer number: "))
    if user_guess > rn:
        print("Guess is too high")
        game = input("Do you want to guess again? Yes or Exit: ")
    elif user_guess < rn:
        print("Guess is too low")
        game = input("Do you want to guess again? Yes or Exit: ")
    else:
        print("You guess right!")
        break