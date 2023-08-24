### Third challenge ###

"""
Fibonacci:
Write a program that prints the first 50 numbers of the Fibonacci succession:
-It begins from 0
-It's made up of a numbers succession of which the following number is the sum of the 2 that
    came before it: 0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci():
    prev = 0
    next = 1
    result = []
    for _ in range(51):
        result.append(prev)
        fib = next + prev
        prev = next
        next = fib
    return result
print(fibonacci())