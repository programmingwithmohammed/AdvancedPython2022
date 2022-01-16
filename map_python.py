# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:07:34 2021

@author: mjach
"""

# map function in python

# Advantage

# It is more efficient than python noraml for loop.
# Reduce memory consumption. With python for loop it store whole list or set or tuple into your system,
# where map only gets one item at a gieven time in your system memory.

# How to write map syntax?

# map(function, iterable,....)
# Here, the function does some action with the iterable items.

# How map works?

# It takes two parameters(required) but you can pass more than one iterable as many as you like
# but make sure function has a parameter for each iterable.

# Map returns an object of a map class but you need to convert it to either list or set and so no

#Exmple 1

number_one_list = [2,3,4,5,6]
number_two_list = [7,8,9,10,11]

square_list_items = []

for number in number_one_list:
    square_list_items.append(number ** 2)

#print('Square list items:',square_list_items)

#Example 2

def square_list_items(number):
    return number * number

result = map(square_list_items, number_one_list )
#print('Memory location address: ', result)
#print(list(result))

#Example 3
def add_list_items(number1, number2):
    return number1 + number2

add_result_items = map(add_list_items, number_one_list, number_two_list)
print('Adding two list items:', list(add_result_items))

#Example 4
# We can pass any of the built in function into map as a first argument
string_items = ['1','2','3']
convert_int = map(int,string_items)
print('Converted int items',list(convert_int))

convert_float = map(float,string_items)
print('Converted float items',list(convert_float))

int_items = [1,2,3,4]
convert_str = map(str,int_items)
print('Int to string:', list(convert_str))

#Example 5
string_list = ['Welcome', 'to', 'my', 'channel']
print('Length of the each string:',list(map(len,string_list)))

#Example 5

#number_one_list = [2,3,4,5,6]
lambda_result = map(lambda num: num * num, number_one_list)
print('Lambda result:', list(lambda_result))

#Example 6

my_string = ['I' , 'like', 'python']

result = map(str.capitalize, my_string)
str_result = list(result)
print('Word capital:',str_result)
print('All uppercase:', list(map(str.upper, my_string)))
print('All lowercase:', list(map(str.lower, my_string)))
#print('REmove whit espace:', list(map(str.strip, my_string)))

