import time
fulltime = time.strftime('%H:%M:%S')

print('fulltime',fulltime)

hour = int(input('enter hour'))
# hour = int(time.strftime('%H'))
minute = time.strftime('%M')
second = time.strftime('%S')

if(hour == 12):
    print('Good Morning')
elif(hour < 12 and hour <= 11):
    print('good morning')
elif(hour > 12 and hour <= 16):
    print('good afternoon')
elif(hour > 16 and hour < 19):
    print('good evening')
else :
    print('Enter valid hour')