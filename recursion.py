from functools import lru_cache
# Fibonacci 5

# Fib 4 + Fib 3

# Fib 4 = Fib 3 + Fib 2
# Fib 3 + Fib 2

# Idea of Fibonacci is to take number and add whatever (number - 1 + number - 2)

@lru_cache(maxsize = 100)
def fibonacci(n):
    # edge cases
    # check that the integer is a positive number
    if type(n) != int:
        raise TypeError('Value must be a positive number')
    if n < 1:
        raise ValueError('Number needs to be positive')

    # base case
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        # recursive step
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(70))

# for n in range(1, 100):
#     print(n, ':', fibonacci(n))

# fib_cache = {}
# def fibonacci(n):
#     if n in fib_cache:
#         return fib_cache[n]

#     # compute nth term
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n - 1) + fibonacci(n - 2)

#     # cache the value and return it
#     fib_cache[n] = value
#     return value

# for n in range(1, 100):
#     print(n, ':', fibonacci(n))
