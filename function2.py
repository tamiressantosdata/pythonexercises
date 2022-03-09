# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:34:26 2022

@author: tamir
"""

def works(arg):
    result = []
    result.append(arg)
    return result

print(works("0,1,2,3,4"))

def answer():
    print(7)

answer()

def run_something(func):
    func()
    

print(run_something(answer))


#Keyword Arguments
##To avoid positional argument confusion, you can specify arguments by the
#names of their corresponding parameters, even in a different order from
#heir definition in the function:
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

#When used inside the function with a parameter, an asterisk groups a
#variable number of positional arguments into a tuple of parameter values

def print_args(*args):
    print("positional arguments of a tuple",args)
    
print_args(3,2,1)


#You can use two asterisks (**) to group keyword arguments into a
#dictionary, where the argument names are the keys, and their values are the
#corresponding dictionary values. The following example defines the
#function print_kwargs() to print its keyword arguments:

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


