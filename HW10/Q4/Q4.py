# -*- coding: utf-8 -*-
"""
HW10
"""
# Q4

import sqlite3
import pandas as pd

poketypes = pd.read_csv("pokemon_type_names.csv")
poketypes = poketypes[poketypes['local_language_id'] == 9]
poketypes = poketypes.drop('local_language_id', axis=1)
poketypes = poketypes.rename(columns={'type_id': 'id'})
c = sqlite3.connect("poke.db")
poketypes.to_sql(name="pokemon_types", con=c)