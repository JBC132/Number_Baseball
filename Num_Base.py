import random

def start_game():
    name1 = input("Player1 Name?: ")
    name2 = input("Player2 Name?: ")

    name1_num = input(name1 + "\'s number: ")
    name1_num = input(name2 + "\'s number: ")

    if random.randrange(0, 2) == 1:
        print(name2, "goes first")
    else:
        print(name1, "goes first")


start_game()