# -*- coding: utf-8 -*-
"""
HW4
"""
# Q7

import pandas as pd
df = pd.read_csv("../Data/poke.csv")
modified_df = pd.DataFrame(columns=['id', 'identifier', 'species_id', 'height', 'weight', 'base_experience', 'order', 'is_default'])
for index, row in df.iterrows():
    if(row['height'] > 100):
        new_row = [row['id'], row['identifier'].upper(), row['species_id'], row['height'], row['weight'], row['base_experience'], row['order'], row['is_default']]
        modified_df.loc[len(modified_df)] = new_row
    elif(row['height'] < 50):
        new_row = [row['id'], row['identifier'].lower(), row['species_id'], row['height'], row['weight'], row['base_experience'], row['order'], row['is_default']]
        modified_df.loc[len(modified_df)] = new_row
    elif(row['height'] > 50 and row['height'] < 60):
        new_row = [row['id'], row['identifier'].title(), row['species_id'], row['height'], row['weight'], row['base_experience'], row['order'], row['is_default']]
        modified_df.loc[len(modified_df)] = new_row
    else:
        new_row = [row['id'], row['identifier'], row['species_id'], row['height'], row['weight'], row['base_experience'], row['order'], row['is_default']]
        modified_df.loc[len(modified_df)] = new_row
modified_df = modified_df.sort_values(by='id', ascending=True)
with open("q7.out", "w") as file:
    file.write(modified_df.to_string())