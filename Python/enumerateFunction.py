# Enumerate function
'''
THe enumerate function is a built-in function in python that allow
we to loop over a sequence (such as a list, tuple or string)
and get the index and value of the each element in the sequence
at the same time . 

Ex -> 
'''
# program without enumerate fuction
marks = [50,45,89,55,45,55,66,99]

index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print('ashu marks', mark)
    index +=1

# program with enumerate fuction
for index, mark in enumerate(marks):
    print(mark, index)
    if(index == 3):
        print('ashu marks', mark)
    index +=1


# output is ---
'''
50 0
45 1
89 2
55 3
ashu marks 55
45 4
55 5
66 6
99 7
'''

# changing the start index ---
'''
By default the enumerate function start from 0 index , 
but we can specify a different starting index by passing
it as an argument to the enumerate function
'''
print('changing the start index')
for index, mark in enumerate(marks, start = 3):
    print(index, mark)
    if(index == 3):
        print('ashu marks', mark)
    index +=1


'''
here index value is start from 3,

we need not to confuse that marks of value will be print after 
3rd index, simply we are changing the starting index value not the print
value of mark


3 50
ashu marks 50
4 45
5 89
6 55
7 45
8 55
9 66
10 99
'''



