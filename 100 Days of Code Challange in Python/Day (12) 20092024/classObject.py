
class firstClass:
    firstname = 'Ashu'
    age:24
    add:'ar'

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