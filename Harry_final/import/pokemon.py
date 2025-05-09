# -*- coding: utf-8 -*-
"""
Final Project
"""
#Initialize Pokemon Table
import sqlite3
import pandas as pd

db_path = "../teambattle.db"
sql_path = "../sql/pokemon.sql"
df = pd.read_csv("../data/pokemon.csv")
with open(sql_path, 'r') as sql_file:
    script = sql_file.read()
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.executescript(script)
conn.commit()
conn.close()
for index, row in df.iterrows():
    poke_id = row['id']
    poke_name = row['identifier']
    poke_height = row['height']
    poke_weight = row['weight']
    poke_base_exp = row['base_experience']
    add_pokemon = "INSERT INTO pokemon (ID, Name, Height, Weight, Experience) VALUES (" + str(poke_id) + ", '" + str(poke_name) + "', " + str(poke_height) + ", " + str(poke_weight) + ", " + str(poke_base_exp) + ")" 
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(add_pokemon)
    conn.commit()
    conn.close()