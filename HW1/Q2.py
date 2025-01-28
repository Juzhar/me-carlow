# -*- coding: utf-8 -*-
"""
HW1
"""
# Q2

userage = int(input("What is your age? "))
new_age = userage + 5
with open("q1_out.txt", "w") as file:
    file.write(str(userage))
    file.write(str(new_age))