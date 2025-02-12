# -*- coding: utf-8 -*-
"""
HW4
"""
# Q9

import pandas as pd
poke = pd.read_csv("../Data/poke.csv")
encounters = pd.read_csv("../Data/encounters.csv")
locations = pd.read_csv("../Data/locations.csv")
locations_area = pd.read_csv("../Data/location_areas.csv")
top_locations = pd.DataFrame(columns=['id', 'region', 'identifier'])
location_count = pd.DataFrame(columns=['location_area_id', 'count'])
top_areas = encounters["location_area_id"].value_counts()[:5].index.tolist()
top_ids = []
for area in top_areas:
    for index, row in locations_area.iterrows():
        if row['id'] == area:
            top_ids.append(row['location_id'])
for location in top_ids:
    for index, row in locations.iterrows():
        if row['id'] == location:
            top_locations.loc[len(top_locations)] = row
with open("q9.out", "w") as file:
    file.write("The locations with the most pokemon are: \n")
    file.write(top_locations.to_string())

