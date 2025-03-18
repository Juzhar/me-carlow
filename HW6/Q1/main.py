# -*- coding: utf-8 -*-
"""
HW6
"""
# Q1

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("../Data/pokemon.csv")
types = pd.read_csv("../Data/types.csv")
poketypes = pd.read_csv("../Data/pokemon_types.csv")
first = []
tt = poketypes.merge(types,how="left",left_on="type_id",right_on="id")
pt = df.merge(tt,how="left",left_on="id",right_on="pokemon_id")
frequency = pt['identifier_y'].value_counts()
df_frequency = pd.DataFrame(frequency)
df_frequency = df_frequency.reset_index()
df_frequency.columns = ['Pokemon Type', 'Pokemon Count']
chart = df_frequency.plot(kind="bar", x = 'Pokemon Type', y = 'Pokemon Count')
plt.title("Number of pokemon for each pokemon type")
plt.show()