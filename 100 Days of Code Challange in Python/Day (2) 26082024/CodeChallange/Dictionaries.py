
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