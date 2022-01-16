# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:33:13 2021

@author: mjach
"""
'''
- Encapsulation is basically is hiding or restrict access your data, methods and variables
- When you set private you can only changed withing a class
- To change the data you cad create setter and getter methods
- You can also use property decorator to create getter and setter methods which is pythonic way to do.

- by default all the variable and methods are public in python
- _ single underscore before a variable or methods will make protected
- __ double underscore will make the variable or methods private.

- Python use very weak encapsulation. it use just a convention not enforced by the language.
'''
#Example public
# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def personDetails(self):
#         print(self.name)
#         print(self.age)

# person = Person('Mohammed', 33 )
# #person.personDetails()

# print(person.name)
# print(person.age)

#Example protected
# class Person:

#     def __init__(self, name, age):
#         self._name = name #protected varaible
#         self._age = age #protected varaible
#     def personDetails(self):
#         print(self._name)
#         print(self._age)

# person = Person('Mohammed', 33 )
# #person.personDetails()

# print(person._name)
# print(person._age)

#Example private

class Person:

    def __init__(self, name, age):
        self.__name = name #private varaible
        self.__age = age #private varaible

    # def personDetails(self): #public method
    #     print(self.__name)
    #     print(self.__age)

    # def _personDetails(self): #protected method
    #     print(self.__name)
    #     print(self.__age)

    def __personDetails(self): #private method
        print(self.__name)
        print(self.__age)

person = Person('Mohammed', 33 )
person.__personDetails()

#print(person.__name)
#print(person.age)
