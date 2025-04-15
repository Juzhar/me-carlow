# -*- coding: utf-8 -*-
"""
HW10
"""
# Q10

import sqlite3

db_path = "poke.db"
sql_path = "Q10.sql"
with open(sql_path, 'r') as sql_file:
    script = sql_file.read()
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.executescript(script)
conn.commit()
conn.close()
success = False

print("Hello! Please enter the details of your pokemon below.")
poke_id = input("ID: ")
poke_name = input("Name: ")
poke_height = input("Height: ")
poke_weight = input("Weight: ")
poke_base_exp = input("Base experience: ")
poke_type = input("Type ID: ")
add_pokemon = "INSERT INTO pokemon (id, name, height, weight, base_experience, type_id) VALUES (" + str(poke_id) + ", '" + str(poke_name) + "', " + str(poke_height) + ", " + str(poke_weight) + ", " + str(poke_base_exp) + ", " + str(poke_type) + ")" 
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(add_pokemon)
    conn.commit()
    conn.close()
    success = True
except Exception as e:
    success = False
    print("Pokemon could not be added")
    print(e)
if success == True:
    print("Your pokemon was added successfully")
