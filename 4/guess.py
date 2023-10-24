'''
    collect user guess integer input
    and compare it with the secret number
    in range [1,100]
    The program will output the relativity
'''

import random

# define a random secret number
SECRET = random.randint(1,100)  # constant global
             # Randomize the SECRET
DUMMY = -1
guess = DUMMY

while (guess != SECRET):
    # tell user to guess the secret number
    guess = int(input("guess the integer: "))

    # tell the user the relativity of guess
    if(guess > SECRET):
        print("guess is too large!")
        print()
    elif(guess < SECRET):
        print("guess is too low!")
        print()
    else:       # guess == SECRET
        print("Congrats!!! You guessed it")

    # if guess is wrong, go back to step 2

# output the secret number

print("The secret number was", SECRET)
