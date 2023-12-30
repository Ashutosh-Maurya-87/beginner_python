# lambda Expression
'''
1. lambda is a keyword 
2. lambda expression are syntatically restricted to a single expression

syntax: 
lambda input: expression

no need of def keyword

no need of return keyword


lambda expression is just like a def function.
This is the short form to define a function.
Lambda expression is used to only that time when we dont need to reuse function

ex-> 
lambda a,b:a+b

call of lambda function
(lambda a,b: a+b)(5,6)
'''

# IF WE WANT TO REUSE THE LAMBDA EXPRESSION THEN
f1 = lambda a,b: a+b
print(f1); '''<function <lambda> at 0x000001D0F1BA04A0> at ke baad wala lambda expression ki id hai hexadecimal me'''

print(f1(5,8)); '''13'''
print(f1(8,8)); '''16'''

# function using def
def add(a,b):
    a+b
x = add
print(x); '''<function add at 0x0000021F8DACD8A0>'''

print(id(x)); '''2357749405696 this is the refrence id of that add function'''
print(id(add)); '''2357749405696 this is the refrence id of that add function'''

# program of find factorial using recursion function
def fact(a):
    if a == 0 or a==1:
        return 1
    else:
        return a*fact(a-1)

print('fact is',fact(4))

# Write a program of factorial by recursion using lambda expression 
f = lambda a: 1 if a ==0 or a ==1 else a*f(a-1)
print('factorial using lambda expression',f(5)), '''factorial using lambda expression 120'''




























