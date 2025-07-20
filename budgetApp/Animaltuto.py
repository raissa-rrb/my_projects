# just a quick tuto to get back on track
# implement an abstract animal class and some real animals that inherit from it

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name # name is public
    
    # animals can make a sound, but they dont't all make the same so it's abstract
    @abstractmethod
    def sound(self):
        pass

    # animals eat 
    def eat(self):
        print("yum i was hungry")
    
    # animals sleep
    def sleep(self):
        print("zzzz i was tired zzzz")


#children
class Cow(Animal):
    def sound(self):
        print("meuuuuh")

    def __str__(self):
        return f"hi i'm a cow my name is {self.name}"
    
class Dog(Animal):
    def sound(self):
        print("wouf wouf")

    def __str__(self):
        return f"hi i'm a dog my name is {self.name}"

class Cat(Animal):
    def sound(self):
        print("meow meow")

    def __str__(self):
        return f"hi i'm a cat my name is {self.name}"

#instanciate animals
cow0 = Cow("Dolores")
dog0 = Dog("Pluto")
cat0 = Cat("kitty")

animals = [cow0, dog0, cat0]

for i in animals:
    print(i)
    i.eat()
    i.sound()
    print("\n") 

