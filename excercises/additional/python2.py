# 1. What is the purpose of an operator, what is precedence?
    #operator modifies initial value by secondary value
    #pecedence is the order in which operators are applied to numbers
# 2. What are the built-in data-structures used to store data in Python? 
    #built in data-structures are the modules that come pre-packaged with python
    #other libraries must be manually added for additional functionality
# 3. Create me a list, add a new item to the end of the list, then grab just that item from the list. Print it to the console. 
###############################################
cars = ['honda', 'toyota', 'ford']
cars.append('peugeot')
popped_car = cars.pop()
print(popped_car)
###############################################
# 4. Create a while loop that prints all the values between 1 - 100. 
def countdown ():
    iteration = 1
    while iteration != 101: 
        print(iteration)
        iteration += 1
    return iteration
countdown()
###############################################
# 5. Create a for loop that prints from 1 - 100. 

for i in range(101): 
    print(i, 'things')

###############################################
# 6. Create a lambda function that takes one parameter (a) and returns it. (edited)

something = lambda a : a-1 
print(something(22))




