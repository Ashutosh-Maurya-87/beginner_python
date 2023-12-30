s1 = {1,5,3,4,6,9,8,7}

s2={1,2,5,8,7,4,1,3,6,9}

print(s1.union(s2)); '''{1, 2, 3, 4, 5, 6, 7, 8, 9}'''
print('update union',s1.update(s2))
print(s1.intersection(s2)); '''{1, 3, 4, 5, 6, 7, 8, 9}'''
print(s1, s2)
# to update the set

city1 = {'Ayodhya', "Aus", "Usa", 'Tokyo', 'Rus'}
city2 = {'India', "Aus", "Usa", 'Tokyo', 'Rus', 'Lucknow'}
city1.intersection_update(city2)

print(city1); '''{'Rus', 'Tokyo', 'Usa', 'Aus'}, city 1 is update'''
print(city2); '''{'Rus', 'Tokyo', 'Usa', 'Aus', 'India', 'Lucknow'}'''

cities3 = city1.symmetric_difference(city2); '''symmetric difference give the uncommon value from the set'''
print(cities3); '''{'Lucknow', 'India'}'''

city1 = {'Ayodhya', "Aus", "Usa", 'Tokyo', 'Rus'}
city2 = {'India', "Aus", "Usa", 'Tokyo', 'Rus', 'Lucknow'}
city1.symmetric_difference_update(city2); '''give uncommon value and update the city1'''
print('symmetric update',city1); '''{'Ayodhya', 'Lucknow', 'India'}'''

# issuperset ---------------
'''
the issuperset() method checks if all the item of paraticuler set are present in the 
origional set. It return True if all the item are present else it return False
'''

city1 = {'Ayodhya', "Aus", "Usa", 'Tokyo', 'Rus'}
city2 = {'India', "Aus", "Usa", 'Tokyo', 'Rus', 'Lucknow'}
print('issuperset',city1.issuperset(city2))
city3 = { "Aus", "Usa", 'Tokyo', 'Rus'}
print('is superset 3',city1.issuperset(city3)); '''True, because all the value of city3 is present in city1 '''

print('is subset',city1.issubset(city3)); '''False'''
print('is subset',city3.issubset(city1)); '''True, bcz city3 is subset of city1'''


# add() method to add item in the set
city1.add('ashu')
print(city1); '''{'ashu', 'Ayodhya', 'Aus', 'Tokyo', 'Rus', 'Usa'} or {'Rus', 'Usa', 'ashu', 'Tokyo', 'Ayodhya', 'Aus'}'''


# remove() method to remove item in the set
city2.remove('India')
print('remove',city2); '''{'Tokyo', 'Usa', 'Rus', 'Aus', 'Lucknow'}'''

# discard() method to remove item in the set
city2.discard('Aus')
print('discard',city2); '''discard {'Usa', 'Tokyo', 'Lucknow', 'Rus'}'''

# The main difference between remove() and discard() is that
#  if we try to delete the item which is not present in the set, then remove() raise an error
#  but discard() does not raise error


#  pop() method, remove item form the last, but the catch is that we dont know gets poped in the unordered set
print(city1.pop()); '''Rus'''
res = city1.pop()
print(res); '''ashu'''
print(city1); '''{'Tokyo', 'Rus', 'Usa', 'Ayodhya'}'''

# del method to delete entire the set
cities = {'India', 'Bharat'}
# del cities
print(cities)

'''
Name cities is not define we get an error because our entire set has been deleted and
there is no variable called cities which contain a set

'''

# clear() method --- clear all item from the set
cities = {'India', 'Bharat'}

print('clear',cities.clear()); '''None'''


if 'ashu' in city1:
    print('Yes')
else :
    print('No')