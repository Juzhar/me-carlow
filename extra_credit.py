
# -*- coding: utf-8 -*-
"""
HW1
"""
# Extra credit: Need more cave
import random as rnd
from tabulate import tabulate
cave_X = int(input("How long shall this cave be? "))
cave_Y = int(input('How wide shall this cave be? '))
success = False
moves = 0


grid = []
for j in range(cave_Y):
    fillerList = []
    for i in range(cave_X):
        fillerList.append('')
    grid.append(fillerList)
player_X = rnd.randint(0, cave_X - 1)
player_Y = rnd.randint(0, cave_Y - 1) 
win_X = player_X
win_Y = player_Y
while win_X == player_X:
    win_X = rnd.randint(0, cave_X - 1)
while win_Y == player_Y:
    win_Y = rnd.randint(0, cave_Y - 1) 
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
        if player_Y < cave_Y - 1:
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
        if player_X < cave_X - 1:
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