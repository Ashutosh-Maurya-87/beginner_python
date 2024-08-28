list = [1,3,4,5,2,2,1,4]

# append method
list.append(45)
print(list); '''[1, 3, 4, 5, 2, 2, 1, 4, 45]'''

# if we want to add in the first index then
list[0] = 66
print(list); '''['66', 3, 4, 5, 2, 2, 1, 4, 45]'''

# if we want to sort the list then
list.sort()
print('it sort in ascending order', list); '''it sort in ascending order [1, 2, 2, 3, 4, 4, 5, 45, 66]'''

# if we want to sort in descending order then
list.sort(reverse=True)
print(list); '''[66, 45, 5, 4, 4, 3, 2, 2, 1]'''

# or
list.reverse(); '''it reverse that list, it does not check that list is sort or not it only reverse that'''
print(list); '''[66, 45, 5, 4, 4, 3, 2, 2, 1]'''

#index(value) method
a = list.index(66)
print('it give the index of 66:', a); '''it give the index of 66: 8'''

# count(value) method
print(list.count(4)); '''it give the how many time that given value is occure:  2'''

#copy method in list
# if we write 
m = list
m[0] = 99
print(list); '''then it also modified the original list as : [99, 2, 2, 3, 4, 4, 5, 45, 66]'''
print(m); '''and m list is also same: [99, 2, 2, 3, 4, 4, 5, 45, 66]'''

# copy method
l = list.copy()
print('new list is', l); '''new list is [99, 2, 2, 3, 4, 4, 5, 45, 66]'''

# if we want to modified that list, it does not change the original list
l[0] = 100
print('new copy list',l); '''new copy list [100, 2, 2, 3, 4, 4, 5, 45, 66]'''
print('original list', list); '''original list [99, 2, 2, 3, 4, 4, 5, 45, 66]'''

#insert(index, value) method in the list 
l.insert(4, 'ashu')
print(l); '''[100, 2, 2, 3, 'ashu', 4, 4, 5, 45, 66]'''

# extends(name of list or empty) method
'''
This method add an entire list or any other collection datatype(set,  tuple, dictionary) to the 
existing list
'''

newList = ['ashu','maurya']
list = ['Bca', 'students']

newList.extend(list)

print(newList); '''['ashu', 'maurya', 'Bca', 'students']'''

# we can also write as
print(newList+list); '''['ashu', 'maurya', 'Bca', 'students']'''

l.extend('')
print(l); '''[100, 2, 2, 3, 'ashu', 4, 4, 5, 45, 66]'''