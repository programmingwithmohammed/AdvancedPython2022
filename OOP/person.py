# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 10:30:29 2021

@author: mjach
"""

'''
What is inheritance?

- we can say inheritance is copying all the functionalities of the base/parent class.
Advantage of the using inheritance --
- DRY - do not repeat yourself - code reuseability
- you can add or remove the functionality or features without modifying the class.
- inheritance define as a -- is a relationship
'''

class Person():

    def __init__(self, firstName, secondName):
        self.firstName = firstName
        self.secondName = secondName

    def person_details(self):
        return f'{self.firstName}{self.secondName}'


#creat a person abject

personOne = Person('Mohammed', ' Chowdhury')
#print(personOne.person_details())

# Employee is a Person - here employee and person is a relatioship
class Employee(Person):

    def __init__(self, firstName, secondName):
        super().__init__(firstName, secondName)

    def employeeAge(self,age):
        return f'{self.age} is a years old'

employeeOne = Employee( 'Hassan',  ' Ali')
print(employeeOne.person_details())