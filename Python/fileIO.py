# Opening a file ---
'''
Before we can any operation on file, we need to first open it. Python provide the function open()
function to open a file. It takes two arguments, 
first the name of the file and second is the mode
means in which mode we want to need to open the file
'''
# By default the open function return a file object that can be used to read or write to the file
 
# f = open('file.txt', 'r')

# print(f); '''<_io.TextIOWrapper name='file.txt' mode='r' encoding='cp1252'>'''

# res = f.read()
# print(res); '''Hey there this is a file to test that file is open or not, this is the output of file.txt'''
# f.close()

# Modes in file ----
'''
1. read (r): This mode open the file for reading only and give an error if the file does not exist.
             This is the default mode if no mode is passed as a parameter

2. write (w): This mode open the file for writing only and 
              create a new file if the file does not exist.

3. append (a): This mode open the file for appending only and 
              create a new file if the file does not exist

4. create (x): This mode creates a file and give an error if the file already exist

5. text (t): Apart from these modes we also need to specify how the file must be handled .
             t mode is used to handle text files. t refers to the text mode. There is no difference
             between r and rt or w and wt since text mode is the default. 
             The default mode is r(open for reading text, synonym of 'rt') 

6. binary (b): used to handle binary files (images, pdf etc)

A) with statement ==> Alternatevly we can  use the with statment to automatically close the file 
                     after we are done with it.
'''
with open('file.txt', 'a') as f:
    f.write('this is inside of the with, and append in the last of the file')
# f = open('file.txt', 'w')
# f.write('this is written from write mode in the file,')
# f = open('file.txt', 'a')

# '''if we want to append in the file'''
# f.write('this is append in the file')
# f.close()