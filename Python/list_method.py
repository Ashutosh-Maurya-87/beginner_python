# list methods ----

l = [1,2,5,4,8]
print('list before append',l); '''[1,2,5,4,8]'''

l.append(45)
print('list after append',l); '''[1,2,5,4,8,45]'''

l = [45,88,74,5,1,89,455, 89]
l.sort()
print('list after sorting', l); '''[1, 5, 45, 74, 88, 89,89, 455]'''

l.sort(reverse=True)
print('sorting in Descinding order', l); '''[455, 89,89, 88, 74, 45, 5, 1]'''

l.reverse()
print('list after reverses',l)

print('index method take the value and give that index of first occurence',l.index(89))

# count method

print('count(value) method give the counting of that value', l.count(89))


# copy method in list ----

# pro way ---
m = l
m[0] = 0
print('modified the old list and assign 0 in the first index of list', l); ''' [0, 5, 45, 74, 88, 89, 89, 455]'''
print('m list', m); ''' [0, 5, 45, 74, 88, 89, 89, 455]'''

a=[7,89,5,4,88,456,12,56,88,999,45,12,65,256,6]
n = a.copy(); '''copy() method make a copy of exist list'''
print('new copy list',n)
n[0] = 0
print(n); '''[0, 89, 5, 4, 88, 456, 12, 56, 88, 999, 45, 12, 65, 256, 6]'''
print('old list i.e not changed ', a); '''[7, 89, 5, 4, 88, 456, 12, 56, 88, 999, 45, 12, 65, 256, 6]'''

# insert(index, value) method 
a.insert(2,'ashu')
print('list after inserting a value', a); '''[7, 89, 'ashu', 5, 4, 88, 456, 12, 56, 88, 999, 45, 12, 65, 256, 6]'''

# extends(name of list or empty) 
'''
This method add an entire list or any other collection datatype(set,  tuple, dictionary) to the 
existing list
'''

newList = ['ashu','maurya']
list = ['Bca', 'students']

# newList.extend(list)
# print('list after adding ', newList); '''['ashu', 'maurya', 'Bca', 'students']  here newList is changed'''

# if we want to that our newList not changed then
a = newList + list
print('without changing the old list', a, newList, list); '''['ashu', 'maurya', 'Bca', 'students']
['ashu', 'maurya'], ['Bca', 'students']
'''