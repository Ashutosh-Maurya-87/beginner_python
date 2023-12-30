# A function which is called itself is called recursion ---

def fact(n):
    if(n == 0 or n ==1):
        return 1
    else : 
        return n * fact(n-1)
    
print(fact(5)); '''120'''

# fibonacci series --

def fib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        print(n)
        return fib(n-1)+fib(n-2)
    
print(fib(6)); '''8'''
print(fib(1))