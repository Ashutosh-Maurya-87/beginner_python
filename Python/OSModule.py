# os module is very khatarnak method
import os
print(os); '''<module 'os' (frozen)>'''

# this create the Day folder in the file if there is not any Day folder
# if(not os.path.exists('day')):
#     os.mkdir('Day')


# if we want to create folder into one time then

# for i in range(0, 100):
#     os.mkdir(f'Day/Day{i+1}')
'''this creates 100 folder inside the Day folder'''

# if we want to rename all the folder then
# for i in range(0,100):
#     os.rename(f'Day/Day{i+1}', f'Day/tutorial{i+1}')
'''this rename all the folder name Day -> tutorial inside the Day'''

# To Find the list of folder
# os.listdir('Day'); '''it give all the list of folder inside the Day'''

# folders = os.listdir('Day')


# for folder in folders:
#     print('print folder one by one', folder)
#     '''to print the file of inside the folder then we write'''
#     print(f'print file inside the folder',os.listdir('Day/{folder}'))

# to find the directory means path where we are working
# print('path is: ', os.getcwd()); '''path is:  D:\imp\Python'''
# os.chdir('/imp')
print('change path: ', os.getcwd()); '''change path:  D:\imp'''


