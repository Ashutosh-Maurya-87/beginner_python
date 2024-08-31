
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

# symmetric_difference(set1,set2 is optional) method
s = {'Ashu','Aadi','Dev','Aarush'}
s1 = {'Aaruhi','Aranji','Adheera','Roohani'}
print(s.symmetric_difference(s1)); 
''' it print all the name because all name is not common in both set
{'Adheera', 'Aaruhi', 'Roohani', 'Aadi', 'Ashu', 'Aranji', 'Aarush', 'Dev'}'''
s1 = {'Aaruhi',"Ashu",'Aranji','Adheera','Roohani'}
print(s.symmetric_difference(s1)); '''{'Dev', 'Aadi', 'Aranji', 'Roohani', 'Aaruhi', 'Aarush', 'Adheera'}''' 

# symmetric_difference_update(set1,set2 is optional) method
set12 = {'Ashu','Aadi','Dev','Aarush'}
set123 = {'Aaruhi','Aranji','Adheera','Roohani'}
set12.symmetric_difference_update(set123)
print('symmetric difference update', set12); 
'''
its update the original set, set12
symmetric difference update {'Adheera', 'Aaruhi', 'Aranji', 'Aarush', 'Ashu', 'Roohani', 'Dev', 'Aadi'}
'''

# issuperset(set1, set2...) method
city = {'ayodhya','lucknow','ghaziabad'}
city2 = {'ayodhya','lucknow','ghaziabad'}
print(city.issuperset(city2)); '''True'''
city3 = {'ayodhya','lucknow','ghaziabad','noida'}
print(city.issuperset(city3)); '''False'''

# issubset(set1,set2...) method
d = {'Ayodhya','Lucknow','Amh','ADI'}
d2 = {'Lucknow','AYC','AMH','ADI'}
print('issubset',d2.issubset(d)); '''False,  all item of set d2 is not present in the set d'''

A = {1,2,3,4,5,6}
B = {1,2,4,5,6}
print(B.issubset(A)); '''True, because all item of set B is present in the set A'''
print(A.issubset(B)); '''False, because all item of set A is not present in the B set'''

# add() method
A={12,23,12,3434,454,6}
A.add(44444)
print('after adding a value', A); 
'''after adding a value {23, 454, 6, 44444, 3434, 12}, 
it can add at any places in the set because we know this is unindexed'''

# A tuple can be added in a set
S = {'red', 'green', 'blue'}
S.add((1, 2))
print('after adding tuple',S)
'''
after adding tuple {'red', 'green', (1, 2), 'blue'}
'''

# But list can’t be a set item
S = {'red', 'green', 'blue'}
# S.add([1, 2]), this give errror
'''Triggers TypeError: unhashable type: 'list'''

# remove() method
S1 = {'Lal','Hara','Neela','Peela'}
S1.remove("Hara")
print('after remove',S1); '''after remove {'Neela', 'Lal', 'Peela'}'''

# discard() method
S1 = {'Lal','Hara','Neela','Peela'}
S1.discard('Blue')
print('discard method',S1); '''discard method {'Lal', 'Hara', 'Neela', 'Peela'}, it not give error '''
# S1.remove('Blue')
print(S1); '''KeyError: 'Blue', remove method give key error '''


# pop() method
city = {'ayodhya','lucknow','ghaziabad','Agartala'}
print('pop method',city.pop()); '''pop method ayodhya,  because it remove random item, so that can be from first or last or any other places'''
x = city.pop()
print(x); '''ayodhya, can me any value'''
print(city); '''{'ayodhya', 'Agartala'}, can be any item in the set, don't get confused'''


# del method to delete entire the set
cities = {'India', 'Bharat'}
# del cities
print(cities); '''NameError: name 'cities' is not defined'''

# clear() method
cities = {'India', 'Bharat'}

print('clear',cities.clear()); '''None'''