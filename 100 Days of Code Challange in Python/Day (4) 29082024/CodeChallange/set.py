
set1 = {1,2,3,4,5,9,8,'ashu'}
print(set1); 

'''
1st run: 
{'ashu', 1, 2, 3, 4, 5, 8, 9}

2nd run:
{1, 2, 3, 4, 5, 'ashu', 8, 9}

every time when we run the that item index is changed because set is unindexed
'''

set1 = {1,2,3,4,4,5,5,6,6,7,7,6,8}
print(set1); '''{1, 2, 3, 4, 5, 6, 7, 8}, bcause set does not contain duplicate value'''

# how to create a empty set
a = set(); '''this creates the empty set'''
print(a); '''set()'''
print(type(a)); '''<class 'set'>'''

# union() method
s1 = {1,4,5,2,3,5,7,1,4,5}

s2 = {4,5,6,1,2,3,4,1,4,5}

print('union method:',s1.union(s2)); '''union method: {1, 2, 3, 4, 5, 6, 7}'''
print(s1); '''{1, 2, 3, 4, 5, 7}'''
# union method does not update the original set, it only adjoint that from specified set, without duplicate value.

# update(one set is required, set2,set3...optional) method
s1 = {'blue','green','yellow','red'}
s2 = {'Orange','white','black','red'}
s1.update(s2)
print(s1); '''{'red', 'white', 'Orange', 'green', 'blue', 'black', 'yellow'}'''
# The update() method updates the original set by adding items from all the specified sets, with no duplicates.
# we can specify as many sets as you want, just separate each set with a comma.


# intersection() method
set1 = {1,2,2,3,3,4,4,5,5,8,8,9,9,4,4,3,3,2,2,33,4}
set2 = {1,2,2,33,4,55,44,22,2,1,2,3,444,55,66,77}
print(set1.intersection(set2)); '''{1, 2, 3, 4, 33}, contains only that item which is common in both set'''
set1 = {1,2,2,3,3,4,4,5,5,8,8,9,9,4,4,3,3,2,2,33,4}
set2 = {1,2,2,33,4,55,44,22,2,1,2,3,444,55,66,77}
set3 = {44,555,6666,7777,8888,333,555,333}
# set3 = {'ashu','aadi','dev','arush'}
print('intersection with multiple set',set1.intersection(set2,set3)); '''intersection with multiple set set(), 

it giving empty set because , not any item is matching in all the set'''

set1 = {1,2,2,3,3,4,4,5,5,8,8,9,9,4,4,3,3,2,2,33,444}
set2 = {1,2,2,33,4,55,44,22,2,1,2,3,444,55,66,77}
set3 = {444,555,6666,7777,8888,333,555,333}
print('intersection with multiple set',set1.intersection(set2,set3)); '''intersection with multiple set {444}'''
A = {'red', 'green', 'blue'}
B = {'yellow', 'orange', 'red'}
C = {'blue', 'red', 'black'}
print(A.intersection(B,C)); '''{'red'}'''

# intersection_update() method
s1 = {1,2,3,4,1,2,3,4,5,6,6,5}
s2 = {1,3,4,5,6,2,3,2,5,6,3,4}
s1.intersection_update(s2)
print('intersection update method',s1); '''intersection update method {1, 2, 3, 4, 5, 6}, it modified the original set'''