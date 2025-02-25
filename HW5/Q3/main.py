# -*- coding: utf-8 -*-
"""
HW5
"""
# Q3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("../Data/pokemon_species.csv")
gen = pd.read_csv("../Data/generations.csv")
reg =  pd.read_csv("../Data/regions.csv")
for index, row in reg.iterrows():
    new_row = [row['id'], row['identifier'].title()]
    reg.loc[index] = new_row
gr = gen.merge(reg,how="left",left_on="main_region_id",right_on="id")
a = df.merge(gr,how="left",left_on="generation_id",right_on="id_x")
frequency = a['identifier_y'].value_counts()
df_frequency = pd.DataFrame(frequency)
df_frequency = df_frequency.reset_index()
df_frequency.columns = ['Regions', 'Count']
b = sns.barplot(data=df_frequency, x = 'Regions', y = 'Count', palette = 'deep')
plt.ylabel("Number of Pokemon")
plt.xlabel("Region Name")
plt.title("Number of pokemon in each region", fontsize = 20, fontweight = 'bold')
plt.xticks(rotation=45, horizontalalignment='right')
plt.show()
