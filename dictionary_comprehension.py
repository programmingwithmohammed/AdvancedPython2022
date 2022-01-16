# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:49:05 2021

@author: mjach
"""

'''
Dictionary Comprehensions

- similar to list comprehensions
- use curly braces instead of brackets
- dictionary consist of key value pairs. key:value

'''
# student_result = {f'student_name- {result}': 0 for result in range (0, 10)}
# print(student_result)



student_result = [(f'studnet_name - {result}', result * 5) for result in range(1,10)]
#print(student_result)

result = {key:value for (key, value) in student_result}
print(result)












