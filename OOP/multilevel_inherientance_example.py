# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 11:10:32 2021

@author: mjach
"""

#Base/parent class 1
class Person():

    def personDetails(self, name, age):
        print('Name of the person:', name)
        print('Age of the person:', age)

#Base/parent class 2
class MacAfee():
    def companyDetails(self, nameOfTheCompany, address):
        print('Company Name:', nameOfTheCompany)
        print('Company address:', address)

class Employee(Person, MacAfee):

    def employeeDetails(self, salary, skills):
        print('Employee salary:', salary)
        print('Employee skills:', skills)

#create employee object
employeeOne = Employee()
employeeOne.personDetails( 'Mohammed',  55)
employeeOne.companyDetails( 'McAfee',  'New work')
employeeOne.employeeDetails(50000,  'Java python etc..')