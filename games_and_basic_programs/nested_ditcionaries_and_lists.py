# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:57:36 2022

@author: larad
"""

#nesting list in dictionary
travel_log = {"France": ["Paris", "Lille", "Dijon"], 
              "Germany": ["Cologne", "Munich"],
              }

#nesting a dictionary inside a dictionary
travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 16, "money spent": "£1000",},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],  "total_visits": 5, "money spent": "£1000",},
    }

#nesting a dictionary in a list
travel_log2 = [
    {
     "Country": "France", 
     "cities_visited": ["Paris", "Lille", "Dijon"], 
     "total_visits": 16, 
     "money spent": "£1000",
     },
    {
     "Country": "Germany", 
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],  
     "total_visits": 5, 
     "money spent": "£1000",
     },
    ]

print(travel_log)
print(travel_log2)