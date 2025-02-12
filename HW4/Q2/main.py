# -*- coding: utf-8 -*-
"""
HW4
"""
# Q2

import pandas as pd
l = pd.read_csv("../Data/locations.csv")
r = pd.read_csv("../Data/regions.csv")
l = l.fillna(999)
r.loc[len(r)] = [999, "carlow"]
with open("q2a.out", "w") as file:
    file.write(l.to_string())
with open("q2b.out", "w") as file:
    file.write(r.to_string())