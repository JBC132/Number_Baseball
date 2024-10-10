import random

def start_game():
    game_set = False
    tries = 0

    name1 = input("Player1 Name?: ")
    name2 = input("Player2 Name?: ")

    while True:
        duplicate = False
        name1_num = input(name1 + "\'s number: ")
        for i in range(4):
            if str(name1_num).count(str(name1_num)[i]) != 1:
                print("There can't be same number\n")
                duplicate = True
                break
        if not duplicate:
            break

    while True:
        duplicate = False
        name2_num = input(name2 + "\'s number: ")
        for i in range(4):
            if str(name2_num).count(str(name2_num)[i]) != 1:
                print("There can't be same number\n")
                duplicate = True
                break
        if not duplicate:
            break

    name1_num_list = []
    name2_num_list = []

    num_length = len(str(name1_num))

    turn = random.randrange(0, 2)
    if turn == 1:
        print(name2, "goes first")
    else:
        print(name1, "goes first")

    while not game_set:
        if (tries+turn) % 2 == 0:
            #name1 goes first
            print(name1 + "\'s turn \n")
            game_set = guess(name1_num_list, name2_num, num_length, game_set)

        elif (tries+turn) % 2 == 1:
            #name2 goes first
            print(name2 + "\'s turn")
            game_set = guess(name2_num_list, name1_num, num_length, game_set)

        tries += 1

def guess(num_list, origin_num, num_length, game_set):
    print("Your previous guesses are: ")
    for elem in num_list:
        print(elem, end=' ')

    print()
    # input guessed number
    while True:
        duplicate = False
        guessed_num = input("Guess a number: ")

        for i in range(num_length):
            if str(guessed_num).count(str(guessed_num)[i]) != 1:
                print("There can't be same number")
                duplicate = True
                break

        if not duplicate:
            if guessed_num == origin_num:
                print("Correct!!")
                game_set = True
                return game_set

            if guessed_num in num_list:
                print("Already guessed. Try another number")
                continue

            else:
                strike_ball(guessed_num, origin_num, num_length)
                num_list.append(guessed_num)
                return game_set


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

    print(str(strike_num) + "Strike " + str(ball_num) + "Ball \n")
    return 0

start_game()