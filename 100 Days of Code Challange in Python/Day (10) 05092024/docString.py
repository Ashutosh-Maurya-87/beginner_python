
def qube(n) :
    '''this is docstring, i.e. write just after the function definiton. This is not a comment'''

    print('qube of number is:', n*n*n); '''qube of number is: 27'''

qube(3)
# now we are accessing the docString
print('docstring is:', qube.__doc__); '''docstring is: this is docstring, i.e. write just after the function definiton. This is not a comment'''


def Check() :
    '''this is docstring'''
    '''this is comment, because its not just after function definiton'''
    print('hello')
    '''this is comment'''

Check()
print(Check.__doc__); '''this is docstring'''