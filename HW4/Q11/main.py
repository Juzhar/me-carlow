# -*- coding: utf-8 -*-
"""
HW4
"""
# Q11

import pandas as pd
df = pd.read_csv("../Data/poke.csv")
df = df.drop_duplicates()
special_poke = []
for index, row in df.iterrows():
    if "-" in row['identifier']:
        special_poke.append(row['identifier'])
with open("q11.out", "w") as file:
    for pokemon in special_poke:
        file.write(pokemon)
        file.write('\n')

        
        
