# print index value of sub-string

sentence = 'Lorem ipsum dolor sit amet'

query = sentence.find('ipsum')
query_two = sentence.index('nothing')

print(query)
print(query_two)

# ########################
# second method 
# true or false match

query_three = 'oops' in  sentence
print(query_three)
