from random import *
import os

u_pwd = input('Enter password: ')
# pwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
#      's','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
pwd=['a','b','c','d','e','f','g','h','i','j','k','h','1','2','3','4','5','6']
pw = ''

while(pw != u_pwd):
    pw=''
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, 17)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print('Cracking password , please wait...')
        os.system('cls')
print('your pwd is cracked :',pw)