# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 21:35:40 2022

@author: tamir
"""

from collections import Counter
breakfast=['spam','eggs','spam','eggs']
breakfast_counter=Counter(breakfast)
print(breakfast_counter)

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter=Counter(lunch)
print(lunch_counter)

breakfast_counter + lunch_counter

print(breakfast_counter + lunch_counter)
breakfast_counter & lunch_counter
print(breakfast_counter & lunch_counter)#intersection

breakfast_counter | lunch_counter #union
print(breakfast_counter | lunch_counter)
