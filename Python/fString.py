# f string is introduces in python 3.6 version

letter = "Hi My name is {} and i am from {}"
country = 'India'
name1= 'Ashu'
print(f"Hi My name is {name1} and i am from {country}")
print(letter)

txt = "value to the 2 decimal {price: .2f} dollers"

print(txt.format(price = 49.09998)); '''without f string'''
price = 50.561425
print(f"valu of price in to 2 decimal places is {price: .2f}")

print(type(f"{2*30}")); '''<class 'str'>'''

#  to show {} in the output
print(f"this is curly braces showing in the output {{true}}"); '''this is curly braces showing in the output {true}'''