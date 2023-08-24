### First Challenge ###

"""
Fizz Buzz:
Write a program that show on console the number 1 to 100 changing the following things
-Multiple of 3 for the word: "fizz"
-Multiple of 5 for the word: "buzz"
-Multiple of 3 and 5 for the word: "fizzbuzz"
"""

def one_to_hundred():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0: print("fizzbuzz")
        elif i % 3 == 0: print("fizz")
        elif i % 5 == 0: print("buzz")
        else: print(i)
one_to_hundred()