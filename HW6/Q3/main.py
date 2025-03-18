# -*- coding: utf-8 -*-
"""
HW6
"""
# Q3

import pandas as pd
import matplotlib.pyplot as plt
poke = pd.read_csv("../Data/pokemon.csv")
poketypes = pd.read_csv("../Data/pokemon_types.csv")
pokegens = pd.read_csv("../Data/pokemon_species.csv")
types = pd.read_csv("../Data/types.csv")
pt = poketypes.merge(types,how="left",left_on="type_id",right_on="id")
pt = pt[["pokemon_id","type_id","identifier"]]
ppt = poke.merge(pt,how="left",left_on="id",right_on="pokemon_id")
ppt = ppt[["id", "height", "weight", "base_experience", "type_id","identifier_y"]]
ppgt = ppt.merge(pokegens,how="left",left_on="id",right_on="id")
ppgt = ppgt[["id", "height", "weight", "base_experience", "type_id","identifier_y", "generation_id"]]
average_values = []
average_count = []
type_found = False
while type_found == False:
    user_type = input("Please input a pokemon type: ")
    if types['identifier'].isin([user_type]).any():
        type_found = True
    else: 
        print("Invalid type")
ppgt = ppgt[ppgt.identifier_y.isin([user_type])]
def calculate_strength(row):
    strength = 5*row['height']+2*row['weight']+row['base_experience']
    return strength
ppgt['strength'] = ppgt.apply(lambda row: calculate_strength(row), axis=1)
gens_df = ppgt[["generation_id","strength"]]
for i in range (1, 10):
     gen_df = gens_df[gens_df.generation_id.isin([i])]
     average_values.append(gen_df['strength'].mean())
     average_count.append(i)
strength_df = pd.DataFrame({'strength': average_values, 'Generation': average_count})
strength_df.plot(x = 'Generation', y = 'strength', kind = 'line')
plt.title('Average strength of ' + str(user_type) + " type pokemon by generation")
plt.show()



    
    