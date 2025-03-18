# -*- coding: utf-8 -*-
"""
HW6
"""
# Q4

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
poke = pd.read_csv("../Data/pokemon.csv")
poketypes = pd.read_csv("../Data/pokemon_types.csv")
pokespecies = pd.read_csv("../Data/pokemon_species.csv")
types = pd.read_csv("../Data/types.csv")
exp = pd.read_csv("../Data/experience.csv")
pt = poketypes.merge(types,how="left",left_on="type_id",right_on="id")
pt = pt[["pokemon_id","type_id","identifier"]]
ppt = poke.merge(pt,how="left",left_on="id",right_on="pokemon_id")
ppt = ppt[["id", "height", "weight", "base_experience", "type_id","identifier_y"]]
ppgt = ppt.merge(pokespecies,how="left",left_on="id",right_on="id")
ppgt = ppgt[["id", "height", "weight", "base_experience", "type_id","identifier_y", "growth_rate_id"]]
average_values = []
min_values = []
max_values = []
count = []
ppgt = ppgt[ppgt.identifier_y.isin(['fire'])]
df = ppgt.dropna()
for i in range (1, 101):
    strength_list = []
    exp_row = exp[exp.level.isin([i])]
    for index, row in df.iterrows():
        height = row['height']
        weight = row['weight']
        base_exp = row['base_experience']
        growth_rate = row["growth_rate_id"]
        exp_poke = exp_row[exp_row.growth_rate_id.isin([growth_rate])]
        added_exp = 0
        for index, row in exp_poke.iterrows():
            added_exp = row['experience']
            pass
        strength = 5*height+2*weight+base_exp+added_exp
        strength_list.append(strength)
    count.append(i)
    average = sum(strength_list) / len(strength_list)
    average_values.append(round(average))
    min_values.append(min(strength_list))
    max_values.append(max(strength_list))
strength_df = pd.DataFrame({'average': average_values, 'minimum': min_values, 'maximum': max_values, 'Level': count})
ids=['average','minimum', 'maximum']
for i in ids:
    (sns.lineplot(data=strength_df,x='Level',y=i, legend='brief',label=str(i)))
plt.ylabel("Strength")
plt.ticklabel_format(style='plain', axis='y')
plt.title("Strength values of fire pokemon based on level")
plt.show()




    
    