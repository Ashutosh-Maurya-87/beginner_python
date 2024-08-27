listOfComedian = ['Tiwari','Baburao','Raju','Shyam','Kachra Seth','Devi Parshad']
print(listOfComedian)

# travarsel in list
print(listOfComedian[2]); '''Raju'''

# print(listOfComedian[9]); '''IndexError: list index out of range'''

print(listOfComedian[-3]); 
'''Shyam, it give Shyam because if we do (length of list - given index number) then number is 3
 so 6-3 = 3 , now count from start of the list, so we start from 0 number then in the third number we have shyam
'''

print(listOfComedian[-4]); '''Raju'''

print(listOfComedian[-5]); '''Baburao'''

'''Or we can remember in another way, means if the given index is in minus (-) then , we count from back
ex- if we give -2 index number then we count from back of the list and start with 1 number
'''
print(listOfComedian[-2]); '''Kachra seth'''

# if we want to print list the we can write also this
print(listOfComedian[:]); '''['Tiwari', 'Baburao', 'Raju', 'Shyam', 'Kachra Seth', 'Devi Parshad']'''

# if we write 
print(listOfComedian[1:]); '''['Baburao', 'Raju', 'Shyam', 'Kachra Seth', 'Devi Parshad']'''
# bcz it skip the first item

print(listOfComedian[1:3]); '''['Baburao', 'Raju'], because it skip first item and print at the third index'''

print(listOfComedian[3:4]); '''[Shyam]'''
# now we check that whether Raju is present in the comedian list or not

if 'Raju' in listOfComedian :
    print('Raju is Present')
else :
    print('Raju is not present')

'''
Output of this program is: Raju is Present
'''

if 'as' in 'Ashutosh':
    print('Yes')
else :
    print('No')

''' output is:  No, because python is case sensitive language'''
# now how we can update a list


