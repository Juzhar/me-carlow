# -*- coding: utf-8 -*-
"""
HW5
"""
# Q6

import pandas as pd
types = pd.read_csv("../Data/types.csv")
first = []
poketypes = pd.read_csv("../Data/pokemon_types.csv")
secondary = None
for index, row in poketypes.iterrows():
    if row['pokemon_id'] not in first:
        first.append(row['pokemon_id'])
        poketypes = poketypes.drop(index)
frequency = poketypes['type_id'].value_counts()
df_frequency = pd.DataFrame(frequency)
df_frequency = df_frequency.reset_index()
df_frequency.columns = ['type_id', 'count']
for index, row in types.iterrows():
    if df_frequency['type_id'].tolist()[0] == row['id']:
        secondary = row['identifier']
with open("q6.out", "w") as file:
    file.write("The most common secondary type is " + str(secondary))

    
