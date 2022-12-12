# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:43:42 2022

@author: larad
"""

#local scope 

def drink_potion():
    potion_strength = 2 
    print(potion_strength)
    

print(potion_strength) # throws a name erro


#global scope

new_potion_strength = 2

def drink_potion1():
    print(new_potion_strength)

drink_potion()
drink_potion1()

#gloabl variables 
#better to do it like this

enemies = 1

def increase_enemies():
    return enemies + 1

#Style guide
#glabal variables always upper case 

PI = 3.14159