# -*- coding: utf-8 -*-
"""
HW4
"""
# Q12

import pandas as pd
df = pd.read_csv("../Data/poke.csv")
modified_df = pd.DataFrame(columns=['id', 'identifier', 'species_id', 'height', 'weight', 'base_experience', 'order', 'is_default'])
for index, row in df.iterrows():
    if "-" in row['identifier']:
        new_identifier = row['identifier'].replace("-", " ")
        new_row = [row['id'], new_identifier.title(), row['species_id'], row['height'], row['weight'], row['base_experience'], row['order'], row['is_default']]
        modified_df.loc[len(modified_df)] = new_row
    else:
        new_row = [row['id'], row['identifier'].title(), row['species_id'], row['height'], row['weight'], row['base_experience'], row['order'], row['is_default']]
        modified_df.loc[len(modified_df)] = new_row
with open("q12.out", "w") as file:
    file.write(modified_df.to_string())