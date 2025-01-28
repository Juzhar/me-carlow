# -*- coding: utf-8 -*-
"""
HW1
"""
# Q3
userage = int(input("What is your age? "))
result = ''
if userage > 30:
    result = 'Fail'
elif userage >= 20:
    result = 'Pass'
else:
    result = 'Fail'
with open("q3_out.txt", "w") as file:
    file.write(result)