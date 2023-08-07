#Second Class

#Variables
firstname = 'Maximiliano'
lastname = 'Grosman'

#One space
print(firstname, lastname)

#Two spaces
print(firstname, ' ', lastname)

#Without spaces
fullname = firstname + lastname
print(fullname)

#With spaces
fullname = firstname + ' ' + lastname
print(fullname)

#Other ways to make valid variables
full_name = firstname + ' ' + lastname
print(full_name)

#Declaring booleans
true = True
false = False
print(true, 'and', false)

#Practice with numbers
print(1)
print(1 + 1)
one = 1
two = 2
three = 3
print(one + 1, one + two, one + three)
print(two + one, two + 2, two + three)
print(three + one, three + two, three + 3)
print(one + one, two + two, three + three)

#Curiosity
print(type(print))

#Length
print(len(firstname), len(lastname), len(full_name), len(fullname))

#Variables in one line not a very good practice, VERY CAREFUL IF USING syntaxis
firstname, lastname, alias, age = 'Maximiliano', 'Grosman', 'Maxy', 29
print(age, alias, firstname, lastname)

#Create variables which you can add input through command console
"""first_name = input('What is your first name: ')
last_name = input('What is your surname: ')
print('Your fullname is:', first_name, last_name)"""

#Not a strong typing, VERY CAREFUL WITH THIS
age = 'Maximiliano'
firstname = 29
print(age, firstname)
lastname = age
print(lastname)

#Force typing won't work, it's just for us to know what type the variable is, maybe on inputs
age: int = 29
age = lastname
print(age, type(age))