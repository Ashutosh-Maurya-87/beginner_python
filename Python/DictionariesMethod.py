'''
Dictionaries Methods------
'''

# to create a empty dictionary
emptyDict = {}
print(emptyDict) 


# update() method -------------
'''
The update() method updates the value of the key provided to it 
if the items already exist in the dictionaries, else it creates a new
key-value pairs
'''

dict = {
    "name": 'Ashu',
    'age': 23,
    "class": "MCA"
}
dict.update({"age": 22})
print(dict); '''{'name': 'Ashu', 'age': 22, 'class': 'MCA'}'''

dict.update({"dob": '11-09-2000'}); '''it create new key, bcz there is no key with the name of dob'''
print(dict); '''{'name': 'Ashu', 'age': 22, 'class': 'MCA', 'dob': '11-09-2000'}'''

'''#######################################'''

shift1 = {111: "40 hrs/week", 112: '42 hrs/week', 113: '43 hrs/week'}
shift2 = {222: '45 hrs/week', 223: '44 hrs/week'}

shift1.update(shift2)
print(shift1); '''{111: '40 hrs/week', 112: '42 hrs/week', 113: '43 hrs/week', 222: '45 hrs/week', 223: '44 hrs/week'}'''

# clear() method removes all the items from the list

dict = {
    "name": 'Ashutosh',
    'age': 23,
    "class": "MCA"
}
dict.clear()
print('clear() method', dict); '''clear() method {}, print empty curly braces'''

# pop() method
# shift1.pop() '''TypeError: pop expected at least 1 argument, got 0
shift1.pop(111)
# print(shift1); 
print(shift1); 
'''{112: '42 hrs/week', 113: '43 hrs/week', 222: '45 hrs/week', 223: '44 hrs/week'}'''

# popitem() method removes the last key-values pair from the dictionaries----
shift = {
    12: '1st shift',
    13: '2nd shift',
    14: '3rd shift'
}

# shift.popitem(13); '''TypeError: dict.popitem() takes no arguments (1 given)

shift.popitem()
print('popitem() method print', shift); 
'''popitem() method print {12: '1st shift', 13: '2nd shift'}'''

# del keyword delete the dictionaries
# del shift
# print(shift); '''NameError: name 'shift' is not defined. Bcz del keyword delete the disctionary'''

dict = {
    "name": 'Ashu Maurya',
    'age': 23,
    "class": "MCA",
    455: '12 miles'
}

del dict['age']
# del dict['455']
# print(dict); '''KeyError: '455'''
print(dict); '''{'name': 'Ashu Maurya', 'class': 'MCA'}'''




































