#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:23:39 2023

@author: aneshamdaoui
"""
# Test if an int > 2 is prime. if not, print smallest divisor 
x = int(input('Enter an integer greater than 2: '))
greater_divisor = None 
for guess in range(2, x):
    if x%guess == 0:
        greater_divisor = int(x / guess)  
        break 
if greater_divisor != None:
    print('Greater divisor of',x, 'is', greater_divisor)
else:
    print(x,'is a prime number')


