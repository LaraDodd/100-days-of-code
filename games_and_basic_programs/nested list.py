# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:55:14 2022

@author: larad
"""

veg = "carrots, potatoes, tomatoes, beets"
veg_list = veg.split(",")


fruit = "apples, pears, oranges"
fruit_list = fruit.split(",")

list = [veg_list, fruit_list]
print(list)

print(list[1][1])