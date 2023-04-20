import random

# Generate a random integer between -100 and 100
target_num = random.randint(-100, 100)

print("Enter the integer for the player to guess.")
print(target_num)

guess = None
num_guesses = 0

# Loop until the user guesses the number
while guess != target_num:
    print("Enter your guess.")
    guess = int(input())

    if guess > target_num:
        print("Too high - try again:")
    elif guess < target_num:
        print("Too low - try again:")

    num_guesses += 1

print("You guessed it in", num_guesses, "tries.")