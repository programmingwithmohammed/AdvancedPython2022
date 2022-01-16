# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 10:30:46 2021

@author: mjach
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
    @abstractmethod
    def play(self):
        pass

class Cat(Animal):
    def eat(self):
        print('Cat is eating now..')

    def sleep(self):
        print('Kity is leeping now')

    def play(self):
        print('Kitty is very happy and playing now')

class Dog(Animal):
    def eat(self):
        print('charly is eating now..')

    def sleep(self):
        print('charly is leeping now')

    def play(self):
        print('charly is very happy and playing now')


cat = Cat()
cat.eat()
cat.play()
cat.sleep()

print('------------------')
dog = Dog()
dog.eat()
dog.play()
dog.sleep()
