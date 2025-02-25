# -*- coding: utf-8 -*-
"""
HW5
"""
# Q1

import pandas as pd
p = pd.read_csv("../Data/pokemon_species.csv")
g = pd.read_csv("../Data/generations.csv")
pg = p.merge(g,how="left",left_on="generation_id",right_on="id")
with open("q1.out", "w") as file:
    file.write(pg.to_string())
pg_filtered = pd.DataFrame(columns=['Pokemon_name', 'Generation_ID'])
for index, row in pg.iterrows():
    new_row = [row['identifier_x'], row['generation_id']]
    pg_filtered.loc[len(pg_filtered)] = new_row
pg_filtered.to_csv('q1.csv')