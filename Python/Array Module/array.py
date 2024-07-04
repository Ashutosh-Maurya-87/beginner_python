from array import *

# a1 = array(typeCode, [elements])

'''
type code      C type

'b'  -------   signed integer
'B'  -------   unsigned integer

'u'  -------   unicode character

'h'  -------   signed integer
'H'  -------   unsigned integer

'i'  -------   signed integer
'I'  -------   unsigned integer

'l'  -------   signed integer
'L'  -------   unsigned integer

'q'  -------   signed integer
'Q'  -------   unsigned integer

'f'  -------   floating point
'd'  -------   floating point
'''

a1 = ('i', [55,88,99])
print(a1); '''('i', [55, 88, 99])'''

print(type(a1)); '''<class 'tuple'>'''

a1 = array('i', [55,88,99])
print(a1); '''array('i', [55, 88, 99])'''
print(type(a1)); '''<class 'array.array'>'''

for i in a1:
    print(i);'''55  88  99'''