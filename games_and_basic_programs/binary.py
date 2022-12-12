# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:18:55 2022

@author: larad
"""
binary = []

x = 0

integer = 12

while integer >= 1:
    quotient = integer%2
    if quotient == 1:
        binary.insert(0,1)
    else:
        binary.insert(0,0)
        
    integer = integer//2
    x += 1

print(binary)
   

zeros = 0
   
for i in binary:
    print(i)
    if binary[i] == 0 and binary[i+1]== 0:
        zeros = zeros+1
    
            
print(f"zeros count: {zeros}")
    
        
        
