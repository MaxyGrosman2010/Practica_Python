### Third Class ###
#Lambda

sum_two_numbers = lambda num_one, num_two: num_one + num_two

print(sum_two_numbers(1, 2))

multiply_values = lambda num_one, num_two: num_one * num_two

print(multiply_values(3,6))

def practice_lambda(value):
    return lambda num_one, num_two: num_one + num_two + value

print(practice_lambda(4)(2,3))