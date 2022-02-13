name = 'Kristine'
age = 12
product = 'Python something something'
from_account = 'somethingelse'

greeting = "Hi {0}, you are listed as {1} years old and you have purchased: {2}...--{3}".format(name, age, product, 'somethingelse')

print(greeting)


#string literal

greeting2 = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}"

print(greeting2)
