class Animals():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        return f"{self.name} is sleeping."
    
    def eat(self):
        return f"{self.name} is eating."
    
class Dog(Animals):
    def bark(self):
        return f"{self.name} says Woof!"

class Fish(Animals):
    def swim(self):
        return f"{self.name} is swimming."
    
class Bird(Animals):
    def fly(self):
        return f"{self.name} is flying."
    
class Monkey(Animals):
    def climb(self):
        return f"{self.name} is climbing."

dog = Dog("Buddy", 3)
fish = Fish("Nemo", 1)
bird = Bird("Kiwi", 2)
monkey = Monkey("George", 5)

print(dog.eat())
print(dog.bark())

print(fish.sleep())
print(fish.swim())

print(bird.fly())
print(monkey.climb())