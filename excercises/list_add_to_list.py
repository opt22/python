tags = [
   'python',
   'development',
   'tutorials',
   'code',
]

#tags[-1] = 'Programming'
print(tags)

tags.extend(['Programming'])
print(tags)

new_tags = tags.extend(['Programming'])
print(new_tags)
    

new_tags = tags + ['Programming']
print(new_tags)
    # preserves original list
    



