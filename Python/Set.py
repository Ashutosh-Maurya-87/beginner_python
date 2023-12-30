# Set ---------

'''
Set do not maintain the order of element
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store 
collections of data, the other 3 are List, Tuple, and Dictionary, 
all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

Set do not contain duplicate item.

* Note: Set items are unchangeable, but you can remove items and add new items.

'''

set1 = {1,5,3,1,4,5,'ashu'}

print(set1); '''{1, 3, 4, 5, 'ashu'} bcz set does not contain duplicate value'''

# to create a empty set
s = set();'''this create empty set'''
print(type(s)); '''<class 'set'>'''

#  accessing the value of set ---

for v in set1:
    print(v); '''1
                 ashu
                 3
                 4
                 5'''
    
