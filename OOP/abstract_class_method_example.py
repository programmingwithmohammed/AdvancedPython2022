# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:40:38 2021

@author: mjach
"""

'''
Strong type of polymorphism

Abstraction

- OOP abstraction is one of the main principle out of four.
	- Inheritance
	- Encapsulation
	- Polymorphism
	- Abstraction
- with abstraction we hide all the data to increase the efficiency of the program and reduce the program complexity
- at the sane time we hide the implementation details and have to accessed through explicity
- through abstraction we decleare a abstraction method but we do not implement it
- abstraction class can have more than one abstract method.
- abstract class can not be instantiated. majority of the concept similar to Java
- After saying all of these actually python does not have real abstract classes and methods like Java but it can be implement or achived
- In python abstract class can be implemented using the Abstract Base Class (ABC) module. The module name is abc
- when you implement ABC(Abstract Base Classes) you must
    implement its properties and methods
'''
from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def find_area(self):
        pass

    @abstractmethod
    def find_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        #return pi * self.radius ** 2
        print('Area of the circle:',pi * self.radius ** 2)

    def find_perimeter(self):
        #return 2 * pi * self.radius
        print('Perimeter of the circle:',2 * pi * self.radius)

class Rectange(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def find_area(self):
        return self.height * self.width

    def find_perimeter(self):
        return 2 * (self.height + self.width)

circle = Circle(3)
# print('Area of the circle :', circle.find_area())
# print('Parimeter of the circle:', circle.find_perimeter())
circle.find_area()
circle.find_perimeter()

rectangle = Rectange(4, 6)
print('Area of the rectange:', rectangle.find_area())
print('Perimeter of the rectangle:', rectangle.find_perimeter())










