# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:02:17 2021

@author: mjach
"""
'''
Set comprehensions

- its a combinaton of list and dictionary comprehensions
- it create a set object
'''
student_result = { result for result in [50,80,80,60,50,30]}
print(student_result)