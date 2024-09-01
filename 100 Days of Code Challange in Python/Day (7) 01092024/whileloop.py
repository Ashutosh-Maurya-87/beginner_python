
# while loop
d = 5
while d :
    print('vlaue is',d)
    d = d-1
'''
vlaue is 5
vlaue is 4
vlaue is 3
vlaue is 2
vlaue is 1
'''

l = ['red','green','blue']
while l :
    print(l.pop())
'''
blue
green
red
'''
l = 'ashutosh'
while l :
    print(l)
    l = l[1:]

'''
ashutosh
shutosh
hutosh
utosh
tosh
osh
sh
h
'''
 # break in while loop
x = 6
while x :
    print('value is',x)
    x -= 1
    if x == 3:
        break; 
'''
value is 6
value is 5
value is 4
'''