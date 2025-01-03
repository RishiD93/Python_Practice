

class Animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):

        return f"{self.name} says {self.sound}"


dog = Animal("Dog", "Woof")
print(dog.make_sound())