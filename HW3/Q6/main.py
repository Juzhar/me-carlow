# -*- coding: utf-8 -*-
"""
HW3
"""
# Q6

import pandas as pd
df = pd.read_csv("../Data/poke.csv")
num_rows = len(df)
num_cols = len(df.columns)
col_names = df.columns
col_names = col_names.tolist()
print("The pokemon dataset consts of " + str(num_cols) + " columns and " + str(num_rows) + " rows. It has the following column names " + str(col_names) + ".")

