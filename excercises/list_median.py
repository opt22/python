#find median manualy 
#-math library
#-sorted function
#-list slicing
#-computation
#-works only with odd numbered list
#import math as m

sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

sp = sale_prices
count = sorted(sp)
center = len(count) // 2
print(sp)
print(count)
print(center)
print(count[center])

#=====================
import math

def find_median(numbers):

    #return sorted(numbers)[math.floor(len(numbers) /2)]

    return sorted(numbers)[len(numbers) // 2]

print(find_median([1,3,4,5,6,7]))
