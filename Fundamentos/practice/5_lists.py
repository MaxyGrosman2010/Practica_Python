#Exercises 1
list = []
list_two = [1, 2, 3, 4, 5]
first, middle, last = list_two[0], list_two[2], list_two[-1]
mixed_data_types = ['Maximiliano', 29, 1.63, 'Single', 'You dont care']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[-1])
it_companies[0] = 'Monolith Soft'
print(it_companies)
it_companies.append('Nintendo')
it_companies.insert(4, 'Sony')
it_companies[0] = it_companies[0].upper()
it_companies[1] = it_companies[1].upper()
it_companies[2] = it_companies[2].upper()
it_companies[3] = it_companies[3].upper()
it_companies[4] = it_companies[4].upper()
it_companies[5] = it_companies[5].upper()
it_companies[6] = it_companies[6].upper()
it_companies[7] = it_companies[7].upper()
it_companies[8] = it_companies[8].upper()
print(it_companies)
print('#; '.join(it_companies))
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[6:9])
print(it_companies[3:6])
print(it_companies.pop(0))
print(it_companies.pop(3))
print(it_companies.pop())
it_companies.clear()
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(len(full_stack))
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

#Exercises 2
ages = [19, 22, 19, 24, 20, 25, 26, 24 ,25, 24]
ages.sort()
print(ages)
min_age = ages.pop(0)
max_age = ages.pop(-1)
ages.insert(0, min_age)
ages.insert(len(ages), max_age)
median_age = ages[4] / 2
average_age = (ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] + ages[7] +
    ages[8] + ages[9]) / len(ages)
range_ages = ages[-1] - ages[0]
print(abs((ages[0] - average_age)), '==', abs((ages[-1] - average_age)))
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
  'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 
  'Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia',
  'Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi',
  'Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile',
  'China','Colombi','Comoros','Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",
  'Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica',
  'Dominican Republic','East Timor (Timor Timur)','Ecuador','Egypt','El Salvador',
  'Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France','Gabon',
  'Gambia, The','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea',
  'Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran',
  'Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati',
  'Korea, North','Korea, South','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho',
  'Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi',
  'Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico',
  'Micronesia','Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia',
  'Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman',
  'Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland',
  'Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia',
  'Saint Vincent','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal',
  'Serbia and Montenegro','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia',
  'Solomon Islands','Somalia','South Africa','Spain','Sri Lanka','Sudan','Suriname',
  'Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand',
  'Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda',
  'Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan',
  'Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']
print(countries[95], countries[96])
first_half = countries[0:97]
second_half = countries[97:]