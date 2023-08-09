###Eighth Class###

#Dictionary
first_dict = dict()
second_dict = {}
print(type(first_dict))
print(type(second_dict))
second_dict = {'name': 'Maximiliano', 'lastname': 'Grosman', 'age': 29, 1: 'Python'}
print(type(second_dict))
first_dict = {'name': 'Maximiliano', 'lastname': 'Grosman', 'age': 29, 
    'Languages': {'Python', 'C++', 'Javascript'}, 1: 1.63}
print(first_dict)
print(second_dict)
print(len(first_dict))
print(len(second_dict))
print(first_dict['name'])#Access to key
first_dict['name'] = 'Daniel'
print(first_dict['name'])
print(first_dict[1])
first_dict['street'] = "You don't care"
print(first_dict['street'])
print(first_dict)
del first_dict['street']#Eliminates one element of the dictionary
print(first_dict)
print('Grosman' in first_dict)#This looks by key, not by value
print('lastname' in first_dict)

#Properties
print(first_dict.items())
print(first_dict.keys())
print(first_dict.values())
print(type(first_dict.values()))
#To get a list of values or keys you need
print(list(first_dict.values()))
#New dict without values but with keys it doesn't need an already existant dictionary to do 
#this, this isn't well seen.
print(dict.fromkeys(('name', 1)))
#You can use a list to set up the keys to create it
keys = ['name', 1, 'floor']
print(dict.fromkeys(keys))
#You can also use another dict
keys_2 = dict.fromkeys(first_dict)
print(dict.fromkeys(keys_2))
#This puts to all the elements the same values because normally it's none
three_dict = dict.fromkeys(first_dict, ('Maximiliano', 'Grosman'))
print(three_dict)