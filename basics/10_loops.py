###Tenth class###

#Loops
my_condition = 0
while my_condition < 10:
    my_condition += 1
    print(my_condition)

while my_condition > 0:
    print(my_condition)
    my_condition -= 1
else: print(f'The counter has reached {my_condition}')#This belongs to the while!!! O:O

#The for works very different, in this case, if there are enough elements it will continue
# until it reaches the last element to go through on the tuple, set, list, dictionary
my_list = [1, 2, 3, 4, 5]
for elememt in my_list:
    print(elememt)
else: print('The list has been look through')

for element in my_list:
    if element == 3:
        print(element)
        break
    print(element)
else: print('End loop')#This is ignore if there is a break