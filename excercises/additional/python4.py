#Are Python Strings immutable or mutable?
    #immutable
#Are Python Lists immutable or mutable?
    #mutable
#What can be stored in a Python List?
    #strings, lists, tupples, dictionaries.
#Explain what a Python Dictionary is and how you might use one.
    #a dictionarry is an array containing key value pairs
    #the basic most use is relating an attribute to an object
        #so a dictionary of self with a key of name and a value of bob
# What is a Tuple in python?
    #A tupple is an immutable list
#What is a Set in python?
    #an un-ordered un-indexed list
    #will only return unique entries from contained values
#What is List Comprehension in Python?
    #create new list from an existing one based on given parameters
    #allows short hand syntax to accomplishing this
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#- - - - - - - - - -  
#Weekend Coding Challenges
#- - - - - - - - - -  

#1. Create me a function that takes a list of 'strings' as an argument, and returns the length of the longest string in the list.
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("(1.)")
things = ["first", "second", "third", "fourth", "fifth", "twenty_fourth"]

def count_longest(input):
    for i in input:
        counter = 0
        if counter < len(i):
            counter = len(i)
    return counter

print(count_longest(things))

#2. Create a function that takes in 'sets' and merges them.

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("(2.)")
someset1 = {"one", "two", "three", "four", "five" }
someset2 = {"six", "seven", "eight", "nine", "ten" }

def mergsts(arg1, arg2):
    return arg1 | arg2

print(mergsts(someset1, someset2)) 

#3. Create a function that takes in a list of numbers, and returns a list containing all numbers between 1- 100, omitting the numbers passed in to it. (Look at picture for example)
    #asdf

#2 files 
#Capture.PNG
#Capture2.PNG
#8:12
#"1, 10, 13" Are numbers I want omitted. They should be the argument you're passing into your function.[In my example].  You can obviously use different numbers, and hopefully you use more of them as well. (edited) 
#8:13
#BONUS (I still WANt it done though): Create me a function that generates a random Hex color value. (edited) 
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("(3.)")
somelist1 = [1, 83, 10, 13, 222, 2, 4, 33, 44, 88, 21311]
resultlist = []

def rnum(inplist):
    for i in inplist:
        if i > 1 and i < 100 and not i == (1, 3, 10) :
            resultlist.append(i)
    print(resultlist)
rnum(somelist1)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("(4.)")

import random
def hxgen():
    output = "#"
    for i in range(3):
        lemath = str(format(random.randrange(1, 255), 'X'))
        output += lemath
    return output
print(hxgen())
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("(5.)")
'''
    Divide the number by 16.
    Get the integer quotient for the next iteration.
    Get the remainder for the hex digit.
    Repeat the steps until the quotient is equal to 0.
'''    
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
