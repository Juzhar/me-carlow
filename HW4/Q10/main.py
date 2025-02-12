# -*- coding: utf-8 -*-
"""
HW4
"""
# Q10

import pandas as pd
poke = pd.read_csv("../Data/poke.csv")
encounters = pd.read_csv("../Data/encounters.csv")
locations = pd.read_csv("../Data/locations.csv")
locations_area = pd.read_csv("../Data/location_areas.csv")
top_locations = pd.DataFrame(columns=['id', 'region', 'identifier'])
location_count = pd.DataFrame(columns=['location_area_id', 'count'])
top_pokemon_id = encounters["pokemon_id"].value_counts()[:1].index.tolist()
bottom_pokemon_id = [encounters["pokemon_id"].value_counts().index[-1].tolist(), encounters["pokemon_id"].value_counts().index[-2].tolist(), encounters["pokemon_id"].value_counts().index[-3].tolist(), encounters["pokemon_id"].value_counts().index[-4].tolist()]
top_pokemon = pd.DataFrame(columns=['id', 'identifier', 'species_id', 'height', 'weight', 'base_experience', 'order', 'is_default'])
bottom_pokemon = pd.DataFrame(columns=['id', 'identifier', 'species_id', 'height', 'weight', 'base_experience', 'order', 'is_default'])
for pokemon in top_pokemon_id:
    for index, row in poke.iterrows():
        if row['id'] == pokemon:
            top_pokemon.loc[len(top_pokemon)] = row
for pokemon in bottom_pokemon_id:
    for index, row in poke.iterrows():
        if row['id'] == pokemon:
            bottom_pokemon.loc[len(bottom_pokemon)] = row
with open("q10.out", "w") as file:
    file.write("The pokemon that appear in the most amount of locations are: \n")
    file.write(top_pokemon.to_string())
    file.write("\nThe pokemon that appear in the least amount of locations are: \n")
    file.write(bottom_pokemon.to_string())

