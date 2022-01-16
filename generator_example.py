# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:26:56 2021

@author: mjach
"""

'''
Generator Expression
- it is a iterable object - like list, set , dictionary
- generator works on demand basis unlike a list which iterate elements all at once
- generator expression looks like list comprehensions just differnce generator use parenthesis where list comprehensions use brackets
- generator are useful for large set of list without storting the entire list in memory

'''
#example 1 - list comprehension

# fruit_names = ['apple', 'banana', 'orange']
# list_comprehension = [('Length = ', len(fruitName)) for fruitName in fruit_names]
# print(list_comprehension)

# example 2 - generator expression
# fruit_names = ['apple', 'banana', 'orange']
# generator_expression = (('Length = ', len(fruitName)) for fruitName in fruit_names)
# print(generator_expression)
# for fruit in generator_expression:
#     print(fruit)

# example 3
import timeit
# list_com = '[number for number in range(0,5 ** 11)]'
# print(timeit.timeit(list_com, number =1))

# generator_expression = '[number for number in range(0,5 ** 11)]'
# print(timeit.timeit(generator_expression, number =1))

generator_expression = [number for number in range(0,5 ** 11)]
print(timeit.timeit(lambda:generator_expression, number =1))

#https://stackoverflow.com/questions/54135771/timeit-valueerror-stmt-is-neither-a-string-nor-callable













