#Tupple item removal
post = ('Python', 'Intro', 'something','published')
print(post)

#remove from end
post = post[:-1] 
print(post)

#remove from begining
post = post[1:] 
print(post)

#remove from specific
    #convert to list, modify, convert back to tuple
post = list(post)

post.remove('Intro')
post = tuple(post)
print(post)


