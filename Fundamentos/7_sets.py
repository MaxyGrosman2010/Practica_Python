###Seventh Class###

#Sets
first_sets = set()
second_sets = {}
print(type(first_sets))
print(type(second_sets))#Dict...
second_sets = {"Maximiliano", "Grosman", 29}
print(type(second_sets))#There are no empty sets, unless you begin it through set()
print(len(second_sets))
#You can't look inside a set
second_sets.add('MaxyGrosman2010')
print(second_sets)
#It isn't an organized structure
second_sets.add('MaxyGrosman2010')
print(second_sets)
#Can't inserted elements that already exist on the sets
#Search elements
print('Maximiliano' in second_sets)
print('Maxy' in second_sets)
#Remove elements of the set
second_sets.remove('MaxyGrosman2010')
print(second_sets)
#Clears the set
second_sets.clear()
print(second_sets)
print(len(second_sets))
#Eliminate set
del second_sets