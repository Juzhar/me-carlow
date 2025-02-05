# -*- coding: utf-8 -*-
"""
HW3
"""
# Q11

import pandas as pd
df = pd.read_csv("../Data/locations.csv")
null_locations = []
for index, row in df.iterrows():
    if pd.isna(row['region_id']):
        null_locations.append(row['identifier'])
print(null_locations)
        
        
        
