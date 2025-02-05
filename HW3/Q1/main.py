# -*- coding: utf-8 -*-
"""
HW3
"""
# Q1

import pandas as pd
scores = [('Bryan', 82), ('Alicia', 75), ('Gary', 87), ('Derrek', 86)
, ('Rachel', 79), ('Eugene', 0), ('Lucy', 98), ('Juan', 66), ('Henry', 68), ('Travis', 92)]
df = pd.DataFrame(scores, columns =['Name', 'Score'])
print(df['Name'])

