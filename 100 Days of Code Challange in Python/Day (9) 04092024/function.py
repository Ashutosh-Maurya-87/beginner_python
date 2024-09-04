
# predefined function
# takeInput = input('enter any thing')

# In python we defined function using def keyword

# definition of function, normal function, without parameter
def name() :
    print('we defined our first function')

# calling function
name()

# function with parameter

def greet(msg) :
    print(f'hello Good Morning! {msg}')

greet('Ashutosh'); '''ello Good Morning! Ashutosh'''

# Default arguments in the function
def add(a=5,b=6) :
    print('function with default arguments', a + b)

add(); '''function with default arguments 11'''
add(10,20); '''after adding it give 30, because it ignore the default vaue and take the passed value whatever we pass
during calling the function, if we don't pass any value then it take default value and print that''' 
'''
function with default arguments 11
function with default arguments 30
'''

# Required length Arguments in Funtion
def avg(a,b,c) :
    print('average is:',(a+b+c)/3)

avg(10,10,10); '''average is: 10.0'''
l = [1,2,3,4,5]
greet(l); '''hello Good Morning! [1, 2, 3, 4, 5]'''

# Variable lenth arguments
'''if we add * and then parameter name, then function take value as a tuple, and we can pass multiple argument,
while calling the function'''
def AvgOfMoreNUmber(*num) :
    sum = 0
    for x in num:
        sum = sum + x
    print('average of numbers is:', sum/len(num))

AvgOfMoreNUmber(1,2,3,4,5,6,7,8,9,10); '''average of numbers is: 5.5'''

# Keywords arguments function
def keyWordArgumentFunction(name1,name2,name3) :
    print('keyword argument function', name1, name2, name3)

# This way the order of the arguments does not matter.
keyWordArgumentFunction(name1 = 'Ashutosh', name2='Aadi', name3='Ranji'); '''keyword argument function Ashutosh Aadi Ranji'''
keyWordArgumentFunction(name2='ashu',name1='ashutosh',name3='ashutosh maurya'); '''keyword argument function ashutosh ashu ashutosh maurya'''
