# Getter ---------
'''
Getter in python are methods that are used to access the value of an object's properties. They are used to
return the value of a specific property and are typically defined using the '@property' decorator.

Example of simple getter method->

class MyClass:
    def __init__(self, value):
          self._value = value
    
    @property
    def value(self):
       return self._value


       In this example, the MyClass class has a single property _value, which is initialized in the init method.
       The value method is defined as a getter using the @property decorator and used to return the value of the
       _value property.

       To use the getter, we can create an instance of the MyClass class,and then access the value property
       as if it were an attribute

       obj = MyClass(10)
       obj.value

       output: 10
'''

class MyClass:
    def __init__(self, value):
          self._value = value
          print('inside the init')

    def show(self):
        print(f' value is {self._value}'); '''value is 20'''
    
    @property
    def value(self):
       return self._value
    


obj = MyClass(20)
obj.show()
print(obj.value); '''20'''

print(obj._value); '''20'''


# Setter -------------------------------------
'''
It is important to note that the getters do not take any parameters and we can not set the value
through getter method.

For that we need setter method which can be added by decorating method @property_name.setter

ex of getter and setter =>

'''

class MyNewClass():
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value


'''@value.setter set the value to the value function'''
obj = MyNewClass(50)
print('setter method',obj.value); '''setter method 50'''
obj.value = 100
print('in setter method after setting the value',obj.value); '''in setter method after setting the value 100'''

