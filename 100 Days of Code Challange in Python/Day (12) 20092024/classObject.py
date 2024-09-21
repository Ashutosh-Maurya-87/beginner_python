
class firstClass:
    firstname = 'Ashu'
    age=24
    add='arr name'

obj = firstClass()
print('bject is', obj); '''bject is <__main__.firstClass object at 0x000002191B94E7D0>'''
print('object is', obj.firstname); '''object is Ashu'''


# How we update the value inside the class by using object
obj.add = 'Gzb'
print('value update ', obj.add); '''value update  Gzb'''


# self parameter in the function of class

class tenthClass:
    istLession = 'A girl with the basket'
    teacher = 'Khargosh'
    time = '40 mins'
    def englishFun(self):
        print('tody you will learn', self.istLession,'with tacher name',self.teacher,'in the time of',self.time)


t = tenthClass()
t.englishFun(); '''tody you will learn A girl with the basket with tacher name Khargosh in the time of 40 mins'''

t1 = tenthClass()
t1.time = "25 mins"
t1.englishFun(); '''tody you will learn A girl with the basket with tacher name Khargosh in the time of 25 mins'''


class studentDetails:
    '''these are class variables'''
    name = 'Aadi'
    gender = 'male'
    hobbies = 'Cricket and Riding'

    '''constructor'''
    def __init__(self,name,gender,hobbies,age,address):
        '''these are instance varibales'''
        self.name = name
        self.gender = gender
        self.hobbies = hobbies
        self.age = age
        self.address = address


s = studentDetails('deva','male','skiting',22,'haridwar')
'''access of instance variable'''
print('stuent details', s.name)
print('stuent details', s.gender)
print('stuent details', s.hobbies)
'''
stuent details deva
stuent details male
stuent details skiting
'''

print('stuent details', s.age)
print('stuent details', s.address)
'''
stuent details 22
stuent details haridwar
'''

# Accessing the class variables
print('class variable student details', studentDetails.name)
print('class variable student details', studentDetails.gender)
print('class variable student details', studentDetails.hobbies)
'''
class variable student details Aadi
class variable student details male
class variable student details Cricket and Riding
'''

class test:
    num = 5
    '''instance method'''
    def add(self,a,b):
        self.a=a
        self.b=b
        sum = self.a+self.b
        return sum
    
t = test()

'''instance method caling '''
print('t value',t.add(2,5)); '''t value 7'''


print('valkue of a is', t.a)
print('valkue of a is', t.b)
'''
valkue of a is 2
valkue of a is 5
'''
# by using class name we can access the class variables
print('class variables value is', test.num); '''class variables value is 5'''

# Modify class variables
test.num = 78
print('modified value of class variables:', test.num); '''modified value of class variables: 78'''