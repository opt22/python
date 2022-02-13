teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
}
teams['red sox'] = ['Price', 'Betts']

print(teams)

featured_team = teams['mets']
print(featured_team)

#                            /----error-condition, 
featured_team = teams.get('mets', 'No Featured team')
#                                               \___return value
        #this creates a fallback value if specified value does not exist
print(featured_team)

