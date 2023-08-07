#Exercise 1
first_name = input('Insert your first name: ')
last_name = input('Insert your last name: ')
full_name = first_name + " " + last_name
country = input('Insert your country: ')
city = input('Insert your city: ')
age = 29
year = 2023
is_married = False
is_true = True
is_light_on = True
one, two, three = 1, 2, 3

#Exercise 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(one), type(two), type(three))
print(first_name, len(first_name))
num_one = 5
num_two = 4
sum = num_one + num_two
sub = num_one - num_two
mul = num_two * num_one
div = num_one / num_two
mod = num_one % num_two
exp = num_one ** num_two
floor = num_one // num_two
print('sum:', sum, 'sub:', sub, 'mul:', mul, 'div:', div, 'mod:', mod, 'exp:', exp, 
      'floor:', floor)
radio = input('Insert a radius here: ')
area_of_circle = 3.14 * int(radio) ** 2
circum_of_circle = 2 * 3.14 * int(radio)
print('Area of the circle is: ', str(area_of_circle), 'and its circumference is: ', 
      str(circum_of_circle))
help('keywords')