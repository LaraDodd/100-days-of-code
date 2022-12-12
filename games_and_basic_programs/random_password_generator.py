# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:08:08 2022

@author: larad
"""
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
'''
password = ""

#running through loop for number of letters user wants
for i in range(int(nr_letters)):
  #generate random number between 0 and number of letters in the list of letters (minus 1)
  letter_num = random.randint(0,len(letters)-1) 
  letter = letters[letter_num]
  password = password + letter

for a in range(int(nr_symbols)):
  symbol_num = random.randint(0,len(symbols)-1)
  symbol = symbols[symbol_num]
  password = password + symbol

for b in range(int(nr_numbers)):
  number_num = random.randint(0,len(numbers)-1)
  number = numbers[number_num]
  password = password + number

print(password)

'''

#Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letter_list = []
symbol_list = []
number_list = []

#running through loop for number of letters user wants
for i in range(int(nr_letters)):
  
  letter_num = random.randint(0,len(letters)-1) 
  letter = letters[letter_num]
  letter_list.append(letter)

for a in range(int(nr_symbols)):
  symbol_num = random.randint(0,len(symbols)-1)
  symbol = symbols[symbol_num]
  symbol_list.append(symbol)

for b in range(int(nr_numbers)):
  number_num = random.randint(0,len(numbers)-1)
  number = numbers[number_num]
  number_list.append(number)


password_list = letter_list+symbol_list+number_list
print(password_list)
random.shuffle(password_list)
print(password_list)

password_str = ""

for char in password_list: 
  password_str += char


#str_password = ''.join(password_list)
print(password_str)


