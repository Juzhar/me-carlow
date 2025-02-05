# -*- coding: utf-8 -*-
"""
HW3
"""
# Q8

import pandas as pd
df = pd.read_csv("../Data/poke.csv")
user_input = input("Please provide a number: ")
if (user_input.isnumeric()):
    df_pokemon = df[df.id==int(user_input)]
    print(df_pokemon)
else:
    print("Error")
    exit()
