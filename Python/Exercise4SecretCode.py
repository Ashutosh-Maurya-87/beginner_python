# Write a python program to translate a message into secret
# code language. Use the rules below to translate normal
# English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first
#     letter and append it at the end now append three random characters
#     at the starting and the end
# else:
#     simply reverse the string
# 
# 
# Decoding:
# 
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove 
# the last letter and append it to the beginning

# program wwould ask , wheter you want to code or decode

enteredText = input('Please enter the text which you want to convert to secret language')
words = enteredText.split(' ')
# ask = input('Do you want to code or Decode')
coding = True
if(coding):
   newWords = []
   for word in words:
      if(len(word)>=3):
          r1='jdk'
          r2='arp'
          resultText = r1 + word[1:] + word[0] + r2
          newWords.append(resultText)
      else:
          newWords.append(word[::1])
   print('res is if: ', ' '.join(newWords))
else:
    newWords=[]
    for word in words:
      if(len(word) >= 3):
          resultText = word[3:-3]
          resultText = resultText[-1] + resultText[:-1]
          newWords.append(resultText)
      else:
          newWords.append(word[::1])
    print('res is else: ', ' '.join(newWords))
    