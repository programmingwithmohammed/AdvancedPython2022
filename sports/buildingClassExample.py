# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 12:14:56 2021

@author: mjach
"""

class Building:

    buildingName = 'ABC Tower'

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def buidlingDetails(self):
        print('Name of the building:',self.name)
        print('Color of the building:',self.color)
        print('Number of age of the building:',self.age)

    def numOfFloors(self,noOfFloor):
        print('Number of floors:',noOfFloor)

#example 1
buildingObj = Building('Luxury Tower', 'Red', '12')

#buildingObj.buidlingDetails()

#print(Building.buildingName)

#print(buildingObj.buildingName)

#example 2

anotherbuildingObj = Building('XYZ Tower', 'Green', '20')

anotherbuildingObj.buidlingDetails()
anotherbuildingObj.numOfFloors(20)
