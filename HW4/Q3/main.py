# -*- coding: utf-8 -*-
"""
HW4
"""
# Q3

import pandas as pd
df = pd.read_csv("../Data/poke.csv")
a = df[df["identifier"].str.startswith("a")]
e = df[df["identifier"].str.startswith("e")]
i = df[df["identifier"].str.startswith("i")]
o = df[df["identifier"].str.startswith("o")]
u = df[df["identifier"].str.startswith("u")]
vowels = pd.concat([a, e, i, o, u], axis=0)
with open("q3.out", "w") as file:
    file.write(vowels.to_string())
