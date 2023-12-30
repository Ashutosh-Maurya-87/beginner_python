a = int(input('input first number'))
b = int(input('input second number'))
def findGreater(a,b):
  print('greater number is:',a) if a > b else print('small number is:',b) if a < b else print('number are equal')

findGreater(a,b)

'''
short-hand syntax can be a convenient way to write if-else statement in one line

however it is not suitable for more complex logic, on that case we need to use full if-else statment 
'''