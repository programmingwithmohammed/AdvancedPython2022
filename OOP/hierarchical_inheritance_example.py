# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:41:25 2021

@author: mjach
"""
#base class example
class Employee():

    def employeeDetails(self, name, age, adddress):
        print('Name of the employee:',name)
        print('Age of the employee:',age)
        print('Address of the employee:',adddress)


class Docotor(Employee):
    def service(self):
        return'Doctor is looking after his/her patient.'

class Teacher(Employee):
    def teach(self):
        return 'Teacher is teching maths...'

doctor1 = Docotor()
doctor1.employeeDetails( 'Mohammed', 55, 'Dublin')
print(doctor1.service())

teacher1 = Teacher()
teacher1.employeeDetails( 'Hassan',  65,  'Cork')
print(teacher1.teach())