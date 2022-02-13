
teams = [
    {
        'astros': {
            '2b': 'edd',
            'ss': 'steve',
            '3b': 'bob',

        }
    },

    {

        'angels': {
            'OF': 'trout',
            'DH': 'pujols',
        }
    },
]

    
print(teams)

angels = teams[1].get('angels', 'Not found')

print(list(angels.values())[1])
