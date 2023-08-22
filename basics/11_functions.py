###Eleventh class###

#Functions
def first_function():
    print("This is a function")
first_function()

def sum(one, two):
    return one + two
print(sum(2, 2))

def print_all(*args):##The *args is treated as a tuple.
    for arg in args: print(arg)
print_all("Hola", "Mundo")
print_all("Soy", "Maximiliano", "Grosman")
print_all("Me gusta", "La carne")