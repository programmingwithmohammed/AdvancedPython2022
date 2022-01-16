# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 11:49:58 2021

@author: mjach
"""
'''
1. Never put same name module and package name. Always put different name.
2. Make sure to put __init__.py file. It will consider as a python package.
3. If you import all with *  these symbole make sure to put inside the __init__.py file
    __all__ = ['name of the module', '.....'] then you can use the module functions and attributies.
4. Module is a python file. Inside the module it can be any attributes, functions, class etc.

'''
#Example 1

# import sports.cricket.sportsDetails
# print(sports.cricket.sportsDetails.play())
# print(sports.cricket.sportsDetails.score())

#Example 2

# from sports.rugby import home_away
# print(home_away.home())

#Example 3

# from sports.soccer import *
# print(home_away.home())



