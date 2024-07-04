'''
Python Decorators are a powerful and versatile tool that allow we to modify the behaviour of function
and methods.
these are the way to extend the functionalities of the function or a method without modifying its source code


Decorator is a function that takes another function as an arguments and return a new function that modify 
the behaviour of the original function. Then new function is often refered to as a 'decorated' function.

Syntax: =

@decorator_function
def my_fun():
 pass

@decorator_function notation is just a shorthand of following code

def my_fun():
  pass

  my_fun = decorator_function(my_func)

Decorator are often used to add functionality to functions and method, such as logging,
memoziation and access control
'''
'''without decorator---'''

# def greet(fun):
#     def modifyFunc():
#         print("Good Morning")
#         fun()
#         print('Thanks for using this function')
#     return modifyFunc

# def hello():
#     print('Hello this is From Ashu')

# greet(hello)()
'''
output is

Good Morning
Hello this is From Ashu
Thanks for using this function
'''

# by using decorator

def greet(fun):
    def modifyFunc():
        print("Good Morning")
        fun()
        print('Thanks for using this function')
    return modifyFunc

@greet
def hello():
    print('Hello this is From hello func')

hello()
# greet(hello)()
'''
output is

Good Morning
Hello this is From Ashu
Thanks for using this function
'''

def myFunc(fn):
    def myInnerFunc(*args, **kwargs):
        # print(type(*args), type(**kwargs))
        print('this is inner my finction', *args, **kwargs)
        fn(*args, **kwargs)
        print('this is print at the end of the function')
    return myInnerFunc

@myFunc
def newFunc():
    print('this print inside the newFunc')

@myFunc
def add(a,b):
    print('sum of number is', a+b)
# myFunc(newFunc)()

newFunc()
add(1,5)

'''
Output is ->

this is inner my finction
this print inside the newFunc
this is print at the end of the function
this is inner my finction 1 5
sum of number is 6
this is print at the end of the function
'''










































