### Second Class ###

#List comprehension
first_list = [35, 24, 62, 52,5, 30, 30, 17]
print(first_list)
second_list = [i for i in first_list]#Copy a list into another list
print(second_list)
third_list = [1, 2, 3, 4, 5, 6, 7]
print(third_list)

#Quick way to create a list of ints, it can apply to other things
fourth_list = [i for i in range(80)]
print(fourth_list)
first_range = range(8)
print(list(first_range))
six_list = [i + 1 for i in range(8)]
print(six_list)
seven_list = [i * 2 for i in range(8)]
print(seven_list)

def sum_five(num):
    result = 0
    for i in range(6):
        result += num + i
    return result

eight_list = [sum_five(i) for i in range(8)]
print(eight_list)