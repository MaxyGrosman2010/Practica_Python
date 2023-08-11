import math
#Exercise 1
first_age = int(input('Enter your age: '))

if first_age >= 18: print("You're old enough to learn to drive")
else: print(f'You need {18 - first_age} more to learn to drive')

second_age = int(input('Enter the age of another: '))

if first_age > second_age: print(f'The first age is older by {first_age - second_age} years')
elif first_age == second_age: print('Both ages are the same')
else: print(f'The second age is older by {second_age - first_age} years')

a = int(input('Please enter a first numer: '))
b = int(input('Please enter a second number: '))

if a > b: print(f'{a} is greater then {b}')
elif a < b: print(f'{b} is greater then {a}')
else: print(f'a and b are an equal value of {a}')

#Exercise 2
grade = int(input('Please insert the grade of a student: '))

if grade >= 80: print('A')
elif grade < 80 and grade > 69: print('B')
elif grade < 70 and grade > 59: print('C')
elif grade < 60 and grade > 49: print('D')
else: print('D')

month = input('Please insert the month: ')

if month == 'March' or month == 'April' or month == 'May': print('Autumn')
elif month == 'September' or month == 'October' or month == 'November': print('Spring')
elif month == 'December' or month == 'January' or month == 'February': print('Summer')
elif month == 'June' or month == 'July' or month == 'August': print('Winter')
else: print('Please insert a valid month')

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Please insert a fruit: ')

if fruit in fruits: print('The fruit exist on the list')
else: 
    fruits.append(fruit)
    print(fruits)

#Exercise 3
person={'first_name': 'Asabeneh', 'last_name': 'Yetayeh', 'age': 250, 'country': 'Finland',
    'is_marred': True, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Space street','zipcode': '02210'}}
pos_skills = math.ceil((len(person['skills']) - 1) / 2)
if len(person['skills']) != 0: print(person['skills'][pos_skills])
if 'Python' in person['skills']: print(person['skills'].index('Python'))

if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front-end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']: 
    print('He is a back-end developer')
else: print('Unknown title')

if person['is_marred'] and person['country'] == 'Finland': 
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married')
