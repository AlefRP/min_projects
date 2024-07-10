
# `import random` is a Python statement that imports the `random` module. This module provides
# functions for generating random numbers. In the code snippet provided, `import random` is used to
# access the `random.randint()` function, which is used to generate a random number within a specified
# range for the guessing game.
X
import random

def guess(x):
    """
    The function `guess` allows the user to guess a number between 1 and a specified maximum number,
    providing feedback on whether the guess is too low or too high until the correct number is guessed.
    
    :param x: The parameter 'x' in the function `guess(x)` represents the maximum number that the user
    can guess. In this case, the function `guess(10)` allows the user to guess a number between 1 and 10
    """
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f"Yay, congrats. You have guessed the number {random_number} correctly!")
                 
guess(10)