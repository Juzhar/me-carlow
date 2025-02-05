# -*- coding: utf-8 -*-
"""
HW3
"""
# Q2

import pandas as pd
end = False
scores ={}
while end == False:
    print("1. Add score \n2. Check score \n3. Exit")
    user_input = input("Input here: ")
    if (user_input == '3'):
        end = True
    elif user_input == '1':
        username = input("Username: ")
        if username in scores:
            new_score = input("Score: ")
            score_list = scores[username]
            score_list.append(new_score)
            scores[username] = score_list
        else:
            score = input("Score: ")
            scores[username] = [score]
        
    elif user_input == '2':
        user = input("Which user's score would you like to see? ")
        df = pd.DataFrame(scores[user], columns =['Score'])
        print(df)
        

