# -*- coding: utf-8 -*-
"""
HW5
"""
# Q8

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pokemon = pd.read_csv("../Data/pokemon.csv")
species = pd.read_csv("../Data/pokemon_species.csv")
special_pokemon = pd.DataFrame(columns = ['id', 'identifier', 'generation_id', 'evolves_from_species_id', 'evolution_chain_id', 'shape_id', 'habitat_id', 'gender_rate', 'capture_rate', 'base_happiness', 'is_baby', 'hatch_counter', 'has_gender_differences', 'growth_rate_id', 'forms_switchable', 'is_legendary', 'is_mythical', 'order', 'conquest_order'])
for index, row in species.iterrows():
    if(row['is_legendary'] == 1):
        special_pokemon.loc[len(special_pokemon)] = row
    elif(row['is_mythical'] == 1):
        special_pokemon.loc[len(special_pokemon)] = row
    else:
        pass
ps = special_pokemon.merge(pokemon,how="left",left_on="id",right_on="id")
def strength(row):
     strength = (row['base_experience'] * 5) + ((row['base_experience'] + row['base_experience']) * 5)
     return strength
ps['strength'] = ps.apply(lambda row: strength(row), axis=1)
df_sorted = ps.sort_values(by='strength', ascending=False)
with open("q8.out", "w") as file:
    file.write(df_sorted.head(5).to_string())
b = sns.barplot(data=df_sorted.head(5), x = 'identifier_x', y = 'strength', palette = 'deep')
plt.ylabel("Strength")
plt.xlabel("Pokemon name")
plt.title("Strongest mythical and legendary pokemon", fontsize = 20, fontweight = 'bold')
plt.xticks(rotation=45, horizontalalignment='right')
plt.show()
