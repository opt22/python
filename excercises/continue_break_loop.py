# loop breaks
#loop continue 
    #default behaviour
usernames = [
        
        'bob',
        'steve',
        'jo',
        'el',
]

for username in usernames:
    if username == 'bob':
        print(f'nein {username}')
        continue
    else:
        print(f'{username} is allowed')


for username in usernames:
    if username == 'steve':
        print(f'{username} is found {usernames.index(username)}')
        break
    print(username)
