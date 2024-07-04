# Constructor ---------------------------------------------------
''''
Constructor is a special method in a class used to create and initialize an object of class.
there are different type of constructor.

Constructor is invoked automatically when an object of class is created.

The main purpose of constructor is to initialize or assign values to the data members of that class.
It can not return any value other than None.

Syntax of Python Constructor: =

def __init__(self):
    # initializations


init is one of the reserve  function in python. in OOP it is known as constructor .
We can also create function by definining the function name with same class name

ex-> 

class ABC:
   def ABC(self):
   
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%======%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Type Of Constructor --

1. Parameterized Constructor
2. Default Constructor


Parameterized Constructor
  When the constructor accept the arguments along with self, it is known as parameterized constructor
 These arguments can be used inside the class to assign the value to the data members


Default Constructor
  When the constructor does not accept any arguments form the object and has only one argument 'self' in the
  constructor it is known as Default constructor
'''

# this is a example of parametrized constructor
class Person:

    def __init__(self, n, o):
        print('Hey this is constructor'); '''Hey this is constructor'''
        self.name = n
        self.occ = o

    def info(self):
        print(f'{self.name} is a {self.occ}'); 
        '''
        Ashu is a Developer
        Khargosh is a Frontend Developer
        '''


a = Person('Ashu', 'Developer')
b = Person('Khargosh', 'Frontend Developer')
a.info()
b.info()


# Example of default constructor

class Details:

    def __init__(self):
        print('Animal')
    
obj = Details()

'''Output is +> Animals'''


















