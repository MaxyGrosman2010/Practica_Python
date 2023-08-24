#Exercises 1
empty = ()
brothers = ('Leandro', "Martin")
sisters = ('Andrea','Estela')
family = brothers + sisters

#Exercises 2
father, brother, mother, sister = family
fruits = ('Apples', 'Bananas')
vegetables = ('Tomato', 'Onion')
animal_products = ('Beef', 'Ground Beef')
food_stuff_it = fruits + vegetables + animal_products
food_stuff_it = list(food_stuff_it)
print(food_stuff_it[2:4])
print(food_stuff_it[0:3], food_stuff_it[3:])
del food_stuff_it
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries.index('Iceland'))