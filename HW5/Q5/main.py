# -*- coding: utf-8 -*-
"""
HW5
"""
# Q5

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("../Data/pokemon.csv")
types = pd.read_csv("../Data/types.csv")
poketypes = pd.read_csv("../Data/pokemon_types.csv")
first = []
tt = poketypes.merge(types,how="left",left_on="type_id",right_on="id")
pt = df.merge(tt,how="left",left_on="id",right_on="pokemon_id")
with open("q5.out", "w") as file:
    file.write(pt.to_string())
def type_color(row):  
    if row['identifier_y'] == 'normal':
        return 'darkgoldenrod'
    elif row['identifier_y'] == 'fighting':
        return 'darkorange'
    elif row['identifier_y'] == 'flying':
        return 'lightcyan'
    elif row['identifier_y'] == 'poison':
        return 'mediumvioletred'
    elif row['identifier_y'] == 'ground':
        return 'saddlebrown'
    elif row['identifier_y'] == 'rock':
        return 'dimgrey'
    elif row['identifier_y'] == 'bug':
        return 'olivedrab'
    elif row['identifier_y'] == 'ghost':
        return 'darkorchid'
    elif row['identifier_y'] == 'steel':
        return 'silver'
    elif row['identifier_y'] == 'fire':
        return 'red'
    elif row['identifier_y'] == 'water':
        return 'blue'
    elif row['identifier_y'] == 'grass':
        return 'green'
    elif row['identifier_y'] == 'electric':
        return 'yellow'
    elif row['identifier_y'] == 'psychic':
        return 'rosybrown'
    elif row['identifier_y'] == 'ice':
        return 'skyblue'
    elif row['identifier_y'] == 'dragon':
        return 'honeydew'
    elif row['identifier_y'] == 'dark':
        return 'black'
    elif row['identifier_y'] == 'fairy':
        return 'pink'
    elif row['identifier_y'] == 'stellar':
        return 'white'
    elif row['identifier_y'] == 'unknown':
        return 'maroon'
    elif row['identifier_y'] == 'shadow':
        return 'navy'
for index, row in pt.iterrows():
    if row['pokemon_id'] in first:
        pt = pt.drop(index)
    else:
        first.append(row['pokemon_id'])
frequency = pt['identifier_y'].value_counts()
df_frequency = pd.DataFrame(frequency)
df_frequency = df_frequency.reset_index()
df_frequency.columns = ['identifier_y', 'count']
pt['type_color'] = pt.apply(lambda row: type_color(row), axis=1)
with open("q5.out", "w") as file:
    file.write(pt.to_string())
df_frequency['type_color'] = df_frequency.apply(lambda row: type_color(row), axis=1)
color_list = df_frequency['type_color'].to_list()
b = sns.barplot(data=df_frequency, x = 'identifier_y', y = 'count', palette = color_list, edgecolor='black', linewidth=1)
plt.ylabel("Number of Pokemon")
plt.xlabel("Type Name")
plt.title("Number of pokemon for every type", fontsize = 20, fontweight = 'bold')
plt.xticks(rotation=45, horizontalalignment='right')
plt.show()




