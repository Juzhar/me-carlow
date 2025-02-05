# -*- coding: utf-8 -*-
"""
HW3
"""
# Q4

import pandas as pd
end = False
scores ={}
while end == False:
    print("1. Add score \n2. Check score \n2. Show total scores \n4. Exit")
    user_input = input("Input here: ")
    if (user_input == '4'):
        end = True
    elif user_input == '1':
        username = input("Username: ")
        if username in scores:
            new_score = int(input("Score: "))
            score_list = scores[username]
            score_list.append(new_score)
            scores[username] = score_list
        else:
            score = int(input("Score: "))
            scores[username] = [score]
        
    elif user_input == '2':
        user = input("Which user's score would you like to see? ")
        if user in scores:
            df = pd.DataFrame(scores[user], columns =['Score'])
            print(df)
        else: 
            print('User does not exist')
    elif user_input == '3':
        user = input("Which user's score would you like to see? ")
        if user in scores:
            total_score = sum(scores[user])
            print(total_score)
        else:
            print('User does not exist')