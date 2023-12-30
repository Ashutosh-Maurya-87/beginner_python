number = input('enter number')
# fromatted string is written by f-string ex
# if we write print('number {number}') then it show number {number}
# but if we write print(f'number {number}') then it show number then vlaue of number
print(f'numbr {number}')

# function in python , we write using def keyword
def square(x) :
    return x*x

for i in range(10) :
    print(f"the square of value {i} is {square(i)}")

# we have define the add function here but we call this function in another file add.py
def add(x):
    return x+x