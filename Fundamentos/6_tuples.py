###Sixth class###

#Tuples
first_tuples = tuple()
second_tuples = ()
first_tuples = (29, 1.63, 'Maximiliano', 'Grosman', 'Maximiliano')
print(first_tuples)
print(type(first_tuples))
print(first_tuples[0])
print(first_tuples[-1])
print(first_tuples.count('Maximiliano'))
print(first_tuples.count('Grosman'))
print(first_tuples.index('Maximiliano'))
#You can't add, delete or change values to tuples
second_tuples = (60, 30)
combine_tuples = first_tuples + second_tuples
print(combine_tuples)#You can concatenate then but not change then
print(combine_tuples[3:6])#You can slice values but you won't be able to change then
#You can change it to a list to modify it, and then change it back, but in that case
#You didn't needed a tuples
#You can delete a tuple as a whole
del first_tuples