# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:44:41 2021

@author: mjach
"""

word = 'programming'
#print(word[0])

# print(word[0:4])#start 0 and end 4th but exclude 4th position
# print(word[3:8])

# print(word[:4])#starting form 0 to end 4th position and exclude 4th position
# print(word[4:])#starting from 4th to the end

sentence = 'python programming'

#print(sentence[:])

# list example slicing

numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[0])
# print(numbers[:])

# print(numbers[::2])# moving forward by 2/ start 0 to the end and step by 2
# print(numbers[::-1]) # reversing the list
print(numbers[1:9:3])# start index 1 and finish to end index and steps by 3
