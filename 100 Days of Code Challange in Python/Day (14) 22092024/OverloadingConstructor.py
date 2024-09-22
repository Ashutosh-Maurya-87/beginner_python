# Python does not support the constructor overloading

# We use constructor channing to overcome this problem

class Vehicle:
    '''constructor of Vehicle class'''
    def __init__(self, engine) -> None:
        print('inside Vehicle constructor')
        self.engine = engine


class Car(Vehicle):
    '''constructor of Car class'''
    def __init__(self, engine, speed) -> None:
        print("inside Car constructor")
        super().__init__(engine)
        self.speed = speed

class ElectricCar(Car):
    '''constructor of ElectricCar'''
    def __init__(self, engine, speed, range) -> None:
        print('inside the electric car class constructor')
        super().__init__(engine, speed)
        self.range = range

o = ElectricCar('2000 cc',200,1000)
print(f'the engine of a car is {o.engine} and speed is {o.speed}km/h and range {o.range}')
'''
inside the electric car class constructor
inside Car constructor
inside Vehicle constructor
the engine of a car is 2000 cc and speed is 200km/h and range 1000
'''