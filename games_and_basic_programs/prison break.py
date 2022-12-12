# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:53:57 2022

@author: larad
"""

#initial conditions
prison = [1, 1, 0, 0, 0, 1, 0]
print("original prison "+str(prison))
freed = 0


for i in range(len(prison)):
  if prison[i] == 1: 
    freed = freed + 1 # increases count of freed by 1
    
    #changing prison list, 0's to 1's, 1's to 0's
    for a in range(len(prison)):
      prison[a] = abs(prison[a]-1)
    print(prison)

print(freed)