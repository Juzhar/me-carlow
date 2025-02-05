# -*- coding: utf-8 -*-
"""
HW3
"""
# Q7

import pandas as pd
df = pd.read_csv("../Data/poke.csv")
valid_pokemon = False
user_pokemon = input('Enter the name of a pokemon: ')
for index, row in df.iterrows():
    if row['identifier'] == user_pokemon:
        user_id = row['id']
        valid_pokemon = True
        
if(valid_pokemon == False):
    print('NOT A POKEMON')
else:
    df_pokemon = df[df.identifier==user_pokemon]
    print(df_pokemon)