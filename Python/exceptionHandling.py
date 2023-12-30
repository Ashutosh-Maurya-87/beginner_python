num = (input('Enter the number:'))
print('Table of entered number is')
try:
  for i in range(1,11):
    print(f'{int(num)} X {i} is', int(num) * (i))
except Exception as e:
  print('invalid input', e, Exception); '''invalid literal for int() with base 10: 'your input' <class 'Exception'>'''
