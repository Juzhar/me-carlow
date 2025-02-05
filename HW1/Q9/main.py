# -*- coding: utf-8 -*-
"""
HW1
"""
# Q9
import pandas as pd
data = pd.read_csv("../Data/poke.csv")
data2 = pd.read_csv('../Data/locations.csv')
df = data['identifier']
print("Build your pokemon team below!")
end = False
pokelist = []
pokeidlist = []
locationlist = []
while end == False:
    print("1. Add pokemon \n2. List team \n3. Drop member \n4. Exit")
    user_input = input("Input here: ")
    if (user_input == '4'):
        end = True
    elif user_input == '1':
        if (len(pokelist) < 6):
            pokemon = input("Pokemon: ")
            if pokemon in df.values:
                pokelist.append(pokemon)
                print(pokemon + ' was added successfully')
                input('Hit enter to continue')
            else:
                print('NOT A POKEMON')
                input('Hit enter to continue')
                continue
        else:
            print('Max team members reached')
            input('Hit enter to continue')
            continue
    elif user_input == '3':
        if (len(pokelist) > 0):
            pokemon = input("Dropped pokemon: ")
            if pokemon in pokelist:
                pokelist.remove(pokemon)
                print(pokemon + " was removed successfully")
                input('Hit enter to continue')
            else:
                print("POKEMON NOT IN LIST")
                input('Hit enter to continue')
    elif user_input == '2':
        for i in range(len(pokelist)):
            number = i + 1
            print (str(number) + '. ' + pokelist[i])
        input('Hit enter to continue')
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
with open("q9_out.txt", "w") as file:
    for i in range(len(pokelist)):
        file.write("ID:" + str(pokeidlist[i]) + " Name:")
        file.write(pokelist[i]+ " Location:")
        file.write(str(locationlist[i]))
        file.write('\n')


