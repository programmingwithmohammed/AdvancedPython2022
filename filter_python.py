# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:13:09 2021

@author: mjach
"""

my_numbers = [1,2,3,4,5,6,7,8]

# def find_even_number(num):
#     if num % 2 == 0:
#         return True
#     return False
# print('Finding even  number:', list(filter(find_even_number,my_numbers)))

#Example 2

print('Finding the even number using the lambda function:',list(filter(lambda num : (num % 2 == 0),my_numbers)))
