# -*- coding: utf-8 -*-
"""
HW4
"""
# Q4

import pandas as pd
df = pd.read_csv("../Data/poke.csv")
p = df[df["identifier"].str.startswith("p")]
strongest = p[p['base_experience'] == p['base_experience'].max()]
with open("q4.out", "w") as file:
    file.write(strongest.to_string())