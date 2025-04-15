# -*- coding: utf-8 -*-
"""
HW10
"""
# Q2

import sqlite3
import pandas as pd

db_path = "poke.db"
sql_path = "../Q1/Q1.sql"
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    with open(sql_path, 'r') as sql_file:
        script = sql_file.read()
    c.executescript(script)
    conn.commit()
    conn.close()
except sqlite3.OperationalError as e:
    print("unable to connect to database", e)
poke = pd.read_csv("pokemon.csv")
for index, row in poke.iterrows():
    poke_id = row['id']
    poke_name = row['identifier']
    poke_height = row['height']
    poke_weight = row['weight']
    poke_base_exp = row['base_experience']
    add_pokemon = "INSERT INTO pokemon (id, name, height, weight, base_experience) VALUES (" + str(poke_id) + ", '" + str(poke_name) + "', " + str(poke_height) + ", " + str(poke_weight) + ", " + str(poke_base_exp) + ")" 
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(add_pokemon)
    conn.commit()
    conn.close()