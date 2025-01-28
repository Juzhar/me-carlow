# -*- coding: utf-8 -*-
"""
HW1
"""
# Q5

print("Enter a list of names below")
end = False
namelist = []
while end == False:
    print("1. Enter user \n2. Exit")
    user_input = input("Input here: ")
    if (user_input == '2'):
        end = True
    elif user_input == '1':
        username = input("Username: ")
        namelist.append(username)

with open("q5_out.txt", "w") as file:
    for item in namelist:
        file.write(item)
        file.write('\n')

