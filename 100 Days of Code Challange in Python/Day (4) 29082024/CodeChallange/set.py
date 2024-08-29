
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
