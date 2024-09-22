# What is Constructor
* Constructor is a special method used to create and initialize the object of a class.
1. Constructor is excuted automatically when the object is created
2. For example, when we execute obj = Sample(), Python gets to know that obj is an object of class Sample and calls the constructor of that class to create an object.

# Syntax of Python Constructor: =

def __init__(self):
    # initializations


* __init__ is one of the reserve  function in python. in OOP it is known as constructor .
* We can also create function by definining the function name with same class name

1. Internally, the __new__ is the method that creates the object
2. And, using the __init__() method we can implement constructor to initialize the object.

# Types of Constructors
In Python three types of constructors.

1. Default Constructor
2. Non-parametrized constructor
3. Parameterized constructor

# Default Constructor
Python will provide a default constructor if no constructor is defined. Python adds a default constructor when we do not include the constructor in the class or forget to declare it. It does not perform any task but initializes the objects. It is an empty constructor without a body.

If you do not implement any constructor in your class or forget to declare it, the Python inserts a default constructor into your code on your behalf. This constructor is known as the default constructor.

It does not perform any task but initializes the objects. It is an empty constructor without a body.

# Non-Parametrized Constructor
A constructor without any arguments is called a non-parameterized constructor. This type of constructor is used to initialize each object with default values.

This constructor doesn’t accept the arguments during object creation. Instead, it initializes every object with the same set of values.
* example: -> def __init__(self):
* self refers to the current object.

# Parameterized Constructor
A constructor with defined parameters or arguments is called a parameterized constructor. We can pass different values to each object at the time of creation using a parameterized constructor.
* example: ->  def __init__(self, value1, value2.value3 ...):
