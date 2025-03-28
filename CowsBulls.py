#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:41:32 2025

@author: ashcash

Python code for cows and bulls

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place,
they have a “cow”. For every digit the user guessed correctly 
in the wrong place is a “bull.” Every time the user makes a guess, 
tell them how many “cows” and “bulls” they have. Once the user guesses 
the correct number, the game is over. Keep track of the number of 
guesses the user makes throughout teh game and tell the user at the end.
"""

def cowsbulls(userguess):
    import random as r
    num = r.randint(1000,9999)
    while num != userguess:
        cows = 0
        bulls = 0
        sep = [int(i) for i in str(num)]
        user_guess_sep = [int(j) for j in str(userguess)]
        for i in range(0,4):
            if sep[i]==user_guess_sep[i]:
                cows+=1
            elif sep[i]!=user_guess_sep[i]:
                bulls+=1
        print(str(cows)+" cows and "+str(bulls)+ " bulls")
        userguess = int(input("Guess again: "))
    while num == userguess:
        return "Congratualtions you won!"