#Tupple re-assignment
post=('Python', 'Intro', 'somethin')

print(id(post))

post = post + ('published',)
    #comma is important
    #otherwise this is an order of operations

title, sub_heading, content, status = post
#sum = (2 * 2) + 5

print(title)
print(content)
print(sub_heading)
print(status)

print(id(post))

