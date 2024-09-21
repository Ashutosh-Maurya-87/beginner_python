class Employee:
    '''class variable defines and value assign'''
    emp_name = 'Aashat'
    emp_age = 33
    emp_joiningDate = '12-22-2022'
    '''defining constructor'''
    def __init__(self,name,age,joinDate):
        self.name = name
        self.age = age
        self.joiningDate = joinDate

    def changeEmpName(self,newName):
        self.name = newName


    def changeJoiningDate(self,newDate):
        self.joiningDate = newDate


    def changeAge(self,newAge):
        self.age = newAge
    
    '''here we defined the class method by using @classmethod decorator'''
    @classmethod
    def changeEmpClassName(cls,newEmpName):
        cls.emp_name = newEmpName


    @classmethod
    def changeEmpClassAge(cls,newEmpAge):
        cls.emp_age = newEmpAge

    @classmethod
    def changeEmpJoiningDate(cls,newDate):
        cls.emp_joiningDate = newDate

    
    def showEmpDetailsInstanceMethod(self):
        print('value of employee through instance method and instance variable')
        print(self.emp_name)
        print(self.emp_age)
        print(self.emp_joiningDate)


    @classmethod
    def showEmpDetailsClassMethod(cls):
        print('vlaue of employee thorough the class method and class variable')
        print(cls.emp_name)
        print(cls.emp_age)
        print(cls.emp_joiningDate)


e = Employee('Aaditya Kumar',23,'12-22-2024')

# calling instance method
e.showEmpDetailsInstanceMethod()
'''
value of employee through instance method and instance variable
Aaditya Kumar
23
12-22-2024
'''
# updating the value of instance variables
e.changeAge(25)
e.changeEmpName('Akshat Kumar')
e.changeJoiningDate('15-10-2023')
print('After updating the instance variable value' )
e.showEmpDetailsInstanceMethod()
'''
After updating the instance variable value
value of employee through instance method and instance variable
Akshat Kumar
25
15-10-2023
'''

# calling class method
Employee.showEmpDetailsClassMethod()
'''
vlaue of employee thorough the class method and class variable
Aashat
33
12-22-2022
'''

# updating the value of class variable
Employee.changeEmpClassName("Aarush Kumar")
Employee.changeEmpClassAge(33)
Employee.changeEmpJoiningDate('22-11-2022')
print("After changing the value of class variable")
Employee.showEmpDetailsClassMethod()
'''
vlaue of employee thorough the class method and class variable
Aarush Kumar
33
22-11-2022
'''

# How we can delete any object 
# we use del keyword to delete any object
# del e
print(e.name); '''NameError: name 'e' is not defined'''