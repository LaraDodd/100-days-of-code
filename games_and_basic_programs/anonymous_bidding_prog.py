# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:06:01 2022

@author: larad
"""
import os
print("Welcome")

other_bidder = True
bidder_list = []

def add_bidder(bidder_name, bidder_bid):
    bidder_dict = {}
    bidder_dict["Person"] = bidder_name
    bidder_dict["Bid"] = bidder_bid
    
    bidder_list.append(bidder_dict)



while other_bidder:
    name = input("What's your name? ")
    bid = input("What's your bid? ")
    
    add_bidder(name, bid)
    
    more_bidders = input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    
    if more_bidders == "no":
        other_bidder = False
    
    os.system('cls')
    
max_bid = "$0"
index = 0

for i in range(len(bidder_list)):

    if int((bidder_list[i]["Bid"]).strip("$")) > int((max_bid).strip("$")):
        max_bid = bidder_list[i]["Bid"]
        index = i

max_bidder = bidder_list[index]["Person"]

print(f"The max bid is {max_bid} and the bidder was... {max_bidder}")