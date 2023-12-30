# break -> when using break it exit from loop
# continue -> when using continue it exit that iteration

for i in range(12):
    if(i == 10):
        print('exit from the loop')
        break
    print('value', 5*i)

for i in range(12):
    if(i == 10):
        print('skip that iteration and directly jump on the next itertion')
        continue
    print('value', 5*i)