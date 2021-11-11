# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Title:
## Name: Benjamin Osafo Agyare
## UM email: bagyare@umich.edu



# # Modules for tasks

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.stats as spstat
from statistics import stdev
import os.path
import warnings
import re
from IPython.display import HTML
from ps1_fun import normal_mean_conf_int, binom_mean_conf_int
from functools import reduce


# # Question 0

# # Python Classes and Objects

# ## Overview
#   - [Python classes](#/slide-2-0)
#   - [Creating a Class data](#/slide-4-0)
#   - [The __init__() Function](#/slide-5-0)
#   - [Object Methods and the self operator](#/slide-6-0)
#   - [Modifying and Deleting objects](#/slide-8-0)

# ## Python classes
# - Python is an object oriented programming language.
# - Almost everything in Python is an object, with its properties and methods.
# - A Class is like an object constructor, or a "blueprint" for creating objects.

# ## Python classes
# - Some points on Python class:
#   + Classes are created by keyword class.
#   + Attributes are the variables that belong to a class.
#   + Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute

# ## Creating a Class
# - To create a class in python, use the reserved keyword `class`
#
# ### Example
# - Here is an example of creating a class named Student, with properties name, school and year:

class Student:
    school = "U of Michigan"
    year = "freshman"


# ## The __init__() Function
#
# - To make better meaning of classes we need the built-in `__init__()` function.
# - The `__init__()` is used function to assign values to object properties, or other operations that are necessary to do when the object is being created.
# - All classes have this, which is always executed when the class is being initiated.

# +
class Student:
    def __init__(self, name, school, year):
        self.name = name
        self.school = school
        self.year = year

person1 = Student("Ben", "University of Michigan", "freshman")
print(person1.name)
print(person1.school)
print(person1.year)


# -

# ## Object Methods and the self operator
# - Objects in python can also have methods which are functions that belong to the object

# ## Object Methods and the self operator
# - The self parameter
#   + The self parameter `self` in the example above references the current state of the class.
#   + It can be used to access the variables that belong to the class.
#   + You can call it whatever you like but has to be the first parameter of any function in a class

# ## Example

# +
class Student:
    def __init__(myself, name, school, year):
        myself.name = name
        myself.school = school
        myself.year = year

    def getAttr(person):
        print("Hi, I'm " + person.name + " and a "
              + person.year + " at " + person.school)


person2 = Student("Ben", "University of Michigan", "freshman")
person2.getAttr()
# -

# ## Modifying and Deleting objects
# - You can modify object properties
# - It is also possible to delete properties objects using the `del` keyword and same can be used to delete the object itself

# ## Example

# +
## Modify object properties
person2.year = "senior"

## Delete properties of objects
del person2.name

## Delete object
del person2
# -

# ## References:
# - [https://www.w3schools.com/python](https://www.w3schools.com/python)
# - [https://www.geeksforgeeks.org/python-classes-and-objects/](https://www.geeksforgeeks.org/python-classes-and-objects/)
# - [https://www.tutorialspoint.com/python3](https://www.tutorialspoint.com/python3)
