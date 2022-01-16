# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:58:18 2021

@author: mjach
"""

#getter and setter example
class Person:

    def __init__(self):
        self.__name = 'Mohammed'
        self.__age = 55

    def personDetails(self):
        print(self.__name)
        print(self.__age)

    # getter and setter methods
    def getName(self):
        print(self.__name)
    def getAge(self):
        print(self.__age)

    def setName(self,name):
        self.__name = name
    def setAge(self,age):
        self.__age = age


person = Person()
# person.personDetails()
# person.getName()
# person.getAge()

person.__name = 'Hassan'
#person.setName('Hassan')
person.getName()
# person.setAge(45)
# person.getAge()

# print(person.name)
# print(person.age)