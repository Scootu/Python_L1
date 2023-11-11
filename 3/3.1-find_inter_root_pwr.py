#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:40:03 2023

@author: aneshamdaoui
"""
# Print pwr root of an integer 
x = int(input('Enter an integer: '))

for pwr in range(2,6,1):
    root = 0
    while root**pwr < x :
        root = root + 1
    if(root**pwr == x):
        break

if(root**pwr != x):
    print('there not exist a number such that root**pwr ==',x)
else:
    print(f'{root}**{pwr} ={root**pwr} == x = {x}')
    

    


