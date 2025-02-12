# -*- coding: utf-8 -*-
"""
HW4
"""
# Q6

import pandas as pd
poke = pd.read_csv("../Data/poke.csv")
types = pd.read_csv("../Data/types.csv")
typeidlist = []
typenamelist = []
poke_id = None
poketypes = pd.read_csv("../Data/pokemon_types.csv")
user_pokemon = input('Enter a pokemon: ')
string_list = []
if user_pokemon in poke.values:
    poke_id = poke.loc[poke['identifier'] == user_pokemon, 'id'].iloc[0]
else:
    print('NOT A POKEMON')
for index, row in poketypes.iterrows():
    if row['pokemon_id'] == poke_id:
        typeidlist.append(row['type_id'])
for index, row in types.iterrows():
    for item in typeidlist:
        if row['id'] == item:
            typenamelist.append(row['identifier'])
for element in typeidlist:
    count = 0
    for index, row in poketypes.iterrows():
        if (row['type_id'] == element):
            count += 1
    x = poketypes[poketypes["type_id"] == element]
    x_pokemon = x['pokemon_id']
    y = pd.DataFrame(columns=['id', 'identifier', 'species_id', 'height', 'weight', 'base_experience', 'order', 'is_default'])
    for index, row in poke.iterrows():
        if row['id'] in x_pokemon.values:
            y.loc[len(y)] = row
    strongest = y.loc[y['base_experience'] == y['base_experience'].max(), 'identifier'].values.tolist()
    weakest = y.loc[y['base_experience'] == y['base_experience'].min(), 'identifier'].values.tolist()
    string_list.append(str(user_pokemon) + " is a " + str(typenamelist[typeidlist.index(element)]) + " type.\n" 
                       + "There are " + str(count) + " different " + str(typenamelist[typeidlist.index(element)]) + " types.\n"
                       + "The strongest pokemon of this type are: " + str(strongest) + "\n"
                       + "The weakest pokemon of this type are: " + str(weakest)+ "\n")
with open("q6.out", "w") as file:
    for string in string_list:
        file.write(string)
    
    
    
