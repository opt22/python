#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
print('[--1--]')
# 1.    Create a Python function that accepts a list of numbers and returns the average of the list of numbers.
#import math as m

sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

sp = sale_prices
def average(something):
     alist = sorted(something) 
     target = len(sorted(something)) // 2
     return alist[target]
def average2(something):
     return sorted(something)[len(sorted(something)) // 2 ]
average3 = lambda something : sorted(something)[len(sorted(something)) // 2 ]

def average4 ():
    return lambda thing : sorted(thing)[len(sorted(thing)) // 2 ]

average4_var = average4()

print(average(sp))
print(average2(sp))
print(average3(sp))
print(average4_var(sp))

print('endfunc')
print('_______________________________')

count = sorted(sp)
center = len(count) // 2

print(sp)
print(count)
print(center)
print(count[center])

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
print('[--2--]')

# 2.  Print the number 55 from the nested list to the console.
students = {
   "s1": "Randy",
   "s2": "Clayton",
   "s3": "Marlon",
   "s4": "Eric",
   "s5": "Andrew",
   "s6": "Nick",
   "s7": "Billy",
   "s8": "Tristan",
   "grades": [100,99,88,90,77,66,55,44,33]
 }

print(students['grades'][6])

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
print('[--3--]')
#  3. Insert a string called "new-item" into the list of names, after the name "Terry" and before the name "Jordan".
names_list = ["Marlon", "Randy", "Nick", "Billy", "Clayton", "Terry", "Jordan", "Tristan", "Eric", "Andrew"]
names_list.insert(6,"new_item")
print(names_list)
if "new_item" in names_list:
    print ("Great Success!")
