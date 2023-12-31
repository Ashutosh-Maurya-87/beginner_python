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
# but if we want the each item of this list [1,2,3,4,5,6] then
l = [1,2,3,4,5,6]
newL = []
for val in l:
    newL.append(cube(val)) 


print(newL); '''[1, 8, 27, 64, 125, 216]'''














