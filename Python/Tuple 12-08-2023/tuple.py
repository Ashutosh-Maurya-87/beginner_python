'''
Tuple: Tuples are defined by enclosing the 
        elements in parentheses (()) instead of square brackets ([]).
    2. Tuples are immutable means we can not ulter them after creation
    3. Tuple are order collection of data item. This store multiple item in single variable
'''

tuple = ('ashu',23,'BCA','Students')
print(type(tuple), tuple); '''<class 'tuple'>, ('ashu', 23, 'BCA', 'Students')'''

# intersting thing in tuple
tup = (2)
print(type(tup), tup); '''<class 'int'>, 2  if we write only one value in the tuple then
python convert it into the integer, 

To overcome this problem, we will add extra comma after that one value, then python understand
this is tuple like -> tup(2,)
'''
tup = (2,)
print(type(tup), tup); '''<class 'tuple'> (2,)'''

print(tuple[0]); '''ashu'''
print(tuple[1]); '''23'''
print(tuple[2]); '''BCA'''

# important ,  positive indexing and negative indexing is same like list in the tuple

print(tuple[-2]); '''BCA'''
print(tuple[len(tuple) - 3]); '''23'''

if 'ashu' in tuple:
    print('Yes ashu is in tuple')


tup1 = tuple[1:3]
print('new tuple', tup1); '''(23, 'BCA')'''

newTup = (1,25,35,44,55,6,22,55,88)
print('tuple from 0 to 6', newTup[0:6])
print('using jumping in tuple', newTup[0:6:2]); '''(1,35,55)'''