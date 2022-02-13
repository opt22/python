#heading = "Python: An Introduction, and Python: Advanced"
#
#header, _, subheader = heading.partion(': ')
#print(header)
#print(subheader)
#


tags = 'python,coding,programming,development'
list_of_tags = tags.split(',')
print(list_of_tags)
    #convets to a single list
    #output is a collection

list_of_tags = tags.split()
print(list_of_tags)
    #converts string to list of strings

heading = "Python: An Introduction, and Python: Advanced"

heading_list = heading.split(': ')

print(heading_list)
#partition returns a tuple and split returns a list
