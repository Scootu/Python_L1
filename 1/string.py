#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:00:10 2023

@author: aneshamdaoui
"""
print("show the first 1000 prime number")

num = 145  
fr = float(f'{1/3:.2f}')   ## how to write 2 digite in float format  
strLitteral = 'anesHamdaoui'

print("the lenght of aneshamdaoui is" ,"{}".format(len(strLitteral)),strLitteral[0:4],)
print(f'{int(num*fr)} is {1/3*100:.2f} % of {num}')

print('write a program that print the year of the user besed in format fo dd/mm/yyyy')

#birthday = input("Hi,entre your birthday in the dd/mm/yyyy format \n")
#day= birthday[0:2]
#month =birthday[2:4]
#year = birthday[6:len(birthday)]

#print("you wear born in the year {}.".format(year))


#num_x = int(input('How many times should I print the letter X? '))
to_print = ''
#concatenate X to to_print num_x times
#i = 0 
#while i < num_x : 
#    to_print = to_print +'X' 
#   i = i + 1 
#print(to_print)

n_list = []  # Initialize an empty list to store odd numbers
l_num = float('-inf')  # Initialize l_num with negative infinity
i = 1  # Initialize the counter to 1

while i <= 10:
    num = int(input(f'enter number {i}: '))
    if num % 2 != 0:
        n_list.append(num)  # Append the odd number to the n_list

    if num > l_num and num % 2 != 0 :
        l_num = num  # Update l_num if num is greater

    i += 1  # Increment the counter

print("List of odd numbers:", n_list)
print("Largest number entered:", l_num)




