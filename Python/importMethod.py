# import pandas
# print(pandas)
from importMethod2nd import welcome, varName
welcome('Ashu maurya')
print('this is coming from another file', varName)


# The dir function ---
'''
Finally python has a built in function called dir that we can use to 
view the names of all the functions and variables define in a module.
'''
import math as built_inMethod
res = built_inMethod.floor(5.9988)
print('built_inMethod', res); '''built_inMethod 5, we can write any name in the place of built_inMethod'''
#  first method ---------------
import math
res = math.sqrt(16)
print('math', res); '''math 4.0'''

# To print all the function of the imported method ---
print('dir all math method',dir(math))
'''
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 
'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 
'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 
'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 
'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 
'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 
'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 
'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
'''
# Second method -----------
'''We can also import only specific function by using from keyword'''
from math import sqrt, pi

res = sqrt(9) * pi

print(res, pi); '''9.42477796076938 3.141592653589793'''

# Third method -----------
from math import floor as f
print(f(4.5599)); '''4'''