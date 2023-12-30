'''
what is list in python?

1. Lists are order collection of data items.
2. This store multiple items in a single variable.
3. List item are seprated by commas and enclose with [] bracket.
4. List are changable , means we can alter them after creation.
5. List can store multiple data type ex. ['ashu', 23, True]

Example: -

list = [1,2,3,4,5]
print(list)
'''

list_Of_Cid_team = ['ACP Parduman', 'Abhijeet', 'Daya','Shreya','Purvi','Pankaj','Tarika','Salunkhe','Fredicks','Sachin']

print('if user give index in minus (-)', list_Of_Cid_team[-3]); ''' output is : Salunkhe'''
print('if user give index in minus (-)',list_Of_Cid_team[len(list_Of_Cid_team) -3]); ''' output is: Daya '''

# program to check 'Tarika' is in the cid list or not
if 'Tarika' in list_Of_Cid_team:
    print('Yes! tarika is in the team😊')
else :
    print('No😒 tarika is not in the list')

if 'As' in 'Ashutosh':
    print('yes')
else:
    print('No')


marks = [45,5,78,54,77,26]

'''
listName[start index or zero index : end index]

listName[start index or zero index : end index : jump index]

jump index is optional, if we write jump index in the list to print the list 
  then it jumps that given count from the list
'''
print('all the value of marks', marks); '''[45,5,78,54,77,26]'''

print('all the value of marks, we can write also as', marks[:]); '''[45,5,78,54,77,26]'''

print('value of marks start from 1st index and print after 1st index to last index', marks[1:]); '''[5,78,54,77,26]'''

marks= [1,4,5,7,8,96,2,3,6,45,23,97,45,23,48,12,23,56]
print('marks from 1 index to 8 index', marks[1:8]); '''[4,5,7,8,96,2,3]'''

print('list using jump index', marks[1:8:2]); '''4,7,96,3'''


# List Comprehension ------

# Syntax
'''
list = [Expression(item) for item in iterable if condition]

Expression => It is the item which is being iterated

Iterable => it can be list, tuple, dictionaries,sets and even in array and strings

Condition => Condition check if the item should be added to the new list or not
'''

lst = [i for i in range(4)]
print(lst); '''[0,1,2,3]'''

number = [i*i for i in range(8)]
print(number); '''[0,1,4,9,16,25,36,49]'''


number = [i*i for i in range(10) if i%2 == 0]
print(number); '''[0,4, 16,36,64]'''