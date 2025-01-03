
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started."

car = Car()
bike = Motorcycle()

print(car.start_engine())  # Output: Car engine started.
print(bike.start_engine())  # Output: Motorcycle engine started.