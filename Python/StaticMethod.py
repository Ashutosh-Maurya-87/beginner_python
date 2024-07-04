'''
Static method in python are method that belongs to a class rather than an instance of class.
They are defined using the @staticmethod decorator and do not have access to the instance of class (i.e self).
    They are called on the class itself , not an instance of the class.

    Static method are often used to create utility function that don't need to acess to the instance data.

    we can call static method without use of a obj, we can call directly with that parameter
'''

class Math:
    def __init__(self, num):
        self.num = num

    def addNum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        print('add')
        return a+b


a = Math(6)
a.addNum(5)
print(a.num);'''11'''
print(Math.add(4,5)); '''9'''
print(a.add(3,5)); '''8'''