# -*- coding: utf-8 -*-
"""
HW3
"""
# Q9

import pandas as pd
data = pd.read_csv("../Data/poke.csv")
df = data['identifier']
print("Build your pokemon team below!")
end = False
pokelist = []
pokeidlist = []
while end == False:
    print("1. Add to team \n2. List team \n3. Drop from team \n4. Exit")
    user_input = input("Input here: ")
    if (user_input == '4'):
        end = True
    elif user_input == '1':
        if (len(pokelist) < 6):
            pokemon = input("What pokemon would you like to add? ")
            if pokemon in df.values:
                pokelist.append(pokemon)
                print(pokemon + ' was added successfully')
                input('Hit enter to continue')
            else:
                print('NOT A POKEMON')
                input('Hit enter to continue')
                continue
        else:
            print('Too many pokemon')
            input('Hit enter to continue')
            continue
    elif user_input == '3':
        if (len(pokelist) > 0):
            pokemon = input("Dropped pokemon: ")
            if pokemon in pokelist:
                pokelist.remove(pokemon)
                print(pokemon + " was removed successfully")
                input('Hit enter to continue')
            else:
                print("POKEMON NOT IN LIST")
                input('Hit enter to continue')
    elif user_input == '2':
        for i in range(len(pokelist)):
            df_pokemon = data[data.identifier==pokelist[i]]
            print(df_pokemon)
        input('Hit enter to continue')
