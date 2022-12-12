# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:50:38 2022

@author: larad
"""

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        #print("Leap year.")
        return True
      else:
        #print("Not leap year.")
        return False
    else:
      #print("Leap year.")
      return True
  else:
    #print("Not leap year.")
    return False
    


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if month > 12 or month < 1:
        return "invalid month"
    elif is_leap(year) and month == 2:
        days = 29
    else: 
        days = month_days[month - 1]
    return days
    
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







