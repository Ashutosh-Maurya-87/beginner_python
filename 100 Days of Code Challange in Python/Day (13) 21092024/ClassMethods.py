# Example: Define and call an instance method and class method
class Student:
    '''class variables'''
    name='Aayan'
    age=23
    st_id=1234
    rollNum= 45
    '''constructor'''
    def __init__(self,name,age,address):
        '''these are instance variables'''
        self.studentName = name
        self.studentAge = age
        self.studentAddress = address

    '''instance method'''
    def updateName(self,updatedName):
        self.studentName = updatedName

    @classmethod
    def changeAge(default, changedAge):
        default.age = changedAge

    def showStudentDetails(self):
        print(f'instance variable details, students details are:{self.studentName,self.studentAge,self.studentAddress}')
        print(f'class variable details, students details are:{Student.name, Student.age,Student.st_id, Student.rollNum}')


s = Student('Aarohit',22,'Hta House')

s.showStudentDetails()
'''
instance variable details, students details are:('Aarohit', 22, 'Hta House')
class variable details, students details are:('Aayan', 23, 1234, 45)
'''

s.studentAddress = 'Hat 123, USA'
print('updated value of student address is', s.studentAddress); '''updated value of student address is Hat 123, USA'''

s.updateName('Deeva Aadi')
s.showStudentDetails()
'''
instance variable details, students details are:('Deeva Aadi', 22, 'Hat 123, USA')
class variable details, students details are:('Aayan', 23, 1234, 45)
'''

# changing the value of class variables
Student.changeAge(55)
Student.name = 'Dada Jee'
Student.rollNum = 89
s.showStudentDetails()
'''
instance variable details, students details are:('Deeva Aadi', 22, 'Hat 123, USA')
class variable details, students details are:('Dada Jee', 55, 1234, 89)
'''