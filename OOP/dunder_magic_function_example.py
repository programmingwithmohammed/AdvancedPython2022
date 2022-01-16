# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:16:15 2021

@author: mjach
"""
'''
__repr__ is to find out the representation of an object official way
__str__ is to find out the informal way to representation of an object

'''
class Dog():

    def __init__(self, name, breed, age):
        self.name= name
        self.breed = breed
        self.age = age

    def __repr__(self):
        return 'Belong to class of {}, name of {}, breed of the dog{}, age of the dog{}'.format(
            self.__class__.__bases__[0].__name__,self.__class__.__name__, self.breed, self.age)

    def __str__(self):
        return 'This dog name is {}, breed typr is  {}, age of the dog is {}'.format(self.name, self.breed, self.age)

dog = Dog('Rita', ' Golden', ' 10')
print(dog)
#print(repr(dog))
#print(dog.__repr__())
