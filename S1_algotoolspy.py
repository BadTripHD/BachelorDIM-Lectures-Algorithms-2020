# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:45:46 2020

@author: polletb
"""
import math

def algorithm_1(marks):
    average = 0    
    
    for i in marks:
        average += i
    
    average = math.floor(average / len(marks))
    return average


print(algorithm_1([10, 20]))