### Fourth Challenge ###

"""
Is it a prime number?
Write a function which finds out if a number is prime or it isn't. Print the prime numbers
between 1 to 100
"""

def is_prime(num):
    if num < 2: return False
    for i in range(2, num):
        if num % i == 0: return False
    return True

for i in range(1, 101): print(f"{i}: {is_prime(i)}")