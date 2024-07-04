# Class Variable -
''' Class variable are defined at the class lavel and are shared among all the instances of the class.
They are defined outside of any method and are usually used to store information that is common to all instance
of the class.

For example: A class variable can be used to store the number of instance of a class that have been created.
'''

# Instance variable -
'''
Instance variable are defined at the instance level and are unique to each instance of the class.
They are defined inside the init method and are usually used to store information that is specific to each instance of the class.
For Example: -
  An instance variable can be used to store the name of an employee in a class that represent an employee
'''

class Employee:
    companyName = 'Microsoft'; '''this is class variable'''
    noOfEmployee = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployee += 1

    def showDetails(self):
        print(f'name of employee is {self.name} and the raise amount is {self.raise_amount} and company name is {self.companyName} and no of emp is {self.noOfEmployee}')

emp = Employee('Ashu')
# emp.showDetails(); '''name of employee is Ashu and the raise amount is 0.02'''
# Employee.showDetails(emp); '''name of employee is Ashu and the raise amount is 0.02'''
emp.name = 'Ashutosh Maurya'
emp.companyName = 'Google'
emp.showDetails(); '''name of employee is Ashutosh Maurya and the raise amount is 0.02 and company name is Google'''

emp2 = Employee('Aditya')
emp2.showDetails(); '''name of employee is Aditya and the raise amount is 0.02 and company name is Microsoft'''
# emp.showDetails()

# after adding noOfEmployee output is:
'''
name of employee is Ashutosh Maurya and the raise amount is 0.02 and company name is Google and no of emp is 1
name of employee is Aditya and the raise amount is 0.02 and company name is Microsoft and no of emp is 2
'''

'''here for first employee company name is change but for second not, its happen because for first employee "emp" object have
instance variable and for second "emp2" have not any instance variable , 
when python run then its check if there is any instance
variable then that value got changed otherwise it take the value of the class variables
'''
