# Indentation ---------------------
      Indentation refers to the spaces at the begining of a code line.
      It is very important as Python uses indentation to indicate a block of code.
      If the indentation is not correct we will endup with IndentationError error.


# Predefine Functions --------------
   print -> this is a function (predefined)
   input -> predefined function in python

def -> def keyword indecate we are defining a function


when we want to write a function in one file and call them in another file
then we import that functin from that file 
for ex-> 

file name -> function.py
have 

def square(x) :
   return x*x

and another file  square.py
have call function -
for i in range(10):
    print(f"The square of {i} is {square(i)}")

then we import like this
from function import square , then square.py is something like this

from function import square
 for i in range(10):
    print(f"The square of {i} is {square(i)}")

------------or-----------
we can import entire function module like and we access that particular function by using function.square

import function
 for i in range(10):
    print(f"The square of {i} is {function.square(i)}")


'''
what is list in python?

1. Lists are order collection of data items.
2. This store multiple items in a single variable.
3. List item are seprated by commas and enclose with [] bracket.
4. List are changable , means we can alter them after creation.
5. List can store multiple data type ex. ['ashu', 23, True]

Example: -

list = [1,2,3,4,5]
print(list)
'''
################################################################
'''
Tuple: 
1.  Tuples are defined by enclosing the 
    elements in parentheses (()) instead of square brackets ([]).
2. Tuples are immutable means we can not alter them after creation
3. Tuple are order collection of data item. This store multiple item in single variable

ex-> 

tuple = ('ashu',23,'BCA','Students')
'''
#############################################################
'''
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store 
collections of data, the other 3 are List, Tuple, and Dictionary, 
all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

Set do not contain duplicate item.

* Note: Set items are unchangeable, but we can remove items and add new items.

'''

#########################################################################

'''
# Dictionaries ------------


dictionaries are order collection of data items. They store multiple item in single variable

Dictionaries item are key-value pairs that are seprated by commas  and enclose with curly braces {}
'''

dict = {
    'name': 'ashu',
    'age': 23,
    'class': 'BCA'
}

print(dict)

##############################################################################

# lambda Expression
'''
1. lambda is a keyword 
2. lambda expression are syntatically restricted to a single expression

syntax: 
lambda input: expression

no need of def keyword

no need of return keyword


lambda expression is just like a def function.
This is the short form to define a function.
Lambda expression is used to only that time when we dont need to reuse function

ex-> 
lambda a,b:a+b

call of lambda function
(lambda a,b: a+b)(5,6)
'''
######################################################################3