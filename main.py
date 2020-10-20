# Andrei's Python Guessing game code
from random import randint
import sys

# generate a number 1~10
answer = randint(1, 10)


def validate_user_input(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False


# We enclose this in an if block to prevent this code from running
# when the file is imported into test_game.py
if __name__ == "__main__":
    # input from user?
    # check that input is a number 1~10
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            validate_user_input(guess, answer)
        except ValueError:
            print('please enter a number')
            continue
