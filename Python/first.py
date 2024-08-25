print('hello Ashutosh')

# this is comment (we can comment like this in python)
# Array
array = ['ashutosh', 'maurya', 'software']

print(array[0])
# to add value in the last index of array we use Array.append
array.append('engineer')
print(array)

#to sort we use sort function
array.sort()
print('sort array', array)


#creating a empty set in python
s = set()
# to add a value in the set we use .add method and pass the value inside add
# and .add function take only one argument not two or more
# s.add(1, 2) this give error but s.add(1) givs no error
s.add(1)
s.add(7)
s.add(480)
s.remove(1)
print(s)

#dectinoaries in python --
houses = {'ashu': "Mauryan's House", 'Ashutosh': 'maurya house'}

# adding more on this house object then 
houses["ashutoshmaurya"] = 'Benglow'
print('ashu house is',houses['ashu'])
print(houses)

#in python we can take input by using input ex-
name = input('enter your name')
print('h', name)