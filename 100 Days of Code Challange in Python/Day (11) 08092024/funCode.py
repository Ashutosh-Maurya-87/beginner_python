# write a program that will handle morning task 😂😂

# def Alarm(time) : 
#     if(time == '5:00') :
#         print('morning walk pe jana hai')
#     elif time == '6:00' :
#         print('Lota leke khet jana hai 😂')
#     elif time == '7:00' :
#         print('Ready hona hai, Aur school jana hai')
#     else :
#         print('Late ho gaye tum, Ab tum to gaye bete 😂😂😂😂😂')

# time = input('enter the time')
# Alarm(time)

# program to plan a trip with girlfriend 😂😂😂😂😂😂😂

list = []
def gfCall (gfSay) :
    print('Gf Say:',gfSay)

def boyCall (boySay) :
    print('Boy Say:', boySay)

def repeatGfCall () : 
     gfSay = input('Gf saying: ')
     list.append(gfSay)
     gfCall(gfSay)

def repeatBoyCall () : 
     boySay = input('Boy saying: ')
     list.append(boySay)
     boyCall(boySay)

print(f'Who is make the plan for trip?')
print(f'press 1 for Boy')
print(f'press 2 for Girl')
print(f'press 3 for Exit Chat')
inputNumber = input('Enter the number: ')

if(int(inputNumber) == 1) :
    boySay = input('what you want to say? regarding trip')
    list.append(boySay)
    boyCall(boySay)
    if (len(boySay) > 1) :
        repeatGfCall()
        repeatBoyCall()
        repeatGfCall()
        repeatBoyCall()
        repeatGfCall()
        repeatBoyCall()
        repeatGfCall()
        repeatBoyCall()
        repeatGfCall()
        repeatBoyCall()
elif int(inputNumber) == 2 :
        girlSay = input('what you want to say? regarding trip')
        list.append(girlSay)
        gfCall(girlSay)
        if (len(girlSay) > 1) :
            repeatBoyCall()
            repeatGfCall()
            repeatBoyCall()
            repeatGfCall()
            repeatBoyCall()
            repeatGfCall()
            repeatBoyCall()
            repeatGfCall()
            repeatBoyCall()
            repeatGfCall()
else : 
        print('you have entered wrong number 😯🤔')

