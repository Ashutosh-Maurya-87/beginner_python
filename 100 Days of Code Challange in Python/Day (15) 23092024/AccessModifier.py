# public data member

class TenthClass:
    def __init__(self,name) -> None:
        print('this is public data member')
        self.name = name; '''this is public data member, it can be access anywhere inside and outside of the class'''
    # public instance method
    def show(self):
        print(f'the name you have provided is {self.name}')


t = TenthClass('Ashutosh Maurya'); '''this is public data member'''
x = t.show()
print(x); '''the name you have provided is Ashutosh Maurya, after that None* confuse in this None why it return this'''




# Private Data member

class Emp:
    def __init__(self, name, salery) -> None:
        # public data member
        self.name = name
        # private data member
        self.__salery = salery


obj = Emp('Aadi',100000)
print(f'accessing the name of emp: is {obj.name}'); '''accessing the name of emp: is Aadi'''
# As we know , we can't access the private member outside of the class, so that it give attribute error
# print(f'salery of emp is: {obj.__salery}'); '''AttributeError: 'Emp' object has no attribute '__salery'''

# We can access private members from outside of a class using the following two approaches
# 1. Create public method to access private members
# 2. Use name mangling


# Creating a public method inside the class to acccess the private data member

class Emp:
    def __init__(self, name, salery) -> None:
        # public data member
        self.name = name
        # private data member
        self.__salery = salery

    def show(self):
        print('employee name is', self.name,'and salery is:', self.__salery)

em = Emp('Ashutosh', 1000000)
em.show(); '''employee name is Ashutosh and salery is: 1000000'''


# Name Mangling to access private or protected data member
# syntax -> objectName._className__dataMemberName

class Emp:
    def __init__(self, name, salery) -> None:
        # public data member
        self.name = name
        # private data member
        self.__salery = salery

employee = Emp('Aaditya',5555555)
print(f'employee name is {employee.name} and salery is {employee._Emp__salery}')
'''
employee name is Aaditya and salery is 5555555
'''


# Protected Data Member

class Company:
    def __init__(self):
       
        # protected data member
        self._salery = 999999
       

class Emp(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print('name of emp is', self.name, 'salery is', self._salery)

obj = Emp('Ashu')
obj.show(); '''name of emp is Ashu salery is 999999'''
