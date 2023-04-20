import random

target_num = int(input("Enter the integer for the player to guess.\n"))
num_guesses = 0

while True:
    guess = int(input("Enter your guess.\n"))
    num_guesses += 1

    if guess == target_num:
        if num_guesses == 1:
            print("You guessed it in 1 try.")
        else:
            print("You guessed it in", num_guesses, "tries.")
        break
    elif guess > target_num:
        print("Too high - try again:")
    else:
        print("Too low - try again:")