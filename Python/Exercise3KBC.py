'''
Create a program capable of displaying questions to the user like KBC.
Use list data type to store the questions and their correct answer.
Display the final amount the person is taking home after playing the game
'''

list_of_questions = [
    ['Which country was won the 2023 wrold cup ?', 'India', 'Australia','Sauth Africa', "Srilanka", 2],
    ['Which country was won the 2019 wrold cup ?', 'India', 'Australia','Sauth Africa', "Newzeland", 4],
    ['Which country was won the 2015 wrold cup ?', 'India', 'Australia','Sauth Africa', "Srilanka", 2],
    ['Which country was won the 2011 wrold cup ?', 'India', 'Australia','Sauth Africa', "Srilanka", 1],
    ['Which country was won the 2007 wrold cup ?', 'India', 'Australia','Sauth Africa', "Srilanka", 4],
    ['Which country was won the 2003 wrold cup ?', 'India', 'Australia','Sauth Africa', "Srilanka", 2],
    ['Which country was won the 1999 wrold cup ?', 'India', 'Australia','Sauth Africa', "Srilanka", 2],
    ['Which country was won the 1995 wrold cup ?', 'India', 'Australia','Sauth Africa', "Srilanka", 2],
    ['Which country was won the 1991 wrold cup ?', 'India', 'Australia','Sauth Africa', "Srilanka", 2],
    ['Which country was won the 1987 wrold cup ?', 'India', 'Australia','Sauth Africa', "Srilanka", 2],
    
]

levels = [1000,2000,3000,5000,10000,20000, 40000, 160000,320000, 400000]
money=0
for i in range(0, len(list_of_questions)):
    ans = list_of_questions[i]
    print(f'\n\nQuestion for Rs. {levels[i]}')
    print(f'Q{i+1}.', ans[0])
    print(f'\n1. {ans[1]}     2. {ans[2]}')
    print(f'3. {ans[3]}     4. {ans[4]}')
    reply = int(input('\nenter the options number: '))
    if(reply == ans[-1]):
        print(f'\nCorrect answer! You have won the amount of {levels[i]}')
        if(i == 4):
            money = f'{levels[i]}'
        elif(i == 9):
            money = f'{levels[i]}'
    elif(reply ):
        print(f'\nYour options is wrong!😒')
        break
    
    
print('\n\nYour take money for home!',money)
# print(list_of_questions)