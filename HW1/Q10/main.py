# -*- coding: utf-8 -*-
"""
HW1
"""
# Q10
import random as rnd
from tabulate import tabulate
success = False
moves = 0
grid = [['', '', '', ''], 
        ['', '', '', '']]

player_X = rnd.randint(0, 3)
player_Y = rnd.randint(0, 1) 
win_X = player_X
win_Y = player_Y
while win_X == player_X:
    win_X = rnd.randint(0, 3)
while win_Y == player_Y:
    win_Y = rnd.randint(0, 1) 
grid[player_Y][player_X] = 'X'
print(tabulate(grid, tablefmt="grid"))
print('Welcome to the dungeon!')
while success == False:
    print('Enter w for up, s for down, d for right, and a for left, or q if you want to exit early')
    player_input = input('Your move: ')
    if player_input == 'w':
        if player_Y > 0:
            moves += 1
            grid[player_Y][player_X] = ''
            player_Y -= 1
            grid[player_Y][player_X] = 'X'
            print(tabulate(grid, tablefmt="grid"))
        else:
            print("NOT A VALID MOVE")
            input("Hit enter to continue")
            print(tabulate(grid, tablefmt="grid"))
    elif player_input == 's':
        if player_Y < 1:
            moves += 1
            grid[player_Y][player_X] = ''
            player_Y += 1
            grid[player_Y][player_X] = 'X'
            print(tabulate(grid, tablefmt="grid"))
        else:
            print("NOT A VALID MOVE")
            input("Hit enter to continue")
            print(tabulate(grid, tablefmt="grid"))
    elif player_input == 'd':
        if player_X < 3:
            moves += 1
            grid[player_Y][player_X] = ''
            player_X += 1
            grid[player_Y][player_X] = 'X'
            print(tabulate(grid, tablefmt="grid"))
        else:
            print("NOT A VALID MOVE")
            input("Hit enter to continue")
            print(tabulate(grid, tablefmt="grid"))
    elif player_input == 'a':
        if player_X > 0:
            moves += 1
            grid[player_Y][player_X] = ''
            player_X -= 1
            grid[player_Y][player_X] = 'X'
            print(tabulate(grid, tablefmt="grid"))
        else:
            print("NOT A VALID MOVE")
            input("Hit enter to continue")
            print(tabulate(grid, tablefmt="grid"))
    elif player_input == 'q':
        break
    if (player_X == win_X and player_Y == win_Y):
        success = True
if success == True:
    print('Congratulations you made it out!')
    print('Moves: ' + str(moves))
else:
    print('Better luck next time!')