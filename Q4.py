# -*- coding: utf-8 -*-
"""
HW1
"""
# Q4
print("Enter a list of names below")
end = False
namelist = []
while end == False:
    print("Add a name or enter exit to exit")
    user_input = input("Input here: ")
    if (user_input == 'exit'):
        end = True
    else:
        namelist.append(user_input)

with open("q4_out.txt", "w") as file:
    for item in namelist:
        file.write(item)
        file.write('\n')
