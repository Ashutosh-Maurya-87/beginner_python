'''
in python there is no any do while loop, like c,c++ etc.
But we can use break inside the while loop, which will overcome the problem of do-while loop

# To create a do while loop in python, we need to
# Modify the while loop a bit in order to get similar
# behaviour to a do while loop


# the most common technique to emulate a do-while loop
# in python is to use an infinite while loop with a  
# break statement wrapped in an if statement that checks a given condition and breaks the 
#  iteration if that condition becomes true
'''
x = 1; 
while True :
    print('value of x is',x)
    x += 1
    if(x%5 == 0) :
        break; 

'''
value of x is 0
value of x is 1
value of x is 2
value of x is 3
value of x is 4
value of x is 5
value of x is 6
value of x is 7
value of x is 8
value of x is 9
'''