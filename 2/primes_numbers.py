#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import log
"""
Created on Thu Nov  9 19:01:28 2023
this function will take more than 10min 
@author: aneshamdaoui
"""

# List of odd numbers
list_p_odd = []
i = 0 
n = 0   
z = 1
while i< 100000  : 
    if(i %2 !=0) :
       list_p_odd.append(i)
    i+=1     
    
i = 0
n = 0 
log_sum = 0 
sum_n = 0 
list_primes = []
while i < 50000 : 
    n = list_p_odd[i]
    z = n    
    while z >= 1:
        
        if(n % z == 0 and n != z and z != 1) :
            break
        elif(z == 1):
            list_primes.append(n)
            log_sum += log(n)
            print(f'log:{log_sum /n}')
        z = z - 1 
        
    i = i + 1 

