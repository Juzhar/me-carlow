# -*- coding: utf-8 -*-
"""
HW1
"""
# Q6

import pandas as pd
df = pd.read_csv("poke.csv")
valid_pokemon = False
user_pokemon = input('Enter the name of a pokemon: ')
for index, row in df.iterrows():
    if row['identifier'] == user_pokemon:
        user_id = row['id']
        valid_pokemon = True
        
if(valid_pokemon == False):
    print('NOT A POKEMON')
else:
    with open("q6_out.txt", "w") as file:
        file.write(str(user_id))
        file.write('\n')
        file.write(user_pokemon)