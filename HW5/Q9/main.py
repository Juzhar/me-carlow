# -*- coding: utf-8 -*-
"""
HW4
"""
# Q9

import pandas as pd
import random as rnd
from tabulate import tabulate
success = False
team_made = False
location_selected = False
region_selected = False
fail = False
moves = 0
grid = [['', '', '', ''], 
        ['', '', '', ''],
        ['', '', '', ''], 
        ['', '', '', ''],]
coords = [[0,0], [1,0], [2,0], [3,0], [0,1], [1,1], [2,1], [3,1], [0,2], [1,2], [2,2], [3,2], [0,3], [1,3], [2,3], [3,3]]
team = pd.DataFrame(columns = ['poke_id', 'poke_identifier', 'species_id', 'height', 'weight', 'base_experience', 'order', 'is_default'])
player_X = rnd.randint(0, 3)
player_Y = rnd.randint(0, 3) 
player_coords = [player_X, player_Y]
win_X = player_X
win_Y = player_Y
while win_X == player_X:
    win_X = rnd.randint(0, 3)
while win_Y == player_Y:
    win_Y = rnd.randint(0, 3) 
win_coords = [win_X, win_Y]
poke = pd.read_csv("../Data/pokemon.csv")
species = pd.read_csv("../Data/pokemon_species.csv")
poke = poke.rename(columns={'id': 'poke_id'})
poke = poke.rename(columns={'identifier': 'poke_identifier'})
encounters = pd.read_csv("../Data/encounters.csv")
locations = pd.read_csv("../Data/locations.csv")
locations_area = pd.read_csv("../Data/location_areas.csv")
regions = pd.read_csv("../Data/regions.csv")
generations = pd.read_csv("../Data/generations.csv")
local = locations_area.merge(locations,how="left",left_on="location_id",right_on="id")
el = encounters.merge(local,how="left",left_on="location_area_id",right_on="id_x")
pel = poke.merge(el,how="left",left_on="poke_id",right_on="pokemon_id")
enemy_poke = pd.DataFrame(columns=['id', 'identifier', 'base_experience'])
gr = generations.merge(regions,how="left",left_on="main_region_id",right_on="id")
pgr = species.merge(gr,how="left",left_on="generation_id",right_on="id_x")
ppgr = poke.merge(pgr,how="left",left_on="poke_id",right_on="id")
grid[player_Y][player_X] = 'X'
start_len = 0
poke_name = ''
for coord in coords:
    if coord == player_coords or coord == win_coords:
        coords.remove(coord)
def check_position(coords):
    global enemy_poke
    global team
    for index, row in enemy_poke.iterrows():
        if coords == row['coords']:
            first_row = team.iloc[0]
            print("Your " + str(first_row['poke_identifier']) + " encountered a " + str(row[poke_name]))
            if first_row['base_experience'] > row['base_experience']:
                print(str(first_row['poke_identifier']) + " defeated the " + str(row[poke_name]) + "!")
                enemy_poke = enemy_poke.drop(index)
            else:
                print(str(first_row['poke_identifier']) + " was defeated...")
                enemy_poke = enemy_poke.drop(index)
                team = team.drop(index = start_len - len(team))
print('Welcome to the dungeon!')
while team_made == False:
    print('Build your pokemon team!')
    print('Please select what you would like to do')
    print("1. Add pokemon \n2. Generate random team \n3. Delete pokemon \n4. Proceed forward ")
    user_input = int(input("Input here: "))
    if user_input == 1:
        pokemon_found = False
        pokemon = input("Enter the name of the pokemon you want to add: ")
        for index, row in poke.iterrows():
            if pokemon == row['poke_identifier']:
                pokemon_found = True
                team.loc[len(team)] = row
                print(str(pokemon) + " was added successfully")
                input('Hit enter to continue')
        if pokemon_found == True:
            pass
        else:
            print('NOT A VALID POKEMON')
            input('Hit enter to continue')
    elif user_input == 2:
        rand_ints = []
        team.drop(team.index, inplace=True)
        for i in range(6):
            number = rnd.randint(1, 1305)
            if number not in rand_ints:
                rand_ints.append(number)
        for number in rand_ints:
            for index, row in poke.iterrows():
                if index == number:
                    team.loc[len(team)] = row
        print('Team successfully generated')
        input('Hit enter to continue')
    elif user_input == 3:
        member_found = False
        pokemon = input("Enter the name of the pokemon you want to remove: ")
        for index, row in team.iterrows():
            if pokemon == row['poke_identifier']:
                team = team.drop(index)
                member_found = True
                print(str(pokemon) + " was removed successfully")
                input('Hit enter to continue')
        if member_found == True:
            pass
        else:
            print('NOT A TEAM MEMBER')
            input('Hit enter to continue')
    elif user_input == 4:
        start_len = len(team)
        team_made = True
    else:
        print('NOT A VALID OPTION')
        input('Hit enter to continue')
while location_selected == False and region_selected == False:
    print('Select if you want to input a region or a location')
    lorr = int(input("1. Region \n2. Location \nInput here: "))
    if lorr == 1:
        region = input("Please select a region: ")
        filtered_ppgr = ppgr[ppgr['identifier_y'] ==  region]
        enemy_poke = filtered_ppgr.sample(n=14)
        poke_name = "identifier"
        region_selected = True
    elif lorr == 2:
        location = input("Please select a location: ")
        new_location = location.replace(" ", "-")
        filtered_pel = pel[pel['identifier_y'] == new_location]
        enemy_poke = filtered_pel.sample(n=14)
        poke_name = "poke_identifier"
        location_selected = True
    enemy_poke['coords'] = coords
    print(enemy_poke)
print(tabulate(grid, tablefmt="grid"))
while success == False:
    print('Enter w for up, s for down, d for right, and a for left, or q if you want to exit early')
    player_input = input('Your move: ')
    if player_input == 'w':
        if player_Y > 0:
            moves += 1
            grid[player_Y][player_X] = ''
            player_Y -= 1
            player_coords = [player_X, player_Y]
            grid[player_Y][player_X] = 'X'
            print(tabulate(grid, tablefmt="grid"))
            check_position(player_coords)
        else:
            print("NOT A VALID MOVE")
            input("Hit enter to continue")
            print(tabulate(grid, tablefmt="grid"))
    elif player_input == 's':
        if player_Y < 3:
            moves += 1
            grid[player_Y][player_X] = ''
            player_Y += 1
            player_coords = [player_X, player_Y]
            grid[player_Y][player_X] = 'X'
            print(tabulate(grid, tablefmt="grid"))
            check_position(player_coords)
        else:
            print("NOT A VALID MOVE")
            input("Hit enter to continue")
            print(tabulate(grid, tablefmt="grid"))
    elif player_input == 'd':
        if player_X < 3:
            moves += 1
            grid[player_Y][player_X] = ''
            player_X += 1
            player_coords = [player_X, player_Y]
            grid[player_Y][player_X] = 'X'
            print(tabulate(grid, tablefmt="grid"))
            check_position(player_coords)
        else:
            print("NOT A VALID MOVE")
            input("Hit enter to continue")
            print(tabulate(grid, tablefmt="grid"))
    elif player_input == 'a':
        if player_X > 0:
            moves += 1
            grid[player_Y][player_X] = ''
            player_X -= 1
            player_coords = [player_X, player_Y]
            grid[player_Y][player_X] = 'X'
            print(tabulate(grid, tablefmt="grid"))
            check_position(player_coords)
        else:
            print("NOT A VALID MOVE")
            input("Hit enter to continue")
            print(tabulate(grid, tablefmt="grid"))
    elif player_input == 'q':
        break
    if (player_X == win_X and player_Y == win_Y):
        success = True
    if len(team) == 0:
        print("You couldn't make it out :(")
        break
if success == True:
    print('Congratulations you made it out!')
    print('Moves: ' + str(moves))
else:
    print('Better luck next time!')
with open("status.out", "w") as file:
    if success == True:
        file.write('Success')
        file.write('\n')
        file.write(str(len(team)))
    else:
        file.write('Failure')
