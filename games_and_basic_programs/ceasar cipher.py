# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:03:08 2022

@author: larad
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encode(text, shift):
  encoded_text = ""
  
  for letter in text:
    new_index = alphabet.index(letter)+shift
    if new_index > 25:
      new_index = new_index - 26
    encoded_text += alphabet[new_index]
    
  print(encoded_text)



def decode(text,shift):
  decoded_text = ""

  for letter in text:
    new_index = alphabet.index(letter)-shift
    if new_index < 0:
      new_index = new_index + 26
    decoded_text += alphabet[new_index]
    
  print(decoded_text)


if direction == 'encode':
  encode(text,shift)
elif direction == 'decode':
  decode(text,shift)



  