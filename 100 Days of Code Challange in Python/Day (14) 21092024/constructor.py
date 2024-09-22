

# Non-Parameterized constructor example
class ConstructorClass:
    def __init__(self):
        print('this is the constructor')

c = ConstructorClass(); '''this is the constructor'''


class ParameterizedConstructor:
    def __init__(self, name, age):
        self.name = name
        print('this is parameterized constructor', self.name, name, age)

p = ParameterizedConstructor('Ashu', 23); '''this is parameterized constructor Ashu Ashu 23'''

# if we dont make any constructor the python create by default a constructor automatically at the time of object creation
class DefaultConstructor:
    def AddFun(self, a,b):
        sum = a+b
        return sum
    

d = DefaultConstructor()
print(d.AddFun(56,44)); '''100'''