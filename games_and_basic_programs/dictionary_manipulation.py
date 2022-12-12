# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:04:11 2022

@author: larad
"""

programming_dictionary = {
  "Bug": "An error in a program that prevents  the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

#print the keys
for item in programming_dictionary:
  print(item+"\n")

#print the values 
for key in programming_dictionary:
  print(programming_dictionary[key]+"\n")

print(programming_dictionary)

#retrieving item from dictionary
print(programming_dictionary["Bug"])

#adding new items to dictionary
programming_dictionary["Loop"] = "Action that repeats over and over again"
print(programming_dictionary)

#initialise empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
programming_dictionary = {}

#reassign a value 
programming_dictionary["Bug"] = "a moth"