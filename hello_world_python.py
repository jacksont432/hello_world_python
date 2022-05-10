# This is a tutorial for people in experienced in python
# it will show you how to do basic functions

# these are libraries
# you can use this code to perform functions more easily
import numpy as np
import pandas as pd
import math
import os

# printing
# in python printing is easy use print() to print to the console
print("hello world")

# variables
# in python variables are implicitly typed which means you do not need to declare variables or their type
# int, float and double types
number = 11
print(number)
# now a double or float
number = -4.2
print(number)
# string types can use '' or ""
hello = "Hello mom!"
goodbye = 'Goodbye mom.'
print(hello)
print(goodbye)
# booleans use either True or False
python_is_cool = True
print('Python is cool?', python_is_cool)
# lists are collections of values
my_list = [1, 2, 3, 4]
print(my_list)
# tuples are immmutable lists which means they cannot be changed
my_tuple = (1, 2, 3, 4)
print(my_tuple)

# control flow
# python has all of the usual control flows such as for, if and while
# it uses white space instead of {} for blocks
# python uses if, elif and else for selection statements
if python_is_cool:
    print("Python is the best language")
else:
    print("C is the only language")
# you can either loop using indices
# use len() to access the length of the list
for i in range(len(my_list)):
    print(my_list[i])
# or do a foreach loop
# foreach loops iterate through each item in the collection
for num in my_tuple:
    print(num)
# while loops are similar
count = 0
while True:
    if count == 0:
        print("This is my first iteration in the loop")
    elif count == 1 or count == 2:
        print("Still looping")
    elif count == 3 and count != 4 or count == 9:
        print("will this loop ever end")
    else:
        print("I am almost done")
    print(abs(count))
    # python is lame and doesn't have ++ or --
    count += 1
    if (count > 10):
        # this ends the loop
        break

# numpy and pandas are collections that handle lists
numpy_list = np.array([5, 2, 3, 6, 1, 9, 8])
# print the unsorted list
for num in numpy_list:
    print(num)
# sort the list using numpy
numpy_list = np.sort(numpy_list)
print("Now sorted!")
for num in numpy_list:
    print(num)
data=[[1, 'A'], [3, 'C'], [4, 'D'], [2, 'B']]
pandas_collection = pd.DataFrame(data, columns=['Numbers', 'Letters'])
print(pandas_collection)
# end of tutorial
# for more help run
# pipenv install -r requirements.txt
# that will help you get really cool packages
# and be able to run this file!
# good luck coding!