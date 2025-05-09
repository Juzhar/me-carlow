# -*- coding: utf-8 -*-
"""
Final Project
"""
#Initialize Trainer Table

import sqlite3

db_path = "../teambattle.db"
sql_path = "../sql/trainer.sql"
with open(sql_path, 'r') as sql_file:
    script = sql_file.read()
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.executescript(script)
conn.commit()
conn.close()
