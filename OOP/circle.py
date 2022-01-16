# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 09:40:19 2021

@author: mjach
"""

'''
What is Object?

An object can be a function, a variable, a property, a class… everything in Python is an object.

- to create an object we need an __init__ method. if we don't use it by default python use __init__ method to create an object.
- you can pass instance variable through __init__ method to create an object.
'''
'''
What is a Class?

-Class is a blue print of a an Object? A typr of a something e.g car class, animal class
-Every thing or object in Python is an instance of a class.
- The number 42 is an instance of the class int.
-The string Hello, world is an instance of the str (or string) class.
- From a class you can create a new types of object.

What is class variable?
- class variable shared by all instance of the class.

What is an instance?

- if car is a type of something you can think of instance as a specific things like my_VWW is a type of car.
- Both class and instance can have there own variables and methods.

What is self keyword?

- self is used inside the classes to refer its bound to that specific class all of its instance variables and methods.

What is method?
- class can also have a method which is a behaviour of an object.
- that is belong to the object.

-variable is an attribute of an object.

What is __init__ function/method?
-it is a constructor?
-called magic method.
- methods that are used underscores with bracket called magic method - e.g - __init__(),  __gt__(), __ge__(), __str__(), __repr__()

What is a static method?
- static method don''t know about class or instance
- you can create static method without self keyword
- method can be trun to static method just add @staticmethod on top of the method.
- you can call static method either using by class or by the instance
'''

from math import pi

class Circle():

    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        return pi * self.radius ** 2

    def find_perimeter(self):
        return 2 * pi * self.radius


circle_one = Circle(3)
print('Area of the circle:', circle_one.find_area())
print('Perimeter of the circle:', circle_one.find_perimeter())

circle_two = Circle(6)
print('Area of the circle:', circle_two.find_area())
print('Perimeter of the circle:', circle_two.find_perimeter())
