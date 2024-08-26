
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

# if we want