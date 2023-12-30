# f = open('myfile.txt', 'w')
# f.write('hello'); ''' this print hello inside the file'''
# re = f.read()
# print(re)
# f.close()

#  readline() method ---------
'''
readline method reads a single line from the file. If we want to read multiple line we can use loop

The readline method reads all the lines of the file and return them as a list of  string
'''
# f = open('myfile.txt', 'r')

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line); '''hello



# this written by ashu'''


f = open('marks.txt', 'r')
i=0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])
    print(f'Marks of the {i} students in the CS is:', m1)
    print(f'Marks of the {i} students in the Eng is:', m2)
    print(f'Marks of the {i} students in the Math is:', m3)

    '''
Marks of the 1 students in the CS is: 45
Marks of the 1 students in the Eng is: 87
Marks of the 1 students in the Math is: 89
Marks of the 2 students in the CS is: 55
Marks of the 2 students in the Eng is: 85
Marks of the 2 students in the Math is: 88
Marks of the 3 students in the CS is: 23
Marks of the 3 students in the Eng is: 45
Marks of the 3 students in the Math is: 78
    '''

# writelines() method ---
'''
The writelines() method in python write a seqquence of string to a file.
The sequence can be any iterable of object such as a list or a tuple.

'''

f = open('writelinefile.txt', 'w')
lines = ['line1\n', 'line2\n', 'line3\n', 'line4\n']
f.writelines(lines); '''this write the value of line in the file of writelinefile.txt'''
f.close()


# Keep in mind
'''the writelines() method does not add new line characters between the strings in the sequence.
if we want to add a new line between the string then, we can use a loop to write each string seprately.

'''

f = open('writelinefile.txt', 'w')
lines = ['line1 Ahu\n', 'line As\n', 'line Ashu\n', 'line4Maurya\n']

for line in lines:
    f.write(line+'Ashu Maurya')
f.close()