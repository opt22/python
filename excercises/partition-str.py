heading = "Lorem: Ipsum dolor sit amet, consetetur sadipscing elitr, sed"

header, _, subheader = heading.partition(': ')
#|      \         \          \        \     \__________removed from string
#part1   part2     part3      variable partition function


print(header)
print(_)
print(subheader)

print('something')
first, second, third = heading.partition(': ')

print(first)
print(second)
print(third)


