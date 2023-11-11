#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:04:07 2023

@author: aneshamdaoui
"""
# sum of prime numbers 2<p<1000 
# odd numbers 3 to 999 
i = 0 
prime_sum = 0 

for i in range(1,999,1):
    if(i%2!=0):
        for n in range(i,0,-1):
            if(i % n == 0 and n != i and n != 1):
                break
            elif(n == 1):
                prime_sum = i + prime_sum 

print(prime_sum)

                


                
                    
                


        

    

     
            
