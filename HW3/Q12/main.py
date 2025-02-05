# -*- coding: utf-8 -*-
"""
HW3
"""
# Q12

import pandas as pd
pokemon_data = pd.read_csv("../Data/poke.csv")
locations = pd.read_csv("../Data/locations.csv")
regions = pd.read_csv("../Data/regions.csv")
region_id = None
location_list = []
df = pokemon_data['identifier']
df2 = regions['identifier']
print("Hello Ash!")
end = False
while end == False:
    print("1. Search by name \n2. Search by region \n3. Exit")
    user_input = input("Input here: ")
    if (user_input == '3'):
        end = True
    elif user_input == '1':
        pokemon = input("What pokemon are you looking for? ")
        if pokemon in df.values:
            pokemon_dataframe = pokemon_data[pokemon_data.identifier==pokemon]
            print(pokemon_dataframe)
        else:
            print('NOT A POKEMON')
            input('Hit enter to continue')
            continue
    elif user_input == '2':
        location_list = []
        region = input("What region are you looking for? ")
        if (region in df2.values) == False:
            print('NOT A REGION')
            input('Hit enter to continue')
            continue
        else:
            for index, row in regions.iterrows():
                if region == row['identifier']:
                    region_id = row['id']
            for index, row in locations.iterrows():
                if pd.isna(row['region_id']):
                    pass
                else:   
                    if row['region_id'] == region_id:
                        location_list.append(row['identifier'])
            print('Here are some locations in the ' + str(region) + ' region')
            print(location_list)
        
        