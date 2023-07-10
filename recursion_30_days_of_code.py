def factorial(n):
    # terminating condition
    if n-1 >= 1:
        return n*factorial(n-1)
    else:
        return n

print(factorial(int(input())))
