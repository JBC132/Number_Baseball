import random

def start_game():
    game_set = False

    name1 = input("Player1 Name?: ")
    name2 = input("Player2 Name?: ")

    name1_num = input(name1 + "\'s number: ")
    name1_num = input(name2 + "\'s number: ")

    if random.randrange(0, 2) == 1:
        print(name2, "goes first")
    else:
        print(name1, "goes first")







    game_set = True

def guess(num_list, origin_num):
    # input guessed number
    while True:
        guessed_num = input("Guess a number: ")
        if guessed_num in num_list:
            print("Already guessed. Try another number")
            continue
        else:
            strike_ball(guessed_num, origin_num)
            break

def strike_ball(guessed_num, origin_num):
    # check if guessed number has strike or ball

    # result = <strike_num> + "strike" + <ball_num> + "ball"
    # return result
    pass




start_game()