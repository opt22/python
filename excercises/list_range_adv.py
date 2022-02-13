tags = [
        'python', 
        'development', 
        'tutorial', 
        'code'
]

print('first')
tag_range = tags[1:-1:2]
print(tag_range)
#print every second item

print('second')
tag_range = tags[::-1]
print(tag_range)
#reverse the list

print('reverse')
tags.sort(reverse=True)
print(tags)


print(tags.range(3))



