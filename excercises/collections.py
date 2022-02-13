users = ['bob', 'steve', 'alex']
print(users)
users.remove('steve')
print(users)

popped_user = users.pop()
#remove last user from list and store in variable 
print(popped_user)
print(users)

del users[0]
#remove entry by index
print(users)
