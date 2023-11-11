#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:13:34 2023

@author: aneshamdaoui
"""

# prite the sum of prime numbers greater than 2 and less than 1000 
sum_p = 0
for odd in range(3,999):
    if(odd%2 != 0):
        n = 3
        while n != odd:
            if(odd%n == 0):
                break
            n = n + 1
        if(n == odd):
                sum_p += odd
        


            
                
            