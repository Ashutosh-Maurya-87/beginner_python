'''
finally keyword

   whichever we write inside the finally keyword that is excute all time
'''

# -------------------------finally clause
'''
The finally code block is also a part of exception handling.
When we handle exception using the try and except block, we can include a 
finally block at the end. The finally block is always excuted so it is generally used 
for doing the concluding task like closing file resources or closing database connection 
or may be ending the program excution with a delightful message


SYNTAX ----
 try:
    statements which coukd generate exception
 except:
    solution of generated exception 
 finally:
    block of code which is going to excute in any situation
'''

try:
    a = [1,2,3,4]
    print(a)
except:
    print('except block')

finally:
    print('finally block, it will excute always')

'''in the above example which is written inside the finally block that will print'''

def func():
 try:
    l = [1,2,3,5,4,5,6]
    guess = input('enter the index number to find that value')
    print('your number is',l[int(guess)])
    return 1
 except:
    print('Some error occurred')
    return 0

 finally:
    print('i will be excuted at every time')

x = func()
print('return function',x)

'''
output of above example ------
enter the index number to find that value ff
Some error occurred
i will be excuted at every time
return function 0

enter the index number to find that value 4
your number is 4
i will be excuted at every time
return function 1
'''
