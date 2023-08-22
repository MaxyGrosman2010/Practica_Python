### Thirteenth class ###

#Exceptions
number_one = 1
number_two = 2
number_two = "2"
#It's not mandatory to use all of the options here, the only mandatory ones are try and except
try:
    print(number_one + number_two)
except:
    print("An error has occurred")
else:#If an error hasn't occurred, it goes to else
    print("There hasn't been an error in the execution")
finally:#It will always run no matter what if there is an error or not
    print("The program continues")

#Exceptions by types
try:
    print(number_one + number_two)
except TypeError: #Only catches errors of TypeError in this case, it can be for other types
    print("An error has occurred of TypeError")
except ValueError:
    print("An error has occurred of ValueError")

#Exceptions by information of exception
try:
    print(number_one + number_two)
except Exception as e:#Exception makes sure that no matter the error it enters here
    print(e)
