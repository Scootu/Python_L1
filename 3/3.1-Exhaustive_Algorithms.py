#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:47:36 2023

@author: aneshamdaoui
"""

# Exhaustive enumeration 
# decrementing function 
x = int(input("Entre an integer :"))
ans = 0
while ans**3 < abs(x):
    # print('Value of the decrementing function abs(x) - ans**3 is',abs(x)-ans**3)
    ans = ans + 1 
if ans**3 != abs(x):
    print(x,'is not a prefect cube')
else:
    if x < 0 :
        ans = -ans 
    print('Cube root of',x,'is',ans)



