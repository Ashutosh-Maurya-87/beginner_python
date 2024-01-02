'''
# Dictionaries ------------


dictionaries are order collection of data items. They store multiple item in single variable

Dictionaries item are key-value pairs that are seprated by commas  and enclose with curly braces {}
'''

dict = {
    'name': 'ashu',
    'age': 23,
    'class': 'BCA'
}

print(dict)
print(dict['name']); '''ashu'''
print('dict get method',dict.get('name')); '''ashu'''

# to access all keys, keys()
print(dict.keys()); '''dict_keys(['name', 'age', 'class'])'''
print(dict.values()); '''dict_values(['ashu', 23, 'BCA'])'''

for key in dict.keys():
    print('key are', key); '''name   age   class'''
    print(dict[key]); '''ashu  23  BCA'''

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''
items()  method print all key-value pairs in the dictionaries.
'''
print(dict.items()); '''dict_items([('name', 'ashu'), ('age', 23), ('class', 'BCA')])'''

for key, value in dict.items():
    print(f'the value are corresponding to the key {key} is {value}'); 

'''
the value are corresponding to the key name is ashu
the value are corresponding to the key age is 23
the value are corresponding to the key class is BCA
'''











