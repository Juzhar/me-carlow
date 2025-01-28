# -*- coding: utf-8 -*-
"""
HW1
"""
# Q1

username = input("What is your name? ")
if (username[0].islower() == True):
    capital_letter = username[0].upper()
    capital_username = capital_letter + username[1:]
else:
    capital_username = username
print ("Hello, " + capital_username)
with open("q1_out.txt", "w") as file:
    file.write("Hello, " + capital_username)