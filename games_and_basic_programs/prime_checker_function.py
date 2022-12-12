# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:26:11 2022

@author: larad
"""
def prime_checker(number):
    
    num_list =[]
    for i in range(2,number):
        num_list.append(number%i)

    if 0 in num_list:
        print("It's not a prime number")
    else:
        print("It's a prime number")



user_input = int(input("Check this number: "))
prime_checker(number=user_input)
