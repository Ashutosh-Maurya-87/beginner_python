
for i in range(1,5):
    print(i)


else:
    print('no i')

'''
else will be used with the loop also
else block will excute when all iteration of the loop will complete succefully

in above example loop will excute completely and after that else block will excute


'''

for i in range(5):
    print('value of i',i)
    # if(i % 2 != 0):
    if(i == 3):
        break
    else: {
        print('value of i in with if block', i)
    }

else:
    print('else bloack will execute after compltion of all the iteration')

'''
in the above example out sider else block is not print
because iteration of loop is not execute completely

Means to say that loop is not reached its last element in the range of 5, 
if iteration will reach
last element of the loop then outside else will print

Means loop become break in the above example not end(complete)
'''