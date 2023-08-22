#Exercises 1
def add_two_numbers(one, two):
    return one + two

def area_of_circle(radio):
    return 3.14 * (radio ** 2)

def add_all_nums(*nums):
    result = 0
    for num in nums:
        if type(num) is int:
            result += num
        else:
            return "You have not send only number as such this isn't valid"
    return result

def celsius_to_Fahrenheit(temp):
    return (temp * (9 / 5)) + 32

def check_season(month):
    if month == "March" or month == "April" or month == "May": return "Autumn"
    elif month == "September" or month == "October" or month == "November": return "Spring"
    elif month == "December" or month == "January" or month == "February": return "Summer"
    elif month == "June" or month == "July" or month == "August": return "Winter"
    else: return "It isn't a valid month"

def print_list(new_list):
    if type(new_list) is list: 
        for elem in new_list: print(elem)
    else: print("Please send a valid list")

def reverse_list(to_reverse):
    list_reversed = []
    if type(to_reverse) is list:
        for elem in reversed(to_reverse): list_reversed.append(elem)
        return list_reversed
    else: return "Please send a valid list"

def capitalize_list(cap):
    cap_list = []
    if type(cap) is list:
        for elem in cap: 
            if type(elem) is str: 
                elem = elem.capitalize()
                cap_list.append(elem)
            else: cap_list.append(elem)
    return cap_list

def add_item(to_add_list, elem):
    if type(to_add_list) is list:
        to_add_list.append(elem)
        return to_add_list
    else: return "Please insert a list to add an element"

def remove_item(list_to_remove, to_remove):
    if type(list_to_remove) is list:
        list_to_remove.remove(to_remove)
        return list_to_remove
    else: return "Please send a list so we can remove the element"

def sum_all_numbers(num):
    to_return = 0
    if type(num) is int:
        for elem in range(num): to_return += elem
        return to_return
    else: return "Please insert a number"

def sum_odd_numbers(num):
    if type(num) is int:
        to_return = 1
        while(to_return < num): to_return += 2
        return to_return

def sum_even_numbers(num):
    if type(num) is int:
        to_return = 0
        while(to_return < num): to_return += 2
        return to_return

def odd_and_evens(num):
    odd = 0
    even = 0
    if type(num) is int:
        for elem in range(num):
            if elem % 2 == 0: even += 1
            elif elem % 2 != 0: odd +=1
    print(f'The number of odds are {odd}')
    print(f'The number of evens are {even}')

def factorial(num):
    if type(num) is int:
        if num >= 1: return num * factorial(num - 1)
        return 1

