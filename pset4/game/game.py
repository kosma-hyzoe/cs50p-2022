import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            break
    except ValueError:
        continue

int_to_guess = random.randint(1, level)

while True:
    try:
        users_guess = int(input("Guess: "))

        if users_guess < int_to_guess:
            print("Too small!")
        elif users_guess > int_to_guess:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()
    except ValueError:
        continue
