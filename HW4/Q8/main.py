# -*- coding: utf-8 -*-
"""
HW4
"""
# Q8

import pandas as pd
df = pd.read_csv("../Data/poke.csv")
no_fire_df = pd.DataFrame(columns=['id', 'identifier', 'species_id', 'height', 'weight', 'base_experience', 'order', 'is_default'])
types = pd.read_csv("../Data/types.csv")
poketypes = pd.read_csv("../Data/pokemon_types.csv")
fire_index = types.loc[types['identifier'] == 'fire', 'id'].iloc[0]
fire_ids = []
for index, row in poketypes.iterrows():
    if row['type_id'] == fire_index:
        fire_ids.append(row['pokemon_id'])
for index, row in df.iterrows():
    if row['id'] not in fire_ids:
        no_fire_df.loc[len(no_fire_df)] = row
with open("q8.out", "w") as file:
    file.write(str(no_fire_df['id'].count()))