# -*- coding: utf-8 -*-
"""
HW1
"""
# Q7

import pandas as pd
data = pd.read_csv("../Data/poke.csv")
df = data['identifier']
print("Build your pokemon team below!")
end = False
pokelist = []
while end == False:
    if (len(pokelist) < 6):
        print("1. Enter pokemon \n2. Exit")
        user_input = input("Input here: ")
        if (user_input == '2'):
            end = True
        elif user_input == '1':
            pokemon = input("Pokemon: ")
            if pokemon in df.values:
                pokelist.append(pokemon)
            else:
                print('NOT A POKEMON')
                continue
    else:
        print('Max team members reached')
        end = True
with open("q7_out.txt", "w") as file:
    for item in pokelist:
        file.write(item)
        file.write('\n')