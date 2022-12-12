# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:26:47 2022

@author: larad
"""

#add function 
def add(n1, n2):
  return n1+n2

#subtract function 
def subtract(n1, n2):
  return n1-n2

#divide function 
def divide(n1, n2):
  return n1/n2

#multiply function 
def multiply(n1, n2):
  return n1*n2
  
#store information in dictionary
operations = {"+":add,
            "-":subtract,
            "/":divide,
            "*":multiply,
            }

operators = ""
for i in operations:
  operators += i+" "



def calculator():
  num1 = float(input("First number? "))
  cont_calc = True

  while cont_calc:
  
    chosen_operation = input(f"Please choose an operator out of the following: {operators}")
  
    num2 = float(input("Next number? "))
    
    calculation_function = operations[chosen_operation]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {chosen_operation} {num2} is equal to {answer}")
  
    yes = input(f"Type 'y' to continue calculating with {answer}, or 'n' to stop calculating ")
  
    if yes == "y":
      cont_calc = True
      num1 = answer
    elif yes == "n":
      cont_calc = False
      calculator()
    else:
      print("wrong input")

calculator()
    


