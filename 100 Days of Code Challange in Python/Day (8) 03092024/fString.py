l = 'India is my country {}'
print(l); '''India is my country {}'''
name = 'Ashu'
name2 = 'Aadi'
print('my first name is {name} and second name is {name2}'); '''my first name is {name} and second name is {name2}'''

# but if we use fString
print(f'my first name is {name} and {name2}'); '''my first name is Ashu and Aadi'''

text = 'value to 2 decimal {price: .2f} dollers'

print(text.format(price = 24.980099)); '''value to 2 decimal  24.98 dollers'''

price = 34.563445
print(f'value of price in 2 decimal palces is: {price: .2f}'); '''value of price in 2 decimal palces is:  34.56'''

print(type(f"{10*29}")); '''<class 'str'>'''

print(f"{10*29}"); '''290'''

# to show {} using fstring
print(f'i am going to show {{price}} inside the curly braces'); '''i am going to show {price} inside the curly braces'''