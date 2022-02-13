#evaluate answer against user input
#'''
#rps game
#'''
##print("(1)")
#
#
#def rps_game1():
#    return "rock" 
#print(rps_game1())
#
#print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
#print("(2)")
#
#def rps_game2():
#    import random
#    result = random.randrange(0, 3)
#    options = ("rock", "paper", "scisors")
#    return options[result]
#print(rps_game2())

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
#print("(3)")

def rps_game3():
    player_choice = str(input("rock paper or scisors?"))
    import random
    computer_choice = ("rock", "paper", "scisors")[random.randrange(0,3)]
    spread = [player_choice , computer_choice]
    win_conditions = [
                     ["win" ,["rock" , "scisors"]],
                     ["lose" ,["rock" , "paper"]],
                     ["draw" ,["rock" , "rock"]],
                     ["draw" ,["scisors" , "scisors"]],
                     ["win" ,["scisors" , "paper"]],
                     ["lose" ,["scisors" , "rock"]],
                     ["win" ,["paper" , "scisors"]],
                     ["draw" ,["paper" , "paper"]],
                     ["lose" ,["paper" , "rock"]]
                     ]
    print(f"comp:{computer_choice}")
    print(f"player:{player_choice}")
    print(f'spread:{spread}')
    for condition in win_conditions:
        if condition[1] == spread:
            print(f"result {condition[0]}")
    return f"comp:{computer_choice}"
rps_game3()



