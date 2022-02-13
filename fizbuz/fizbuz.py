"""
for multiples of 3 print "Fizz"
for multiples of 5 print "Buzz"
for multiples of 3 and 5 print "FizzBuzz"
"""
numlist = range(1, 101)

def fizbuz():
    # print(numlist)
    for num in range(1,101):
        print(num)
        if float(num/3) == num//3:
            print(f"{num} : Fizz")
            # output = f"{num} : Fizz"
#            output.append(f"{num} : Fizz")

        elif float(num/5) == num//5:
            print(f"{num} : Buzz")
#            output.append(f"{num} : Buzz")

        elif float(num/3) == num//3 and float(num/5) == num//5:
            print(f"{num} : FizzBuzz")
#            output.append(f"{num} : FizzBuzz")
        else:
            print(num)

fizbuz()
