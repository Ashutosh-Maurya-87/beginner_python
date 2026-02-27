
class Test:
    def __init__(self,vegitable,fruit) -> None:
        self._veg = vegitable
        self._fruit = fruit

    def get_veg(self):
        return self._veg
    
    def set_veg(self,val):
        self._veg = val

    def get_fruit(self):
        return self._fruit
    
    def set_fruit(self,value):
        self._fruit = value

obj = Test('Potato','Apple')
print('veg is', obj.get_veg()); '''veg is Potato'''
obj.set_veg('Tomato')
print('updated veg is',obj.get_veg()); '''updated veg is Tomato'''
print(obj.get_fruit()); '''Apple'''
print(obj._fruit);'''Apple'''
