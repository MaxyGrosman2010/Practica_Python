###Fourth Class###

#Strings
my_string = 'My first string of this file'
my_other_string = 'Second string'
print(len(my_string))
print(len(my_other_string))
#Actions
my_new_line = 'This is a string\nwith jump to another line'
print(my_new_line)
my_tab = '\tThis is a string with tabulation'
print(my_tab)
my_scape = 'This combines\nJump with\ttabulation'
print(my_scape)
my_scape_ignore = 'This ignores\\nJump and\\ttabulation'
print(my_scape_ignore)

#Format
name, lastname, age = 'Maximiliano', 'Grosman', 29
#Variables in lines of strings, this won't work if you don't put the correct amount
print('My name is %s %s and my age is %s'%(name, lastname, age))
#The position matter so the line knows which is first, second and last
print('I have %s and for my %s i could have had a much better career'%(age, age))
#A new format to do this is
format_string = 'My name is {} {} and i have {}'.format(name, lastname, age)
print(format_string)
#Works for numbers too
a = 3
b = 4
print('{} + {} = {}'.format(a, b, a + b))
#Should be a float of 2 digits
print('{} / {} = {:.2f}'.format(a, b, a / b))
#Another form is the following which works the same as .format
#This is know as interpolation
print(f'{a} + {b} = {a + b}')

#Unpacking strings
language = 'Python'
a, b, c, d, e, f = language
print(a)
print(b)
#Slicing
slice = language[0 : 3]
print(slice)
slice_two = language[3 : ]
print(slice_two)
#Getting chars on reverse
reverse = language[-1]
print(reverse)
reverse_string = language[::-1]
print(reverse_string)
#Jumps every 2do characters
jump_string = language[0:6:2]
print(jump_string)

#System functions
#Length
print(len(language))
#First letter cap
print(language.capitalize())
#All uppercase string
print(language.upper())
#All lowercase string
print(language.lower())
#Counts letters
print(language.count('t'))
#If it contains a number returns booleans
print(language.isnumeric())
print('1'.isnumeric())
#Concat functions
print(language.upper().lower().capitalize())
#If it starts with certain characters
print(language.startswith('py'))