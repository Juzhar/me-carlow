# -*- coding: utf-8 -*-
"""
HW6
"""
# Q2

import pandas as pd
import matplotlib.pyplot as plt
type_found = False
p = pd.read_csv("../Data/pokemon_types.csv")
pokemon = pd.read_csv("../Data/pokemon_species.csv")
poketypes = pd.read_csv("../Data/pokemon_types.csv")
types = pd.read_csv("../Data/types.csv")
gen = pd.read_csv("../Data/generations.csv")
pt = poketypes.merge(types,how="left",left_on="type_id",right_on="id")
while type_found == False:
    user_type = input("Please input a pokemon type: ")
    if types['identifier'].isin([user_type]).any():
        type_found = True
    else: 
        print("Invalid type")
pt = pt[pt.identifier.isin([user_type])]
pt = pt[["pokemon_id","type_id","identifier"]]
ppt = pt.merge(pokemon,how="left",left_on="pokemon_id",right_on="id")
ppt = ppt[["pokemon_id","type_id","identifier_x", "generation_id"]]
gppt = ppt.merge(gen,how="left",left_on="generation_id",right_on="id")
frequency = gppt['identifier'].value_counts()
df_frequency = pd.DataFrame(frequency)
df_frequency = df_frequency.reset_index()
df_frequency.columns = ['generation', 'pokemon count']
chart = df_frequency.plot(kind="bar", x = 'generation', y = 'pokemon count')
plt.xticks(rotation=45)
plt.title("Number of " + str(user_type) + " pokemon for every generation.")
plt.show()