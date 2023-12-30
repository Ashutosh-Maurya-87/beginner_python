def Square(n):
    '''this function take a number and return that square, and i.e doc string not a comment'''

    print((n**2)); '''4'''
Square(2)

# to print the doc string, i.e written inside the function
print(Square.__doc__); '''this function take a number and return that square, and i.e doc string not a comment'''

''' Diffrence b/w comments and docString'''

# docstring

'''
Python docstring are strings used right after the defnition of the function, method ,class
or module . They are used to document our code

We can access these docstring using the doc attribute


if we write string just after function definition then we can say that is docstring otherwise not
ex= 
def add(a,b):
  ''''''number is added, now this string is docstring'''''''''
'''
def add(a,b):
  print(a, b)
    number is added, now this string is not docstring
'''



# Comments ---
'''
Comments are descriptions that helps programmers to better understant the functionalities of the program
They are completely ignored by python interpreter
'''