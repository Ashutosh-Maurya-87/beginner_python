# Seek and tell function in python
'''these method are builtin io module.'''
# seek() funtion ------------
'''
the seek() function allows to move the current position within a file to a specific point.
The position is specified in bytes and we can move either forward or backward from the current position 
'''

# tell() funtion =================
'''
tell() function return the current position within the file  in bytes.
This can be useful for keeping track of our location within the file or for seeking to a specific position
relative to the current position.
'''

# eample of seek() function
with open('test.txt', 'r') as f:
    # this is used to write somting inside the file by using python file method
    # f.write('123456789eashumaurya')

    # move to the 10th byte in the file
    f.seek(10)

    currentPosition = f.read()
    # Read the next 5 byte from that seek point
    data = f.read(5)
    print(data); '''ashum'''



# eample of tell() function
with open('test.txt', 'r') as f:
    # this is used to write somting inside the file by using python file method
    # f.write('123456789eashumaurya')

    # move to the 10th byte in the file
    f.seek(10)

    currentPosition = f.tell()
    print('current posiiotn', currentPosition); '''10'''
    # Read the next 5 byte from that seek point
    data = f.read(5)
    print(data); '''ashum'''


# truncate (छाँट कर छोटा करना) function ---
    '''when we open the file in the python by using open function, we can specify the mode in which mode
    we want to open the file. If we specify the mode as 'w' or 'a' the file is opend in write mode and we can
    write to the file . However we want to truncate(छाँट कर छोटा करना) the file to a specific size we can use the truncate function
    '''

with open('newFile.txt', 'w') as a:
    a.write('Hello Ashu Maurya this is truncate file')

    # define the size of file
    a.truncate(5); '''by using this we can store only 5 character in inside the file'''

with open('newFile.txt', 'r') as b:

    # before truncate the file

    # print(b.read()); '''Hello Ashu Maurya this is truncate file'''

    # after truncate the file
    print(b.read()); '''Hello'''