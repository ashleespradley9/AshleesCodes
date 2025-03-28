#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:35:49 2025

@author: ashcash

Created a fun game of Rock Paper Scissors
"""

game = input("Want to play Rock Paper Scissors? ")

while game == "Yes":

    player_1 = input("Rock Paper Scissors?")
    player_2 = input("Rock Paper Scissors?")
    
    if player_1 == player_2:
        print('Tie')
        game = input('Want to play again?')
    elif player_1 == 'Rock' and player_2 == 'Paper':
        print('Player 2 wins!')
        game = input('Want to play again? ')
    elif player_1 == 'Rock' and player_2 == 'Scissors':
        print('Player 1 wins!')
        game = input('Want to play again? ')
    elif player_1 == 'Paper' and player_2 == 'Scissors':
        print('Player 2 wins!')
        game = input('Want to play again? ')
    elif player_1 == 'Paper' and player_2 == 'Rock':
        print('Player 1 wins!')
        game = input('Want to play again? ')
    elif player_1 == 'Scissors' and player_2 == 'Rock':
        print('Player 2 wins!')
        game = input('Want to play again? ')
    elif player_1 == 'Scissors' and player_2 == 'Paper':
        print('Player 1 wins!')
        game = input('Want to play again? ')
    else:
        print("invalid entry")
        game = input('Want to play again? ')