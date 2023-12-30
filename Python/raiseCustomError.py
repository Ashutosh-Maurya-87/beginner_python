'''
In python we can raise custom error by using raise keyword
'''

# Example ----------
num = int(input('enter the number between 5 to 10'))

if(num < 5 or num > 10):
    print(num)
    raise ValueError('Value should be between 5 to 10')
else:
    print('value is', num)


'''
enter the number between 5 to 10 78
78
Traceback (most recent call last):
  File "D:\imp\Python\raiseCustomError.py", line 10, in <module>
    raise ValueError('Value should be between 5 to 10')
ValueError: Value should be between 5 to 10
'''

num = input('enter the number:')

if(num == 'quit'):
    print('you have type:',num)
elif(int(num) < 5 or int(num) > 10):
    print(num)
    raise ValueError('Value should be between 5 to 10')
else:
    print('value is', num)

'''
program that take sting quit but not give the error
enter the number:quit
you have type:  quit
'''
  
# read more about raising error --> https://docs.python.org/3/library/exceptions.html