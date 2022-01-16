# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:58:53 2021

@author: mjach
"""

#getter and setter example
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def personDetails(self):
        print(self.__name)
        print(self.__age)

    # getter and setter methods

    @property
    def getName(self):
        print(self.__name)

    @getName.setter
    def setName(self,name):
        self.__name = name

    @property
    def getAge(self):
        print(self.__age)
    @getAge.setter
    def setAge(self,age):
        self.__age = age


person = Person('Mohammed', 33 )
#person.personDetails()
person.getName
# person.getAge

# person.setName = 'Hassan'
# person.getName
# person.setAge = 55
# person.getAge

# print(person.name)
# print(person.age)