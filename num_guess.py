import random

target_num = random.randint(-100, 100)
num_guesses = 0

print("Enter the integer for the player to guess.")
print(target_num)

while True:
    num_guesses += 1
    guess = int(input("Enter your guess: "))

    if guess > target_num:
        print("Too high - try again.")
    elif guess < target_num:
        print("Too low - try again.")
    else:
        print("You guessed it in", num_guesses, "tries.")
        break