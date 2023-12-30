# we can add,delete,update the tuple, but need to change that tuple in the list
#  and the we can do, and after performing the fuctinalities we convert that list 
#  again to the tuple

tup = ('ashu',1,4,5,"India")

temp = list(tup); '''here we convert tuple to list'''
print(type(temp))

temp[4] = 0; 
print(temp); '''['ashu', 1, 4, 5, 0]'''
temp.append('Russia')
print(temp); '''['ashu', 1, 4, 5, 0, 'Russia']'''

# now we again convert list to tuple
tup = tuple(temp)
print(tup); '''('ashu', 1, 4, 5, 0, 'Russia')'''

# tuple.count method in tuple, tupleName.count(value)
#  it check how many occurence of that value is present in the tuple

tup = (1,2,3,5,4,1,2,3,2,6,5,2,1,1,2,3,3,2,1,1)
print('count of 2 in tuple',tup.count(2)); '''number of 2 present in the tuple i.e count of 2 in tuple 6 time'''

# index() method in tuple
print('index of 3 is',tup.index(3)); '''give the first occurence index in the tuple i.e index of 3 is 2'''

# index(value, startIndex, endIndex)
res = tup.index(3, 4, 9); 
print('index of 3 between 4th index to 9th index is',res); '''index of 3 between 4th index to 9th index is 7'''












