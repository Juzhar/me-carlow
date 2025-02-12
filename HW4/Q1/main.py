# -*- coding: utf-8 -*-
"""
HW4
"""
# Q1

import pandas as pd
df = pd.read_csv("../Data/locations.csv")
null_df = pd.DataFrame(columns=['id', 'region_id', 'identifier'])
for index, row in df.iterrows():
    if pd.isna(row['region_id']):
        null_df.loc[len(null_df)] = row
with open("q1.out", "w") as file:
    file.write(null_df.to_string())
        
        