

nums = list(range(1,100))
print(nums)
print('---------------------')

while len(nums) > 0:
    print(nums.pop())

def guessing_game():
    while True: 
        print('Guess?')
        guess = input()

        if guess == '42':
            print('correct')
            return False
        else:print(f'No, worng{guess} \n')

guessing_game()





