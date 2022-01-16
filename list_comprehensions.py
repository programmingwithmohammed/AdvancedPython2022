# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 11:28:14 2021

@author: mjach
"""

'''
List comprehensions

- a unique way of creating a list
- it consist of bracket and containg an expression followed by a for loop clause
- within a list comprehensions we can perform other python operation such as get string length, make string uppercase etc..
- we can use condition statement within list comprehensions like if ,else'

'''
#example 1
# fruit_names = ['apple', 'banana', 'orange']
# empty_fruit_list = []
# for fruit in fruit_names:
#     empty_fruit_list.append(len(fruit))

# print(empty_fruit_list)

#example 2 - list comprehension

# fruit_names = ['apple', 'banana', 'orange']
# list_comprehension = [('Length', len(fruitName)) for fruitName in fruit_names]
# print(list_comprehension)

# example 3

# find_even_num = []
# for num in range(100):
#     if num % 2 == 0:
#         find_even_num.append(num)
# print('0 to 100 even num:', find_even_num)

# example 4
# find_all_even_num = [('even num:', num) for num in range(100) if num % 2 == 0]
# print(find_all_even_num)

#example 5
# find_all_even_num = [str(num) + '= Even num' if num % 2 == 0 else str(num) + '= Odd num' for num in range(10)]
# print(find_all_even_num)


# example 6
fruit_names = ['apple', 'banana', 'orange']
list_comprehension = [('Length', len(fruitName),fruitName.upper() ) for fruitName in fruit_names]
print(list_comprehension)









