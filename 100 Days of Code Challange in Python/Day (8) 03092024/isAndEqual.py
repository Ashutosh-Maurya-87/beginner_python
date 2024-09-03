a = '4'
b = '5'
print(a is b); '''False'''
print(a == b); '''False'''

a = 45
b = 45
print('is operator',a is b); '''True, because python does not create different memory allocation for the same value, it locate only and update that '''
print(a == b); '''True'''

# list case
l = [1,2,3]
nl = [1,2,3]
print('memory address of l is', id(l))
print('memory address of nl is', id(nl))
'''
memory address of l is 2011591169280
memory address of nl is 2011592751808
'''
print('is operator', l is nl); '''is operator False, because if we do same by using list then its create
 another memory allocation for each list, so that reason it give false
'''
print(l == nl); '''True, because the value of list is same, but address is not same'''

a = None
b = None
print(a is b); '''True'''
print(a == b); '''True'''

print(a or b is None); '''True'''

# tuple case
t = (1,2,3,'four')
t2 = (1,2,3,'four')
print('is operator in tuple',t is t2); '''is operator in tuple True'''
print('address of t is ', id(t)); '''address of t is  1907473916256'''
print('address of t2 is ', id(t2)); '''address of t2 is  1907473916256'''

'''so that reason it give true'''

# dictionaries case
a = {
    'name':'Ashu'
}
b = {
    'name':'Ashu'
}
print('memory address of a is', id(a)); '''memory address of a is 2273729597696'''
print('memory address of b is', id(b)); '''memory address of b is 2273731049728'''
print(a is b); '''False'''
print(a == b); '''True, bcz value is same'''

# set case
s = {1,2,3,4}
s1 = {1,2,3,4}
print('memry address of s is', id(s)); '''memry address of s is 1713130868960'''
print('memry address of s1 is', id(s1)); '''memry address of s1 is 1713130868064'''
print(s is s1); '''False'''
print(s == s1); '''True'''