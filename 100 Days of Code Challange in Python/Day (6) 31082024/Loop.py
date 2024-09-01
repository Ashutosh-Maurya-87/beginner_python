for x in 'Ashutosh' :
    print(x)
'''
A
S
h
u
t
o
s
h
'''
# if else inside for in loop
for x in [1,2,3,4,5,6,7,5] :
    if x == 4 :
        print('we did here something different')
    else :
        print('number of list is:',x)

'''
number of list is: 1
number of list is: 2
number of list is: 3
we did here something different
number of list is: 5
number of list is: 6
number of list is: 7
number of list is: 5
'''

# print number from 1 to 10
for i in range(10) :
    print('number',i)

# nested for in loop--
# print table from 1 to 10
'''we write here 11 because range function start from 0 and go up to that (given number - 1) place'''
for i in range(1,11):
    for j in range(1,11):
        print(f'table of {i}X{j} is', i * j)

colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    print(x)
else:
    print('Done!')
'''
red
green
blue
yellow
Done!

because when index of list is done then it check another index whether that have valu or not
'''
'''here we have else method , we write here because if loop is completed then else is excuted'''
for x in colors:
    print(x)
else:
    print('Done!',x)

'''
red
green
blue
yellow
Done! yellow
'''


# nested for..in in nested list
l = [[1,2,3,4,5,5],[2,3,4,5,6,7],[34,55,33,44,66,77]]
for i in l :
    for x in i :
        print('after nested value',x)


'''
after nested value 1
after nested value 2
after nested value 3
after nested value 4
after nested value 5
after nested value 5
after nested value 2
after nested value 3
after nested value 4
after nested value 5
after nested value 6
after nested value 7
after nested value 34
after nested value 55
after nested value 33
after nested value 44
after nested value 66
after nested value 77
'''
l = [[1,2,3,4,5,5],[2,3,4,5,6,7],[34,55,33,44,66,77]]
for i in l :
    print('here is the value of i',i)
    for x in i :
        print('after nested value',x)
'''
here is the value of i [1, 2, 3, 4, 5, 5]
after nested value 1
after nested value 2
after nested value 3
after nested value 4
after nested value 5
after nested value 5
here is the value of i [2, 3, 4, 5, 6, 7]
after nested value 2
after nested value 3
after nested value 4
after nested value 5
after nested value 6
after nested value 2
after nested value 3
after nested value 4
after nested value 5
after nested value 5
here is the value of i [2, 3, 4, 5, 6, 7]
after nested value 2
after nested value 3
after nested value 4
after nested value 5
after nested value 6
after nested value 2
after nested value 3
after nested value 4
after nested value 5
after nested value 6
after nested value 4
after nested value 5
after nested value 6
after nested value 5
after nested value 6
after nested value 6
after nested value 7
here is the value of i [34, 55, 33, 44, 66, 77]
after nested value 34
after nested value 55
after nested value 33
after nested value 44
after nested value 66
after nested value 77
'''
# how to print table from 1 to 20 in python

for x in range(1,21) :
    for y in range(1,21) :
        print(f'the table of {x}X{j} is:', x*j)

# access index in loop
a = [12,34,5,2,4,3,22]
for x in range(len(a)) :
    print('index is',x,'value is',a[x])

'''
index is 0 value is 12
index is 1 value is 34
index is 2 value is 5
index is 3 value is 2
index is 4 value is 4
index is 5 value is 3
index is 6 value is 22
'''

# left triangle using loop
# for x in range(1,6) :
#     for y in range(1,x+1) :
#         print('*')
#         print('')