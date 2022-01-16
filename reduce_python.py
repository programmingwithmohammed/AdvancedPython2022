# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:26:49 2021

@author: mjach
"""

from functools import reduce

#my_numbers = [1,2,3,4,5,6]

# def add(num1, num2):
#     return num1 + num2
# print('Final value:', reduce(add, my_numbers))

print('Using lambda :', reduce((lambda num1, num2 : num1 + num2), [1,2,3,4,5,6]))


