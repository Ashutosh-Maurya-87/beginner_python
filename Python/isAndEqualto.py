# is in python
'''
is opertor =>  return the location of the variable means it check the address of the variable is same in the memory
               or not. if memory location is same then its return the True else False
               CHECK EXACT LOCATION OF OBJECT IN MEMORY

== operator =>  check the value if value is same then its return the True or false, 
                it not check the memory location , 
'''

a = 4
b = 4

print(a is b); '''True'''
print( a == b); '''True'''

l = [1,5,4]
nl = [1,5,4]

print(l is nl); '''False because in the memory location both variable store value in the different memory location'''
print( l == nl); '''True  because the value of both list is same, and address is not same'''

ab = None
ba = None

print(ab is ba); '''True'''
print( ab == ba); '''True'''

print(ab or ba is None); '''True'''