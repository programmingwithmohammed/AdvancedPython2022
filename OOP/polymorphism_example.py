# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:01:20 2021

@author: mjach
"""

'''
Polymorphism

- What is polymorphism?
 -. Polymorphism word came from greek. we can divide the polymorphism word in two parts
	first part - poly means many and
	second pard - morphism meand forms
	so it means many forms.

- so in software/coding/ programming we can do  a method can be transform in many forms.
'''

from math import pi

class Shape():

    def find_area(self):
        pass

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
# print('Area of the rectange:', rectangle.find_area())
# print('Perimeter of the rectangle:', rectangle.find_perimeter())