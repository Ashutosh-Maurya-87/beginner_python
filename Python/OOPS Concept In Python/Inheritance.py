# Inheritance---
'''
When a class derive from another class. The child class will inherit all the public and protected 
properties and method from the parent class. In addition, it can have its own properties and methods
this is called as inheritance.

Syntax->
  class BaseClass:
    body of base class

  class DerivedClass(BaseClass):
    body of derived class


Type of inheritance
1, Single
2. Multiple
3. Multilevel
'''

class parent_class:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f'the name of employe is : {self.name} and id is: {self.id}')

e1 = parent_class('ashu', 12)
print('e', e1)
e1.showDetails(); '''the name of employe is : ashu and id is: 12'''


class derived_class(parent_class):
    def showLang():
        print(f'language is python')


e2 = parent_class('Ashu Maurya', 22)
e2.showDetails(); '''the name of employe is : Ashu Maurya and id is: 22'''
e3 = derived_class('child',1)
e3.showDetails(); '''the name of employe is : child and id is: 1'''



























