# -*- coding: utf-8 -*-
"""
HW1
"""
# Q8
import pandas as pd
data = pd.read_csv("poke.csv")
data2 = pd.read_csv('locations.csv')
df = data['identifier']
print("Build your pokemon team below!")
end = False
pokelist = []
pokeidlist = []
locationlist = []
while end == False:
    if (len(pokelist) < 6):
        print("1. Enter pokemon \n2. Exit")
        user_input = input("Input here: ")
        if (user_input == '2'):
            end = True
        elif user_input == '1':
            pokemon = input("Pokemon: ")
            if pokemon in df.values:
                pokelist.append(pokemon)
            else:
                print('NOT A POKEMON')
                continue
    else:
        print('Max team members reached')
        end = True
for pokemon in pokelist:
    for index, row in data.iterrows():
        if row['identifier'] == pokemon:
            pokeidlist.append(row['id'])
for pokeid in pokeidlist:
    localfound = False
    for index, row in data2.iterrows():
        if row['pokemon_id'] == pokeid:
            locationlist.append(row['location_area_id'])
            localfound = True
    if localfound == False:
        locationlist.append('None')
with open("q8_out.txt", "w") as file:
    for i in range(len(pokelist)):
        file.write("ID:" + str(pokeidlist[i]) + " Name:")
        file.write(pokelist[i]+ " Location:")
        file.write(str(locationlist[i]))
        file.write('\n')

