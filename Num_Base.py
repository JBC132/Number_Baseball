import random

def start_game():
    game_set = False

    name1 = input("Player1 Name?: ")
    name2 = input("Player2 Name?: ")

    name1_num = input(name1 + "\'s number: ")
    name2_num = input(name2 + "\'s number: ")

    num_length = len(str(name1_num))

    if random.randrange(0, 2) == 1:
        print(name2, "goes first")
    else:
        print(name1, "goes first")




    game_set = True

def guess(num_list, origin_num, num_length):
    # input guessed number
    while True:
        guessed_num = input("Guess a number: ")
        if guessed_num in num_list:
            print("Already guessed. Try another number")
            continue
        else:
            strike_ball(guessed_num, origin_num, num_length)
            break


def strike_ball(guessed_num, origin_num, num_length):
    # check if guessed number has strike or ball
    strike_num = 0
    ball_num = 0
    guessed_num = list(map(int, str(guessed_num)))
    origin_num = list(map(int, str(origin_num)))

    for i in range(num_length):
        if guessed_num[i] in origin_num:
            ball_num += 1

        if guessed_num[i] == origin_num[i]:
            ball_num -= 1
            strike_num += 1

    result = str(strike_num) + "Strike " + str(ball_num) + "Ball"
    print(result)

start_game()