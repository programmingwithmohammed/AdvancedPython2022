# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:53:11 2021

@author: mjach
"""

'''
Decorator

- in python a decorator is a function and receive a function as a argument.
- it helps to add extra functionalities without modifying actual function.
- in python function can be passed as a argument - you have seen map , reduce
- we can create function within another function
- function can return another function
- syntax of the decorator is  start with @ sign
'''


# def python_basic():
#     print('So far we have learned python basic.')

# def python_advance(function):
#     #function()
#     print('Whats up..')
#     function()
#python_advance(python_basic)

def python_advance(function): # outer function/decorator function
    def python_object_oriented(): # inner funciton
        function()
        print('Now, we are larning python advance topics..')
        #function() # calling outer function/decorator function
    return python_object_oriented # return inner function


@python_advance
def python_basic():
    print('So far we have learned python basic.')

python_basic()

def calculator(function):
    def smart_calculator(a,b):
        return function(a,b)
    return smart_calculator

@calculator
def addition(a,b):
    print(a * b)

addition(5, 5)








