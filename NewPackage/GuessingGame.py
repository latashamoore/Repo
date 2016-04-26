"""
Assignment # 3.4- Guessing Game
Overview
You will create a guessing game!
Write a small python program that does the following:
Generate a random number from 1 to 10 (Look up the appropriate python class/function to do this)
Ask the user to guess the number.
Give the user three guesses to get the number correct.
If the user guesses correctly, exit the game and congratulate the user.
If the user fails give the appropriate error message and exit the game.
Modify the program so that following requirements are met.
If the user is within one of the correct answer display “Hot”
If the user is within two of the correct answer display “Warm”
All other guesses should display “Cold”
Upload the program to GitHub
"""


def generate_random():
    import random
    return(random.randint(1,10))


def guessed_number():
    return(int(input("Please guess a random number from 1 and 10")))


def guessing_game():
    random_number = 0
    random_number = generate_random()
    #print("random number is", random_number, "and type is", type(random_number))
    print()
    is_guessed_number = False
    user_number = 0
    tries = 0
    while (is_guessed_number == False) and (tries < 3):
        user_number = guessed_number()
        tries += 1
        if user_number == random_number:
            is_guessed_number = True
            print('Congratulations! You\'ve guessed the correct number')
            return
        elif user_number == random_number+1 or user_number == random_number-1:
            print('You\'re hot.')
        elif user_number == random_number+2 or user_number == random_number-2:
            print('You\'re warm.')
        else:
            print('You\'re cold.')
    print('Unfortunately, you haven\'t guessed the random number in time')
    return


guessing_game()
