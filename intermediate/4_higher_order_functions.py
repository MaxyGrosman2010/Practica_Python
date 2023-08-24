### Fourth Class ###
from functools import reduce
#Higher order functions
def sum_one(num): return num + 1

def sum_function_values(num_one, num_two, var_func): return var_func(num_one + num_two)

print(sum_function_values(5,2, sum_one))

def sum_five(num): return num + 5

print(sum_function_values(4,6,sum_five))
#Closures
def sum_ten(first_value):
    def add(second_value): return second_value + 10 + first_value
    return add
add_closure = sum_ten(2)
print(add_closure(2))
print(sum_ten(1)(9))

#Build-in Higher order functions
new_list = [1,2,3,4,5]
print(list(map(lambda num: num * 2, new_list)))

print(list(filter(lambda num: num % 2 == 0, new_list)))

def sum_two_values(num_one, num_two):return num_one + num_two

print(reduce(sum_two_values, new_list))