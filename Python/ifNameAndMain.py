'''
The if __name__ == "__main__" idioms is a common pattern used in python scripts to determine wheter
the script is being run directly or being imported as a module into another script


In Python the __name__ variable is a built-in-variable that is automatically set to the name 
of the current module . When a python script run directly the __name__ variable is set to the 
string __main__ . When the script is imported as a module into another script,
the __name__ variable is set to the name of the module 

'''

def ashu():
    print('this is welcome string')

print('__name__', __name__)

'''
output 1 ---
PS D:\imp\Python> python ifNameAndMain2.py
__name__ ifNameAndMain
this is welcome string

output 2 ---
PS D:\imp\Python> python ifNameAndMain.py 
__name__ __main__
this is welcome string
'''

'''by using this ashu() function is called only one time and this print only one time'''
if __name__ == "__main__":
    ashu()


'''
In this example the function contains code that should be run when the script is run directly.
The if statement at the bottom checks whether the __name__ variable is equal to "__main__". if it 
is the main function is called
'''
# importMethod2nd.welcome('ashu')


# Why it is useful ---------
'''
it is useful because it allows you to reuse code from a script by importing it as a module
into another script, without running the code in the original script. 
'''