print("How many integers would you like to enter?")
n = int(input())

# Set the initial values of min and max to be the first number entered
print("Please enter", n, "integers.")
num = int(input())
min_num = num
max_num = num

# Compare following input numbers to the current min and max, and replace if necessary
for i in range(n-1):
    num = int(input())
    if num < min_num:
        min_num = num
    elif num > max_num:
        max_num = num

# Display the final min and max
print("min:", min_num)
print("max:", max_num)