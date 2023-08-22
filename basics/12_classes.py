###Twelfth Class###

# Classes
class Person:
    pass #This is to avoid errors while running code, but do not leave functions or classes 
# with this one
class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.fullname = f"{self.__name} {self.__surname}"
    
    def walk(self):
        print(f'Esta caminando {self.fullname}')

myself = Person("Maximiliano", "Grosman")
print(myself.fullname)
myself.walk()