class Google:
    degination = 'Software Developer'
    def __init__(self) -> None:
        # protected data member
        self._id = 125

class Employee(Google):
    def __init__(self, name, salery) -> None:
        self.name = name
        self.__salery = salery

o = Employee('Raju',5000)
print('employee name is', o.name); '''employee name is Raju'''
print('Salery is:', o._Employee__salery); '''Salery is: 5000'''


class Employee2(Google):
    def __init__(self) -> None:
        Google.__init__(self)

    def show(self):
        print('id is', self._id)
        
obj = Employee2()
obj.show(); '''id is 125'''

