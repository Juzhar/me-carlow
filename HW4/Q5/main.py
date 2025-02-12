# -*- coding: utf-8 -*-
"""
HW4
"""
# Q5

import pandas as pd
df = pd.read_csv("../Data/poke.csv")
user_input = input("Select a letter or set of letters: ")
x = df[df["identifier"].str.startswith(user_input.lower())]
strongest = x[x['base_experience'] == x['base_experience'].max()]
with open("q5.out", "w") as file:
    file.write(strongest.to_string())

