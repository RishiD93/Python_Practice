class Animal:

    def __init__(self, name):
        self.__name = name

    def set_name(self, name):

        self.__name = name

    def get_name(self):

        return self.__name

animal = Animal("Dog")
print(f"Animal name: {animal.get_name()}")
animal.set_name("Cat")
print(f"Updated animal name: {animal.get_name()}")