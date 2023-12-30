# Variable ----
'''
A Variable is a named location in memory that stores a value.
'''

# Local Variable ---
'''
A local variable is a variable that is define within a function and is only accessible within that 
function. It is created when the function is called and destroyed when the function is returns.
'''

# Global variable ---
'''
A global variable is a variable that is define outside the function and is accessible from any
function within code.
'''

x = 4
def func():
    x=5
    print('value of x inside the function: ', x); '''5'''
func()
print('value of x outside of the function: ', x);'''4'''

# changing the value of global variable
x = 4
def func():
   global x 
   x=6
   print('value of x inside the function: ', x); '''6 bcz global change the value of global variable x'''
func()
print('value of x outside of the function: ', x);'''6  bcz global change the value of global variable x'''