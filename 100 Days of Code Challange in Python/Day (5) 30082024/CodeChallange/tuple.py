tup = (1,3,4.5,6)
print('tuple is',tup); '''tuple is (1, 3, 4.5, 6)'''

# create empty tuple
t = ()
print('empty tuple is', t); '''empty tuple is ()'''
print('if we print that type then it give', type(t)); '''if we print that type then it give <class 'tuple'>'''


# intersting thing in tuple
tup = (2)
print(type(tup), tup); 
'''<class 'int'>, 2  if we write only one value in the tuple then
python convert it into the integer, 

To overcome this problem, we will add extra comma after that one value, then python understand
this is tuple like -> tup(2,)
'''
tup = (2,)
print(type(tup), tup); '''<class 'tuple'> (2,)'''

tup = ('ashu','44444','9999999',99999)
print(tup[0]); '''ashu'''
print(tup[1]); '''44444'''
print(tup[2]); '''9999999'''
print(type(tup[2])); '''<class 'str'>, because value is in string'''
# print(type(tup[2,])); '''TypeError: tuple indices must be integers or slices, not tuple'''

# if we give positive index and negative index then it work like list, because this is same in list and tuple
print('after giving index in negative',tup[-2]); '''after giving index in negative 9999999'''

t = (1,2,3.4,5,6,7,4,3,2,'ashu',45,6,7,3)
print(t[1:]); '''(2, 3.4, 5, 6, 7, 4, 3, 2, 'ashu', 45, 6, 7, 3)'''
print(t[1:3]); '''(2, 3.4)'''
print(t[1:8:2]); '''(2, 5, 7, 3), third value is jumping , means we want to skip that number of value'''
print(t[:]); '''(1, 2, 3.4, 5, 6, 7, 4, 3, 2, 'ashu', 45, 6, 7, 3)'''
print(t[0:5]); '''(1, 2, 3.4, 5, 6)'''
