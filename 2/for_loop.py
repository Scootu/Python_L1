#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:37:44 2023

@author: aneshamdaoui
"""
i = 0 
for i in range(2):
    print(i)
    i = 0 
    print(i)

# 0 0 1 0 
x = 3
for j in range(x): # 0 
    print('Iteration of outer loop')
    for i in range(x):
        print('    Iteration of inner loop')
        x = 5 # this will affect in the range in the next loop 
        



            