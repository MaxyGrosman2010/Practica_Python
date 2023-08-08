print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')
print('Coding' + ' ' + 'For' + ' ' + 'All')
company = 'Coding for all'
print(company)
print(len(company))
case = company.upper()
case = company.lower()
case = company.capitalize().title().swapcase()
slice = company[6:]
print(slice.find('Coding', 0, 13))
company = company.title()
python = company.replace('Coding', 'Python', 1)
print(python)
python = python.replace('All', 'Everyone', 1)
print(python)
print(company.split(' '))
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))
print(company[0])
print(company[-1])
print(company[10])
acronym_1 = python[0] + python[7] + python[11]
print(acronym_1)
acronym_2 = company[0] + company[7] + company[11]
print(acronym_2)
print(company[0])
print(company[7])
print(company.rfind('l', 0))
print('You cannot end a sentence with because because because is a conjunction'.find('because',
    0))
print('You cannot end a sentence with because because because is a conjunction'.rindex(
    'because', 0))
print('You cannot end a sentence with because because because is a conjunction'[31:54])
print(company.startswith('Coding'))
print(company.endswith('coding'))
print(f'  {company}  '.strip())
print('thirty_days_of_python'.isidentifier())
print(' '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
radius = 10
area = 3.14 * radius ** 2
print(f'radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius {radius} is {int(area)} meters square.')
print(f'{8} + {6} = {14}\n{8} - {6} = {8 - 6}\n{8} * {6} = {8 * 6}\n{8} / {6} = {8/6:.2f}\n{8} % {6} = {8 % 6}\n{8} // {6} = {8 // 6}\n {8} ** {6} = {8**6}')
