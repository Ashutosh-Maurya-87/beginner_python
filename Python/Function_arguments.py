'''
this is multiline comment ----

There are four type of function arguments --
1. Defaults Arguments
2. Keyword Arguments
3. Variable length Arguments
4. Required length Arguments
'''

# Default Arguments ---
'''This is a default arguments in the function ---'''
def average(a = 6, b = 4):   
    print('average is',a,b, (a+b)/2)   
# average(6,4)
average(); '''average is 5.0'''
average(3,5); '''average is 4.0 because it ignore the default value 6,4 and take 3,5 as respectively'''
average(5); ''' here it takes a = 5 and b = 4'''
average(b=7); ''' here it takes a = 6 and b = 7'''


# Required Arguments ---
'''This is a required arguments in the function because if we not pass argument in the function
then it give the error , so that reason this is required arguments in the function---'''
def average(a, b):   
    print('average is', (a+b)/2)

average(6,4)

# Variable length arguments ---

'''here it takes number as an tuple'''
def averageOfMoreNumber(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print('aaverage of many number is', sum/len(numbers))

averageOfMoreNumber(5,5, 8)