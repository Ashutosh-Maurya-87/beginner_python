
# dictionaries define
dict = {
    "name":'ashu',
    "course":'BCA',
    "Add":'Ayodhya'
}

print(dict)

# to print single value from the dictionaries
print(dict['Add']); '''Ayodhya'''

# to print the single value using get method
print(dict.get('course')); '''BCA'''

# to print the key name
print(dict.keys()); '''dict_keys(['name', 'course', 'Add'])'''

# to print the value name
print(dict.values()); '''dict_values(['ashu', 'BCA', 'Ayodhya'])'''

# dictionaries items() method, if we need to show key and value both the we use items() method
''' items() method print the all key value pair in the dictionaries'''
print(dict.items()); '''dict_items([('name', 'ashu'), ('course', 'BCA'), ('Add', 'Ayodhya')])'''

# Some more important method in Dictionaries

# how to create a empty dictionaries
emptyDictionary = {}
print('Empty dectionaries', emptyDictionary); '''Empty dectionaries {}'''

# if we want to update a dictionary
# we use update() function
emptyDictionary.update({
    'name':'Ashu',
    'lastName':'Maurya'
})
print('updated dictionaries', emptyDictionary); '''updated dictionaries {'name': 'Ashu', 'lastName': 'Maurya'}'''

# if we want to modified existing value then also we use update() method
emptyDictionary.update({
    'name':'Ashutosh',
    'age':23
})
print('after updation existing value, if exist then update it otherwise added it in the last',emptyDictionary)

'''
Output: 
fter updation existing value, if exist then update it otherwise added it in the last {'name': 'Ashutosh', 'lastName': 'Maurya', 'age': 23}
'''

# if we want to clear dictionaries data then
# we use clear() method
print('after clear the dictionaries:',emptyDictionary.clear()); '''after clear the dictionaries: None'''
emptyDictionary.clear()
print('after clear method:', emptyDictionary); '''after clear method: {}'''

# if we want to delete any specific item from dictinaries
# the we use pop() method, its accept a key name as a parameter
newDict={
    'id':123,
    'name':'Aditya',
    'Add':'heart',
    'comedy':'Chin Tapak dum dum😊'
}
newDict.pop('id'); '''it remove that ecpecific item which key name we will provide'''
print(newDict); '''{'name': 'Aditya', 'Add': 'heart', 'comedy': 'Chin Tapak dum dum😊'}'''

# if we want to delete any key-value from the last then we use
# popitem() method
newDict.popitem(); ''' it don't expect any key name as a parameter'''
print(newDict); '''{'name': 'Aditya', 'Add': 'heart'}'''