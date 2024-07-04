# ACCESS SPECIFIER OR ACCESS MODIFIER ====
''' this is used in the python to limit the access of class variable and class methods outside of the class
while impleminting the concept of inheritance'''

# Public Specifier/Modifier
'''All the variable and method in the python are by default public.
Any instance variable of the class followed by the self keyword i.e self.var_name are publically acessed'''

class public_class:
    def __init__(self):
        self.name = 'Ashu'

obj = public_class()
print(obj.name); '''Ashu'''


# Private Modifier ====
'''
In python there is not strict concept of the 'private' modifer like the other OOPS language.
But however a convention has been established to indecate that a variable or method should be considered
private by prefixing the (__) double underscore before the variable name.
This is known as 'WEAK INTERNAL USE INDECATOR' and it is a convetion only not a strict rule.

But code outside the class still can be accessed these private variable and method.
But generally understoood that they can not access or modified.
'''

class Emp:
    def __init__(self):
        print('this is emp class')
        self.__name = 'Ashutosh Maurya'

e = Emp()
# print(e.name); 
'''
this is emp class
Traceback (most recent call last):
  File "D:\imp\beginner_python\Python\OOPS Concept In Python\AccessModifier.py", line 34, in <module>
    print(e.name)
          ^^^^^^
AttributeError: 'Emp' object has no attribute 'name'
'''
print(e._Emp__name); '''Ashutosh Maurya, by using _className we can access'''


# NAME MANGLING ========
'''
Name Mangling in the python is a techinque used to protect class-private and superclass-private
attribute from being accedently overwritten by subClass

Name of class-private and superclass-private attributes are transformed by the addition of a single adding
underscore and adding double underscore respectively.

'''

class NameManglingClass:
    def ___init__(self):
        self.__privateattributes = 'I am a private attribute'
        self.__mangled_attributes = 'I am a mangled attribute'


obj1 = NameManglingClass()
# print('mangled attribute',obj.__mangled_attributes); '''throw an attribute Error'''
print('private attribute',obj1._NameManglingClass__privateattributes); '''throw an attribute Error'''


# Protected Modifier ============================================
'''
In OOP the term 'protected' is used to describe a member (i.e method or attribute) of a class that is intended
to be accessed only by the class itself and its subclasses.

In python the convention for indicating that a member is protected is to prefix its name with a single
underscore(_).

For ex. -> 
if a class has a method called _my_method it is indecating that the method should be accessed 
only by the class itself and its subclass.

It is important to note that the single underscore is just a naming convention, and does not actually
provide any protection or restrict access to the member or method. 

The syntax we follow to make any variable protected is to write variable name followed by a single 
underscore (_) i.e _varName
'''
































