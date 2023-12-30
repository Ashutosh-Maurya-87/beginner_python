# this emulate the do... while loop

# To create a do while loop in python, we need to
# Modify the while loop a bit in order to get similar
# behaviour to a do while loop


# the most common technique to emulate a do-while loop
# in python is to use an infinite while loop with a  
# break statement wrapped in an if statement that checks a given condition and breaks the 
#  iteration if that condition becomes true

# EXAMPLE --- 




i =0
while True:
    print('value of i', i)
    i=i+1
    if(i%100 == 0):
        break