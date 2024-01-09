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
















