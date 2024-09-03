userInput = input('Enter the value which you want')
print('entered value is ', userInput)
'''
Enter the value which you want ashu
entered value is   ashu, while entring we give space , so that reason it give space then entered name
'''

number = input(f'enter the number')
'''while input the number , variable take value as a string'''
print(type(number)); '''<class 'str'>'''
'''so we convert that in number'''
x = int(number)
if x % 10 == 0 :
    print('number is divide by 10')
else :
    print('number is not divide by 10')

