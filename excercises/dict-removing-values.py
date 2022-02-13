teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
    "red sox": ["Price", "Betts"],
}

del teams['astros']
del teams['mets']
    #fails
print(teams.get('mets', 'Not found'))
    
print(teams)
    
#- - - - - - - - - - 
    # *needs to be stored in variable to receive ouput
teams.pop('astros', 'Not found')
teams.pop('rays', 'Not found')
    #no output on fail set in variable
removed_team = team.pop('yankees', 'Not found')
print(teams)
#       \____no value returned
print(removed_team)
#       \____returns value



