# -*- coding: utf-8 -*-
"""
HW6
"""
# Q5

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
poke = pd.read_csv("../Data/pokemon.csv")
growth = pd.read_csv("../Data/pokemon_species.csv")
exp = pd.read_csv("../Data/experience.csv")
pokemon1_found = False
pokemon2_found = False
poke1_exp_list = []
poke2_exp_list = []
levels = list(range(1, 101))
while pokemon1_found == False:
    pokemon1 = input("Enter a pokemon: ")
    if poke['identifier'].isin([pokemon1]).any():
        pokemon1_found = True
    else: 
        print("Invalid pokemon")
while pokemon2_found == False:
    pokemon2 = input("Enter a second pokemon: ")
    if poke['identifier'].isin([pokemon2]).any():
        if (pokemon2 != pokemon1):
            pokemon2_found = True
        else:
            print("Must be a different pokemon")
    else: 
        print("Invalid pokemon")
ids = ['height','weight', 'base_experience']
sns.set(font_scale = .75)
plt.subplot(3, 3, 1)
poke1 = poke[poke.identifier.isin([pokemon1])]
pokedata1 = poke1[["height","weight","base_experience"]]
for index, row in pokedata1.iterrows():
    strength1 = 5*row['height']+2*row['weight']+row['base_experience']
pokedata1 = pokedata1.rename(columns={'base_experience': 'base exp'})
data1 = {'Stats': pokedata1.columns.to_list(),'Values': pokedata1.iloc[0].to_list()}
sns.barplot(x='Stats',y='Values',legend='brief', data = data1)
plt.xticks(rotation=45)
plt.title(pokemon1)
plt.subplot(3,3,3)
poke2 = poke[poke.identifier.isin([pokemon2])]
pokedata2 = poke2[["height","weight","base_experience"]]
pokedata2 = pokedata2.rename(columns={'base_experience': 'base exp'})
for index, row in pokedata2.iterrows():
    strength2 = 5*row['height']+2*row['weight']+row['base exp']
data2 = {'Stats': pokedata2.columns.to_list(),'Values': pokedata2.iloc[0].to_list()}
sns.barplot(x='Stats',y='Values' ,legend='brief', data = data2)
plt.xticks(rotation=45)
plt.title(pokemon2)
poke1_growth = growth[growth.identifier.isin([pokemon1])]
poke1_exp = exp[exp.growth_rate_id.isin([poke1_growth.iloc[0]['growth_rate_id']])]
for index, row in poke1_exp.iterrows():
    poke1_exp_list.append(row['experience'])
data3 = {'Level': levels,'Experience': poke1_exp_list}
plt.subplot(3, 3, 7)
sns.lineplot(data=data3,x='Level',y='Experience', legend='brief')
plt.ticklabel_format(style='plain', axis='y')
poke2_growth = growth[growth.identifier.isin([pokemon2])]
poke2_exp = exp[exp.growth_rate_id.isin([poke2_growth.iloc[0]['growth_rate_id']])]
for index, row in poke2_exp.iterrows():
    poke2_exp_list.append(row['experience'])
data4 = {'Level': levels,'Experience': poke2_exp_list}
plt.subplot(3, 3, 9)
sns.lineplot(data=data4,x='Level',y='Experience', legend='brief')
plt.ticklabel_format(style='plain', axis='y')
plt.subplot(3, 3, 5)
avg_poke1 = sum(poke1_exp_list) / len(poke1_exp_list)
poke1value = avg_poke1 + strength1
avg_poke2 = sum(poke1_exp_list) / len(poke1_exp_list)
poke2value = avg_poke2 + strength2
empty_df = pd.DataFrame({'x': [], 'y': []})
if poke1value > poke2value:
    sns.barplot(x='x', y='y', data=empty_df)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.title(pokemon1)
else:
    sns.barplot(x='x', y='y', data=empty_df)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.title(pokemon2)