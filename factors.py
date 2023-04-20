# Ask the user for a positive integer
num = int(input("Please enter a positive integer: "))

# Print the factors of the input number
print("The factors of", num, "are:")

for i in range(1, num+1):
    if num % i == 0:
        print(i)