def fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n <= 2:
        return 1

    previous_previous = 1
    previous = 1
    current = 2

    for i in range(3, n+1):
        current = previous + previous_previous
        previous_previous = previous
        previous = current

    return current