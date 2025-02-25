# -*- coding: utf-8 -*-
"""
HW5
"""
# Q2

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random as rnd
df = pd.read_csv("../Data/pokemon.csv")
end = False
print('Welcome to pokemon team maker')
team = pd.DataFrame(columns = ['id', 'identifier', 'species_id', 'height', 'weight', 'base_experience', 'order', 'is_default'])
while end == False:
    print('Please select what you would like to do')
    print("1. Add pokemon \n2. Generate random team \n3. Delete pokemon \n4. Exit ")
    user_input = int(input("Input here: "))
    if user_input == 1:
        pokemon_found = False
        pokemon = input("Enter the name of the pokemon you want to add: ")
        for index, row in df.iterrows():
            if pokemon == row['identifier']:
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
            for index, row in df.iterrows():
                if index == number:
                    team.loc[len(team)] = row
        print('Team successfully generated')
        input('Hit enter to continue')
    elif user_input == 3:
        member_found = False
        pokemon = input("Enter the name of the pokemon you want to remove: ")
        for index, row in team.iterrows():
            if pokemon == row['identifier']:
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
        end = True
    else:
        print('NOT A VALID OPTION')
        input('Hit enter to continue')
b = sns.barplot(data=team, x = 'identifier', y = 'base_experience', palette = 'deep')
plt.ylabel("Base Experience")
plt.xlabel("Name")
plt.title("Base experience for each pokemon in your team", fontsize = 20, fontweight = 'bold')
plt.xticks(rotation=45, horizontalalignment='right')
plt.show()
