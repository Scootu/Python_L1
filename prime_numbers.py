#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:49:59 2023

@author: aneshamdaoui
"""

print("print 1000th prime number \n")
i = 1
odd_list  = []
while i <= 1000 : 
    #show all odd numbers
    if i % 2 !=0 :
       odd_list.append(i)
        
    i += 1
i = 0
n = 0
list_len = len(odd_list)
prime_list = []

while i < list_len:
    n = 0
    is_prime = True
    while n < list_len:
        if n != i and odd_list[i] != 0 and odd_list[n] % odd_list[i] == 0:
            is_prime = False
            break
        n += 1
    if is_prime:
        prime_list.append(odd_list[i])
    i += 1

print("List of prime numbers:", prime_list)
        
print(f'{prime_list}') 
