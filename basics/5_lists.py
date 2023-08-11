###Fifth Class###

#List
first_list = list()
second_list = []
print(first_list)
print(second_list)
print(len(first_list))
first_list = [29, 26, 35, 24, 62, 52, 30, 30, 17]
print(first_list)
print(len(first_list))
second_list = [29, 1.63, 'Maximiliano', 'Grosman']
print(second_list)
print(type(second_list))
print(type(first_list))
print(second_list[0])
print(second_list[1])
print(second_list[-1])
print(second_list[-3])
print(second_list[-4])
print(second_list[-len(second_list)])#Overthrough way to find the first element in reverse
print(second_list.count(29))
age, height, name, surname = second_list
print(name)
name, surname, age, height = second_list[2], second_list[-1], second_list[0], second_list[1]
print(name, surname, age, height)
print(first_list + second_list)
#More proof that it has dynamic typing
first_list = "Hello World"
print(first_list)
print(type(first_list))
#Additional Upper case Snakecase is a way to use to mark to other developers it's a constant
first_list = [29, 26, 35, 24, 62, 52, 30, 30, 17]

#Use elements of the list
second_list.append('MaxyGrosman2010')
print(second_list)
second_list.insert(1, 'Red')
print(second_list)
second_list.remove('Red')
print(second_list)
first_list.remove(30)#Deletes the first appearance of the desire element
print(first_list)
print(first_list.pop())
print(first_list)
print(first_list.pop(2))#You can indicate which element to remove from the list
print(first_list)
pop_element = first_list.pop(-1)
print(pop_element)
print(first_list)
first_list.sort()
print(first_list)
del first_list[2]#Deletes element without return it when remove from the list through the index
print(first_list)
first_list.clear()
print(first_list)
second_list[-1] = "Red"
print(second_list)
second_list.reverse()
print(second_list)
print(second_list[1:3])#Sub lists.