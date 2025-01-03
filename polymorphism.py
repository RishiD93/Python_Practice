class Animal:
    def speak(self):

        pass

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo! Moo!"

# Polymorphism in action
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())