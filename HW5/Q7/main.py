# -*- coding: utf-8 -*-
"""
HW5
"""
# Q7

import pandas as pd
species = pd.read_csv("../Data/pokemon_species.csv")
special_pokemon = []
for index, row in species.iterrows():
    if(row['is_legendary'] == 1):
        special_pokemon.append(row['identifier'])
    elif(row['is_mythical'] == 1):
        special_pokemon.append(row['identifier'])
    else:
        pass
with open("q7.out", "w") as file:
    for pokemon in special_pokemon:
        file.write(pokemon)
        file.write("\n")