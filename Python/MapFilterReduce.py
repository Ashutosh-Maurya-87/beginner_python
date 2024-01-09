''''
In Python the map(), filter() and reduce() function are built-in function in python 
that allow we to apply a function to a sequence of elements and return the new sequence
These function are known as higher-order-function, as they take other function as a arguments.

Syntax: map()

map(function, iterable)

function: the function argument is a function that is applied to each element in the iterable argument.

itreable: the iterable argument can be a list, tuple or any other iterable object

'''



# write a program that is print the cube of this each item ex = 
'''ex [2,3,4] cube is [8,27,64]'''

def cube(n):
    return n*n*n

print(cube(3)); '''27'''
# but if we want to the cube of each item of this list [1,2,3,4,5,6] then
l = [1,2,3,4,5,6]
newL = []
for val in l:
    newL.append(cube(val)) 


print(newL); '''[1, 8, 27, 64, 125, 216]'''

# MAP %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# using map method --------

newList = list(map(cube, l))

print('newList', newList); '''newList [1, 8, 27, 64, 125, 216]'''
print(list(map(lambda a: a*a*a, l))); '''[1, 8, 27, 64, 125, 216]'''

# FILTER %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''
The filter function filter a sequence of elements based on a given 
predicate(a function that return boolean value) and return a new sequence containing only the elements that 
the predicate.

# Syntax ------
filter(predicate, iterable)

predicate: this arguments is a function that return a boolean value and is applied to each 
element in the iterable arguments. 

Iterable: The iterable arguments cab be a list, tuple or any other iterable object 
'''
def filter_function(num):
    return num > 2

newFilterList = list(filter(filter_function,l))

print('newFilterList', newFilterList); '''newFilterList [3, 4, 5, 6]'''

new = list(filter(lambda x : x > 2, l))
print(new); '''[3, 4, 5, 6]'''


# reduce %%%%%%%%%%%%%%%%%%%%%%%%
'''
the reduce function is also a higher order function that take function as an argument.
It take two argument and return a single value. It is a part of functools module in Python.

Syntax______------------------
reduce(function, iterable)

function: The function argument is a function that take two arguments and return a single value 


The iterable argument is a sequence of elements such as list or tuple

The reduce function applies the function to the first two elements in the iterable and then applies the function
to the result and the next element and so on. The reduce function return the final result
'''

from functools import reduce

numberList = [1,2,5,4,6,3,1]

# calculate the sum of numbers using the reduce method

def mySum(x,y):
    return x+y

sum = reduce(mySum, numberList)

sum1 = reduce(lambda x,y: x+y, numberList)

print('sum using reduce method', sum); '''sum using reduce method 22'''
print('sum using reduce method and lambda expression', sum1); '''sum using reduce method and lambda expression 22'''










