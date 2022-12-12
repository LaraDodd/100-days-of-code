# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 11:11:44 2022

@author: larad
"""

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
split_input = [*position]# don't need to do this! Can split a string, don't need to convert to list
print(split_input)
col = int(split_input[0]) 
row = int(split_input[1]) 
#col = int(position[0])
#row = int(position[1])

map[row-1][col-1] = "X"





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

