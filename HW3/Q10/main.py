# -*- coding: utf-8 -*-
"""
HW3
"""
# Q9

import pandas as pd
locations = pd.read_csv("../Data/locations.csv")
regions = pd.read_csv("../Data/regions.csv")
region_id = None
location_number = 0
user_region = input('Which region would you like to know about? ')
region_valid = False
for index, row in regions.iterrows():
    if row['identifier'] == user_region:
        region_id = row['id']
        print(region_id)
        region_valid = True
if region_valid == False:
    print("Region does not exist.")
else:
    for index, row in locations.iterrows():
        if row['region_id'] == region_id:
            location_number += 1
    print(str(user_region) + " has " + str(location_number) + " locations.")
