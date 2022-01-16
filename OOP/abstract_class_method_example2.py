# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:44:22 2021

@author: mjach
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


    @staticmethod
    def can_drive(consumption, fuel):
        return consumption <= fuel
        # result = consumption - fuel
        # return result

    @staticmethod
    def fuel_level(consumption,fuel):
        return 'Current fuel level:', consumption - fuel


class Car(Vehicle):
    ADD_CONSUMPTION = 0.9
    #ADD_CONSUMPTION = 1.0

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + Car.ADD_CONSUMPTION)
        if self.can_drive(consumption, self.fuel_quantity):
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def fuel_level(self):
        #return self.fuel_quantity
        self.fuel_quantity = self.fuel_quantity - self.fuel_consumption
        return self.fuel_quantity

car = Car(20, 5)
print('Starting fuel quantity:',car.fuel_quantity)
car.drive(3)
print('After driving fuel quantity:',car.fuel_level())
car.refuel(10)
print('After refiliing fuel level:',car.fuel_quantity)
#car.drive(33)
print('fuel level :',car.fuel_level())
#car.drive(10)
#print('Current fuel level :',car.fuel_level())
class Truck(Vehicle):
    ADD_CONSUMPTION = 1.6
    REFUEL_PROBLEM = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + Truck.ADD_CONSUMPTION)
        if self.can_drive(consumption, self.fuel_quantity):
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.REFUEL_PROBLEM





print("----------")

# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)