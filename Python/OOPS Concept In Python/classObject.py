'''
To create class in the python , we use class keyword

ex-> 
 
class Person:
   name = 'Ashu'
'''

# how to create an object in the python
'''
Object are the instance of class used to acess the properties of the class

ex to create an object -

obj = Person()
'''

class Person:
    name = 'Ashu'
    occupation = 'Software Engineer'
    age = 23

obj = Person()

# update the value 
obj.age = 22

print('acces the name', obj.name); '''access the name Ashu'''

print('Updated  Age is:  ', obj.age); '''Updated  Age is:   22'''

# Self parameter in python
'''
The self parameter is a reference to the current instance of the class and is used to access 
variable that belongs to the class

It must be provied as the extra parameter inside the method defination

Ex->
'''

class Details:
    name = 'Ashutosh'
    age= 20
    occupation = 'Software developer'

    def desc(self):
        print('My name is ', self.name, 'and i am a', self.occupation); 
        '''My name is  Ashutosh and i am a Software developer
        My name is  Khargosh and i am a Eat Carrot
        '''


obj1 = Details()

obj1.desc()

obj2 = Details()

obj2.name = 'Khargosh'
obj2.occupation = 'Eat Carrot'

obj2.desc()



'''
Class Object variable -> we can call this as Static Variable

Instance Object Variable -> Initially this vaiable is empty

class object object is a instance variable 
'''

# Make Instance object variable

class Test():
    x = 7
    def f1(self):
        pass
    @staticmethod
    def f2():
        print('Hello this is f2 function')
    @classmethod
    def f3(clsMthod):
        print('clsMethod',clsMthod.x)

t1 = Test()
t2 = Test()
Test.f3(9); '''class method function called'''
t1.f1()
Test.f2(); '''static method function called'''
t1.f2()

'''
f1() -> is a instance Method

instance method is called by instance object t1

f2() -> is a static method

f3() -> is a class method and clsMethod is a variable it can be any name
we make this for specific task of class

'''










