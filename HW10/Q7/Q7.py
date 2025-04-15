# -*- coding: utf-8 -*-
"""
HW10
"""
# Q7

import sqlite3
import pandas as pd

db_path = "poke.db"
p = pd.read_csv("pokemon.csv")
t = pd.read_csv("pokemon_types.csv")
pt = p.merge(t,how="left",left_on="id",right_on="pokemon_id")
pt = pt.drop(['species_id', 'is_default', "order", "slot", 'pokemon_id'], axis=1)
pt = pt.rename(columns={'identifier': 'name'})
pt = pt.drop_duplicates(subset=['id'])
for index, row in pt.iterrows():
    poke_id = row['id']
    poke_name = row['name']
    poke_height = row['height']
    poke_weight = row['weight']
    poke_base_exp = row['base_experience']
    poke_type = row['type_id']
    add_pokemon = "INSERT INTO pokemon (id, name, height, weight, base_experience, type_id) VALUES (" + str(poke_id) + ", '" + str(poke_name) + "', " + str(poke_height) + ", " + str(poke_weight) + ", " + str(poke_base_exp) + ", " + str(poke_type) + ")" 
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(add_pokemon)
    conn.commit()
    conn.close()