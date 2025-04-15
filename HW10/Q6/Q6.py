# -*- coding: utf-8 -*-
"""
HW10
"""
# Q6

import sqlite3
import pandas as pd

db_path = "poke.db"
sql_path = "Q6.sql"
with open(sql_path, 'r') as sql_file:
    script = sql_file.read()
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("PRAGMA foreign_keys = 1")
c.executescript(script)
conn.commit()
conn.close()
poketypes = pd.read_csv("pokemon_type_names.csv")
for index, row in poketypes.iterrows():
    if(row['local_language_id']==9):
        type_id = row['type_id']
        type_name = row['name']
        add_type = "INSERT INTO pokemon_types (id, name) VALUES (" + str(type_id) + ", '" + str(type_name) + "')"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(add_type)
        conn.commit()
        conn.close()