# -*- coding: utf-8 -*-
"""
HW5
"""
# Q4

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random as rnd
pokemon = pd.read_csv("../Data/pokemon.csv")
species = pd.read_csv("../Data/pokemon_species.csv")
colors = pd.read_csv("../Data/pokemon_colors.csv")
ps = pokemon.merge(species,how="left",left_on="id",right_on="id")
psc = ps.merge(colors,how="left",left_on="color_id",right_on="id")
dropped_cols = ['species_id', 'height', 'weight', 'order_x', 'is_default', 'identifier_y', 'generation_id', 'evolves_from_species_id', 'evolution_chain_id', 'shape_id', 'habitat_id', 'gender_rate', 'capture_rate', 'base_happiness', 'is_baby', 'hatch_counter', 'has_gender_differences', 'growth_rate_id', 'forms_switchable', 'is_legendary', 'is_mythical', 'order_y', 'conquest_order', 'id_y']
psc_dropped = psc.drop(columns = dropped_cols)
rand_poke = pd.DataFrame(columns=['id_x', 'identifier_x',  'base_experience',  'color_id', 'identifier'])
with open("q4.out", "w") as file:
    file.write(psc_dropped.to_string())
rand_ints = []
for i in range(10):
    number = rnd.randint(1, 1026)
    rand_ints.append(number)
for number in rand_ints:
    for index, row in psc_dropped.iterrows():
        if index == number:
            rand_poke.loc[len(rand_poke)] = row
color_list = rand_poke['identifier'].to_list()
b = sns.barplot(data=rand_poke, x = 'identifier_x', y = 'base_experience', palette = color_list, edgecolor='black', linewidth=1)
plt.ylabel("Base Experience")
plt.xlabel("Pokemon Name")
plt.title("Base experience of 10 random pokemon", fontsize = 20, fontweight = 'bold')
plt.xticks(rotation=45, horizontalalignment='right')
plt.show()
