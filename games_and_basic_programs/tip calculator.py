# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:10:42 2022

@author: larad
"""


print("Welcome to the tip calculator\n")
bill = input("What was the total bill? ")


        
if '£' in bill:#error checking
  bill = bill.replace("£", "")
  print(bill)    
  

people = input("How many people to split the bill? ")

tip = input("percentage tip: ")

if '%' in tip:
  tip = tip.replace("%", "")
  print(tip)
elif float(tip)<1:
  tip = int(float(tip)*100)

price_pp = (int(bill)+int(tip)*.01*int(bill))/int(people)
print(price_pp)
  
