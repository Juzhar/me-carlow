# -*- coding: utf-8 -*-
"""
HW4
"""
# Q13

import pandas as pd
df = pd.read_csv("../Data/poke.csv")
end = False
print('Welcome to the dataset changer!')
while end == False:
    print('Please select what you would like to do')
    print("1. Manage dataset \n2. Exit")
    user_input1 = int(input("Input here: "))
    if user_input1 == 1:
        print('What would you like to do to the dataset?')
        print("1. Add Pokemon \n2. Delete Pokemon \n3. Update pokemon")
        user_input2 = int(input("Input here: "))
        if user_input2 == 1:
            new_id = int(input("What do you want the new pokemon's ID to be? "))
            new_identifier = input("What do you want the new pokemon's name to be? ")
            new_species_id = int(input("What should " + str(new_identifier)+ "'s species id be? "))
            new_height = int(input("What should " + str(new_identifier)+ "'s height be? "))
            new_weight = int(input("What should " + str(new_identifier)+ "'s weight be? "))
            new_base_experience = int(input("What should " + str(new_identifier)+ "'s base experience be? "))
            new_order = int(input("What should " + str(new_identifier)+ "'s order be? "))
            print("Should "+ str(new_identifier)+ " be a default pokemon?")
            print("1. Yes \n2. No")
            new_is_default = int(input("Input here: "))
            if new_is_default == 2:
                new_is_default = 0
            new_row = [new_id, new_identifier, new_species_id, new_height, new_weight, new_base_experience, new_order, new_is_default]
            df.loc[len(df)] = new_row
            print(str(new_identifier) + " has been added successfully")
            input('Hit enter to continue')
        elif user_input2 == 2:
            pokemon_found = False
            poke_id = int(input("Enter the ID of the pokemon you want to remove: "))
            for index, row in df.iterrows():
                if poke_id == row['id']:
                    pokemon = row['identifier']
                    df = df.drop(index)
                    pokemon_found = True
                    print(str(pokemon) + " was removed successfully")
                    input('Hit enter to continue')
            if pokemon_found == True:
                pass
            else:
                print('NOT A VALID ID')
                input('Hit enter to continue')
        elif user_input2 == 3:
            pokemon_found = False
            poke_id = int(input("Enter the ID of the pokemon you want to update: "))
            for index, row in df.iterrows():
                if poke_id == row['id']:
                    pokemon = row['identifier']
                    pokemon_found = True                   
                    print("What should " + str(pokemon) + "'s new name be? ")
                    new_name = input('Input here: ')
                    new_row = [row['id'], new_name, row['species_id'], row['height'], row['weight'], row['base_experience'], row['order'], row['is_default']]
                    df.loc[index] = new_row
                    print(str(new_name) + " was updated successfully")
                    input('Hit enter to continue')
            if pokemon_found == True:
                pass
            else:
                print('NOT A VALID ID')
                input('Hit enter to continue')
    elif user_input1 == 2:
        end = True
    else:
        print('NOT A VALID OPTION')
        input('Hit enter to continue')
with open("q13.out", "w") as file:
    file.write(df.to_string())

