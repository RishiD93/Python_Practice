

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."


dog = Dog("Crypto")
cat = Cat("meme")

print(dog.speak())  # Output: Buddy barks.
print(cat.speak())  # Output: Whiskers meows.