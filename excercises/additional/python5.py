#1. Return the number (count) of vowels in the given string. We will consider a, e, i, o, u as vowels for this Kata (but not y).  The input string will only consist of lower case letters and/or spaces.
def vowels(somestr):
    v_list=0
    for i in str(somestr):
        for x in ['a', 'e', 'i', 'o', 'u']:
            if x == i:
                v_list += 1

#2.    Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for twitter and how he types. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below. Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

#    Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
#    Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"


#3. The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.
#     To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
#
#    Your function should accept a list of lists/tuple/dict (for age. and their handicap)

#    Output will consist of a list of string values stating whether the respective member is to be placed in the senior or open category. ( meaning you need to return a list with the open or senior determination)
oldlist = [
         ["bob" ,["55" , "8"]],
         ["edd" ,["57" , "26"]],
         ["fred" ,["11" , "22"]],
         ["steve" ,["80" , "0"]],
         ]
def oldbags(people):
    senior_list = []
    open_list = []
    for person in people:
       if int(person[1][0]) >= 55 and int(person[1][1]) > 7:
           senior_list.append(person[0])
       else:
           open_list.append(person[0])
    return f"openlist: {open_list} seniorlist: {senior_list}"

print(oldbags(oldlist))




