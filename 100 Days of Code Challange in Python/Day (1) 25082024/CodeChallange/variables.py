# define the variable

a = 5
print('this is number type varibale', a)
print('Python automatically find , which type of value is storing in the variable',type(a)); '''<class 'int'>'''

a = 'ashu'
print(a, type (a)); '''ashu <class 'str'>'''

# type casting from number to string
x=4
a = str(x)
print(a, type(a)); '''4 <class 'str'>'''

# type casting from string to number
x='Ashu'
# a= int(x)
# print(a, type(a)); 
'''a= int(x)
       ^^^^^^
ValueError: invalid literal for int() with base 10: 'Ashu'

because string type value is not type cast, 

to change from string to number we use 1-9 value
'''
x='3'
a= int(x)
print(a, type(a)); '''3 <class 'int'>'''

x= float(a)
print(x, type(x)); '''3.0 <class 'float'>'''

